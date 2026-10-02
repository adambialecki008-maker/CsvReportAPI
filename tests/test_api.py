from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_returns_200():
    response = client.get("/health")

    assert response.status_code == 200


def test_reports_accepts_csv_file():
    with open("tests/fixtures/sample_sales.csv", "rb") as file:
        response = client.post(
            "/reports",
            files={"file": ("sample_sales.csv", file, "text/csv")},
        )

    assert response.status_code == 200


def test_reports_returns_422_for_invalid_csv():
    with open("tests/fixtures/invalid_sales_mixed_errors.csv", "rb") as file:
        response = client.post(
            "/reports",
            files={"file": ("invalid_sales.csv", file, "text/csv")},
        )

    assert response.status_code == 422
    assert response.json()["detail"] != []


def test_reports_returns_422_for_malformed_csv():
    with open("tests/fixtures/malformed.csv", "rb") as file:
        response = client.post(
            "/reports",
            files={"file": ("malformed.csv", file, "text/csv")},
        )

    assert response.status_code == 422
    assert response.json()["detail"] == ["Invalid CSV file"]


def test_reports_returns_required_headers_from_xlsx():
    with open("tests/fixtures/sample_sales.csv", "rb") as file:
        response = client.post(
            "/reports",
            files={"file": ("sample_sales.csv", file, "text/csv")},
        )

    assert (
        response.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    assert (
        'attachment; filename="sales_report.xlsx"'
        in response.headers["content-disposition"]
    )
    assert len(response.content) > 0


def test_home_returns_html():
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
