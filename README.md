# Jagaban SMS Telegram Bot 🤖

A customer care Telegram bot for Jagaban SMS with FAQ integration and conversation logging.

## Features

✨ **Key Features:**
- 👋 Interactive welcome message
- 💬 FAQ-based response system
- 🎯 Intelligent keyword matching
- 📝 Conversation logging
- 📊 Support for multiple customer issues
- 🔧 Easy configuration

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- A Telegram account
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/gathfrey-ui/JB-customercare.git
cd JB-customercare
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Get Your Telegram Bot Token

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy your bot token from BotFather

### Step 5: Configure the Bot

**Option A: Direct Configuration (Simple)**
- Open `telegram_bot.py`
- Find line 27: `TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"`
- Replace with your actual token from BotFather

**Option B: Using Environment Variables (Recommended)**
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and add your token:
   ```
   TELEGRAM_BOT_TOKEN=your_token_here
   ```
3. Update `telegram_bot.py` to load from environment:
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
   ```

### Step 6: Run the Bot

```bash
python telegram_bot.py
```

You should see:
```
============================================================
  🤖 JAGABAN SMS TELEGRAM BOT STARTED
============================================================

✅ Bot is running and listening for messages...
📱 Open Telegram and start chatting with your bot!

⚠️  Press Ctrl+C to stop the bot
```

### Step 7: Test the Bot

1. Open Telegram
2. Search for your bot name
3. Send `/start` to see the welcome message
4. Try different queries:
   - "What is your website?"
   - "I have a payment issue"
   - "How do I register?"
   - "Tell me about your Facebook"

## Project Structure

```
JB-customercare/
├── telegram_bot.py          # Main bot application
├── faq_database.py          # FAQ responses and keyword matching
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variable template
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── conversations.json      # Conversation logs (auto-generated)
```

## Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and see the welcome menu |
| `/help` | Show available commands |
| `/faq` | View all FAQ categories |
| `/reset` | Reset conversation and start fresh |

## FAQ Categories

The bot supports responses for:
- 🌐 **Site Link** - Website information
- 💰 **Payment Issues** - Billing and payment help
- 📝 **Registration** - Account creation and login
- 📘 **Facebook** - Social media information
- 🎵 **TikTok** - TikTok channel details
- 🐦 **Twitter** - Twitter/X presence
- ❓ **General Help** - Default responses

## Customizing FAQ

Edit `faq_database.py` to:
1. Add new categories to `FAQ_DATA`
2. Define keywords that trigger responses
3. Write custom response messages

Example:
```python
FAQ_DATA = {
    "your_category": {
        "keywords": ["keyword1", "keyword2", "keyword3"],
        "response": "Your response message here"
    }
}
```

## Conversation Logs

All conversations are automatically logged to `conversations.json` with:
- Timestamp
- User ID
- User message
- Bot response

Example log entry:
```json
{
  "timestamp": "2026-01-28T10:30:45.123456",
  "user_id": 123456789,
  "user_message": "What is your website?",
  "bot_response": "🌐 **Site Information**\n\nYou can visit our website at: **https://jagaban.com**\n..."
}
```

## Deployment Options

### Option 1: Local Development
- Run on your personal computer
- Good for testing and development

### Option 2: Cloud Hosting
Recommended providers:
- **Heroku** - Free tier available
- **AWS** - EC2 instances
- **Google Cloud** - Cloud Run
- **DigitalOcean** - Droplets
- **PythonAnywhere** - Python hosting

### Option 3: Webhook (Production)
For production, use webhook instead of polling:
```python
# Configure webhook in your bot setup
application.run_webhook(
    listen="0.0.0.0",
    port=8443,
    url_path="/webhook",
    webhook_url="https://yourdomain.com/webhook"
)
```

## Troubleshooting

### Bot not responding
- Check if the bot token is correct
- Ensure you have internet connection
- Verify the bot is running (check terminal output)

### Import errors
```bash
pip install -r requirements.txt --upgrade
```

### Token expired
- Get a new token from @BotFather
- Update the TOKEN in the code

### File permission errors
```bash
chmod +x telegram_bot.py  # On macOS/Linux
```

## Contributing

Feel free to:
- Report bugs
- Suggest improvements
- Add new FAQ categories
- Improve responses

## License

MIT License - See LICENSE file for details

## Support

📧 **Email:** support@jagaban.com  
💬 **Telegram:** @JabaganSMS  
🌐 **Website:** https://jagaban.com

## Resources

- [Python Telegram Bot Documentation](https://docs.python-telegram-bot.org/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [BotFather Guide](https://core.telegram.org/bots#botfather)

---

**Last Updated:** January 28, 2026  
**Version:** 1.0.0  
**Status:** ✅ Ready for Production