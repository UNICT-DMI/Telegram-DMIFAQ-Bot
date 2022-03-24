# Telegram-DMIFAQ-Bot
An auto-reply FAQ bot designed to be used on Spotted DMI

## Setup
The bot's token is loaded from the BOT_TOKEN environment variable.

After populating the environment, run 'main.py' to start the bot.

## docker-compose
```yaml
version: '2'
services:
  dmifaq-bot:
    container_name: dmifaq-bot
    image: ghcr.io/unict-dmi/dmifaq-bot:master
    environment:
      - BOT_TOKEN=<your-token>
    restart: unless-stopped
```
