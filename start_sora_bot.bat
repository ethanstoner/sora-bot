@echo off
REM Start Sora Bot script for Windows

cd /d "%~dp0"

echo Starting Sora Bot...

REM Check if .env exists
if not exist .env (
    echo ERROR: .env file not found!
    echo Please copy .env.example to .env and fill in your API keys.
    pause
    exit /b 1
)

REM Check if running in Docker
where docker-compose >nul 2>&1
if %errorlevel% equ 0 (
    echo Starting with Docker Compose...
    docker-compose up -d
    echo Bot started! Check logs with: docker-compose logs -f
) else (
    echo Docker Compose not found. Starting directly with Python...
    
    REM Check if venv exists
    if not exist venv (
        echo Creating virtual environment...
        python -m venv venv
    )
    
    REM Activate venv and run
    call venv\Scripts\activate.bat
    pip install -q -r requirements.txt
    python sora_bot.py
)
