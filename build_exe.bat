@echo off
setlocal
cd /d "%~dp0"
"C:\Program Files\LibreOffice\program\python.exe" -m pip install pyinstaller
"C:\Program Files\LibreOffice\program\python.exe" -m PyInstaller --onefile --windowed --name "CDriveInspectionReport" launcher.py
pause
