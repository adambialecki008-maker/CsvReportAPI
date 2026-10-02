# CSV Report Generator v0.1.0

First portfolio-ready desktop release.

## Highlights

- Windows desktop application with pywebview
- local FastAPI backend
- CSV upload and validation
- row-level validation messages
- Excel report generation
- `Sales` and `Summary` worksheets
- calculated revenue per sale
- total revenue, order count and units sold
- revenue aggregation per customer and product
- PyInstaller `onedir` build
- Inno Setup installer and uninstaller
- custom application and shortcut icon
- automated pytest suite

## Input schema

```text
date,customer,product,quantity,unit_price
```

Validation rules:

- `date`: valid `YYYY-MM-DD`
- `customer`: non-empty
- `product`: non-empty
- `quantity`: positive integer
- `unit_price`: non-negative number

## Installation

Download:

```text
CSVReportGenerator-v0.1.0-Setup.exe
```

Run the installer and launch **CSV Report Generator** from the Start menu or desktop shortcut.

## Notes

The desktop version runs its API locally on the loopback interface. No external server is required for report processing.
