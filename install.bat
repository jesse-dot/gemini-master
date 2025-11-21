@echo off
REM Installation script for Gemini Master FPS Game AI (Windows)

echo ============================================================
echo Gemini Master - FPS Game AI Installation
echo ============================================================
echo.

REM Check Python
echo Checking Python version...
python --version 2>nul
if errorlevel 1 (
    echo Error: Python not found. Please install Python 3.8 or higher.
    pause
    exit /b 1
)
echo Python found
echo.

REM Create virtual environment
echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip -q
echo pip upgraded
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt -q
echo Dependencies installed
echo.

REM Create .env file
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo .env file created
    echo.
    echo WARNING: Edit .env and add your GEMINI_API_KEY
    echo    Get your key from: https://aistudio.google.com/app/apikey
    echo.
) else (
    echo .env file already exists
)
echo.

REM Run setup test
echo Running setup test...
python test_setup.py
echo.

echo ============================================================
echo Installation Complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Edit .env and add your GEMINI_API_KEY
echo 2. Read README.md for usage instructions
echo 3. Run: python main.py
echo.
echo To activate the virtual environment later:
echo   venv\Scripts\activate.bat
echo.
pause
