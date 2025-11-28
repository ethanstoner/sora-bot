# Sora Prompt Generator Discord Bot

A lightweight Discord bot that generates viral Sora 2 video prompts using Groq API. Perfect for running on a mini PC with minimal resource usage.

## Features

- 🎬 Generates ultra-detailed, viral-worthy Sora prompts
- 🚀 Lightweight and efficient (designed for mini PCs)
- 🐳 Docker-ready with resource limits
- 📝 10 different prompt templates
- ⚡ Fast responses using Groq API

## Setup

### 1. Prerequisites

- Python 3.12+ (if running directly)
- Docker & Docker Compose (if using Docker)
- Discord Bot Token
- Groq API Key

### 2. Configuration

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Fill in your API keys in `.env`:
   ```
   DISCORD_BOT_TOKEN=your_discord_bot_token_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

### 3. Discord Bot Setup

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to "Bot" section and create a bot
4. Enable "Message Content Intent" (required!)
5. Copy the bot token to `.env`
6. Invite bot to your server with appropriate permissions

### 4. Running the Bot

#### Option A: Docker (Recommended)

```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

#### Option B: Direct Python

**Linux/WSL:**
```bash
chmod +x start_sora_bot.sh
./start_sora_bot.sh
```

**Windows:**
```cmd
start_sora_bot.bat
```

**Manual:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 sora_bot.py
```

## Usage

The bot listens on the channel specified by `TARGET_CHANNEL_ID` in your `.env` file.

### Commands

- `!prompt` - Generate a random viral Sora prompt
- `!prompt [1-10]` - Generate prompt for a specific template
- `!templates` - List all available templates
- `!ping` - Check if bot is responding
- `!status` - Check bot status

### Prompt Templates

1. CCTV / Ring Doorbell Camera
2. Funny Animal Fails (Handheld)
3. Body Cam Footage
4. Olympic Broadcast
5. Glow-Up Transformation
6. Character Mashup
7. Animal Superpower
8. Time-Travel / Future Self
9. POV Mini-Story
10. Hidden Camera Prank

## Resource Usage

The bot is designed to be lightweight:
- **CPU**: Limited to 0.5 cores (Docker)
- **Memory**: Limited to 256MB (Docker)
- **Network**: Minimal (only responds to !prompt commands)

## Troubleshooting

### Bot not responding?

1. Check that Message Content Intent is enabled in Discord Developer Portal
2. Verify `TARGET_CHANNEL_ID` in `.env` matches your channel ID
3. Check logs: `docker-compose logs -f` or console output
4. Verify `.env` file has correct tokens and channel ID

### Rate limiting?

Groq free tier has limits (30 requests/min, ~6000 tokens/min). The bot only responds to `!prompt` commands, so rate limiting should be minimal.

### Docker issues?

- Make sure Docker is running
- Check permissions: `docker-compose logs sora-bot`
- Rebuild: `docker-compose build --no-cache`

## Files

- `sora_bot.py` - Main bot file
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker image definition
- `docker-compose.yml` - Docker Compose configuration
- `.env.example` - Environment variables template
- `start_sora_bot.sh` - Linux/WSL startup script
- `start_sora_bot.bat` - Windows startup script

## License

MIT
