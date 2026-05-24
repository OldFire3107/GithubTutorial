@echo off
REM Windows setup. Creates a .venv in the project root and installs requirements.txt.
REM
REM Usage (from cmd.exe or PowerShell):
REM     install.bat
REM Then to play:
REM     .venv\Scripts\activate
REM     python main.py

setlocal

REM ---------- find python ----------
where python >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found on PATH.
    echo Install it from https://www.python.org/downloads/ and tick "Add Python to PATH" during install.
    echo Or via winget: winget install Python.Python.3.12
    exit /b 1
)

REM ---------- check version (>= 3.8) ----------
python -c "import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)"
if errorlevel 1 (
    echo ERROR: Python 3.8+ required.
    python --version
    exit /b 1
)

for /f "delims=" %%v in ('python --version 2^>^&1') do echo Using %%v

REM ---------- create venv ----------
if not exist .venv (
    echo Creating virtual environment in .venv ...
    python -m venv .venv
    if errorlevel 1 (
        echo ERROR: failed to create venv.
        exit /b 1
    )
) else (
    echo .venv already exists, reusing it.
)

REM ---------- install deps ----------
call .venv\Scripts\activate.bat
echo Upgrading pip ...
python -m pip install --upgrade pip >nul
echo Installing requirements ...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: pip install failed.
    exit /b 1
)

echo.
echo Done. To play:
echo     .venv\Scripts\activate
echo     python main.py

endlocal
