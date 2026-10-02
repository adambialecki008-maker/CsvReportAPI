#define MyAppName "CSV Report Generator"
#define MyAppVersion "0.1.0"
#define MyAppPublisher "EllShenzar"
#define MyAppExeName "CSVReportGenerator.exe"
#define MyAppIcon "assets\csv_report.ico"

[Setup]
AppId={{D40B3E51-3A7D-4B58-A623-47E2BD3DBF34}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={localappdata}\Programs\CSVReportGenerator
DefaultGroupName={#MyAppName}

PrivilegesRequired=lowest
DisableProgramGroupPage=yes
AllowNoIcons=no

OutputDir=release
OutputBaseFilename=CSVReportGenerator-v{#MyAppVersion}-Setup

Compression=lzma2
SolidCompression=yes
WizardStyle=modern

SetupIconFile={#MyAppIcon}

UninstallDisplayName={#MyAppName}
UninstallDisplayIcon={app}\csv_report.ico

[Files]
Source: "dist\CSVReportGenerator\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "assets\csv_report.ico"; DestDir: "{app}"; Flags: ignoreversion

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\csv_report.ico"; IconIndex: 0
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\csv_report.ico"; IconIndex: 0; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
