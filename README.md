# Discord Server Clone Bot

A simple one-time-use Discord bot built with **Disnake** that clones roles, channels, and basic settings from one server to another.

---

## Features

- Copies all roles (except `@everyone`) with permissions, colors, and settings
- Clones categories and channels (text and voice) preserving order and permissions
- Supports channel topics, slowmode, NSFW flags, bitrate, user limits, etc.
- Simple configuration with source and target server IDs
- Runs once and exits after cloning

---

## Requirements

- Python 3.8+
- Disnake library

---

## Setup

1. Clone this repository

```bash
git clone https://github.com/yourusername/discord-server-clone-bot.git
cd discord-server-clone-bot
```

2. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure your bot token and server IDs in `config.py` from `config.py.example`

---

## Usage

Run the bot with:

```bash
python main.py
```

The bot will connect, copy roles and channels from the source guild to the target guild, then exit automatically.

---

## Notes

- Make sure the bot has administrator permissions on both servers.

- This bot does not copy messages, emojis, webhooks, or bans.

- Run this bot carefully, especially on servers with many channels/roles, to avoid hitting Discord rate limits.

---

## License

This project is licensed under the MIT License.

---

## Author

**Lisdan** — Full-stack developer and Discord/Telegram bot creator.
