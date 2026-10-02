# Integration guide

Copy these files/directories into the root of your existing `CsvReportAPI` repository.

Recommended final commands:

```powershell
python -m pytest
git add .
git status
git commit -m "Prepare v0.1.0 portfolio release"
git push
```

Then create the Windows build:

```powershell
.\build.ps1
```

Compile `installer.iss` in Inno Setup and publish:

```text
release\CSVReportGenerator-v0.1.0-Setup.exe
```

as the binary asset for GitHub Release `v0.1.0`.

Do not commit `build/`, `dist/` or `release/`.
