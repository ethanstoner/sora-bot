#!/bin/bash
# Start Sora Bot script

cd "$(dirname "$0")"

echo "Starting Sora Bot..."

# Check if .env exists
if [ ! -f .env ]; then
    echo "ERROR: .env file not found!"
    echo "Please copy .env.example to .env and fill in your API keys."
    exit 1
fi

# Check if running in Docker
if command -v docker-compose &> /dev/null; then
    echo "Starting with Docker Compose..."
    docker-compose up -d
    echo "Bot started! Check logs with: docker-compose logs -f"
else
    echo "Docker Compose not found. Starting directly with Python..."
    
    # Check if venv exists
    if [ ! -d venv ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    # Activate venv and run
    source venv/bin/activate
    pip install -q -r requirements.txt
    python3 sora_bot.py
fi
