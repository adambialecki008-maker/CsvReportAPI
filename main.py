from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.templating import Jinja2Templates
from csv_file_repository import read_csv_file
from validation import validate_file
from excel_report_repository import create_excel_report
from pathlib import Path
import sys

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/reports")
def create_report(file: UploadFile = File()):
    data = read_csv_file(file.file)
    errors = validate_file(data)
    if errors:
        raise HTTPException(
            status_code=422,
            detail=errors,
        )
    report = create_excel_report(data)
    return StreamingResponse(
        report,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": 'attachment; filename="sales_report.xlsx"'},
    )


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


def resource_path(relative_path: str) -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent

    return base_path / relative_path


templates = Jinja2Templates(directory=str(resource_path("templates")))
