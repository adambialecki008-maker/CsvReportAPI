import threading
import time
import urllib.request

import uvicorn
import webview

from main import app

HOST = "127.0.0.1"
PORT = 8765
APP_URL = f"http://{HOST}:{PORT}"
HEALTH_URL = f"{APP_URL}/health"


def run_server(server):
    server.run()


def wait_for_server(timeout=10):
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            with urllib.request.urlopen(HEALTH_URL, timeout=0.5) as response:
                if response.status == 200:
                    return
        except Exception:
            time.sleep(0.1)

    raise RuntimeError("FastAPI server did not start.")


def main():
    config = uvicorn.Config(
        app=app,
        host=HOST,
        port=PORT,
        log_level="warning",
        access_log=False,
    )

    server = uvicorn.Server(config)

    server_thread = threading.Thread(
        target=run_server,
        args=(server,),
        daemon=True,
    )

    server_thread.start()

    try:
        wait_for_server()

        # Potrzebne, żeby pobieranie wygenerowanego XLSX działało w oknie.
        webview.settings["ALLOW_DOWNLOADS"] = True

        webview.create_window(
            title="CSV Report Generator",
            url=APP_URL,
            width=1000,
            height=700,
            min_size=(800, 600),
            resizable=True,
        )

        webview.start()

    finally:
        server.should_exit = True
        server_thread.join(timeout=3)


if __name__ == "__main__":
    main()
