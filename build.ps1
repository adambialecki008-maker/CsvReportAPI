$ErrorActionPreference = "Stop"

Write-Host "Running tests..."
python -m pytest

Write-Host "Cleaning previous build..."
Remove-Item -Recurse -Force build, dist -ErrorAction SilentlyContinue
Remove-Item CSVReportGenerator.spec -ErrorAction SilentlyContinue

Write-Host "Building CSV Report Generator..."
python -m PyInstaller launcher.py `
    --name CSVReportGenerator `
    --onedir `
    --windowed `
    --icon "assets\csv_report.ico" `
    --add-data "templates;templates" `
    --clean

Write-Host ""
Write-Host "Build complete:"
Write-Host "dist\CSVReportGenerator\CSVReportGenerator.exe"
