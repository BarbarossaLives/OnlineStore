@echo off
echo 🏪 Local Store Development Setup
echo =================================

echo.
echo 🚀 Starting local development setup...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not available. Please install Python 3.8+ and try again.
    pause
    exit /b 1
)

echo ✅ Python found!

REM Run the Python setup script
python run_local.py

echo.
echo 🎉 Setup complete! Press any key to exit.
pause >nul

