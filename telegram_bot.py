"""
Telegram Bot Integration for Jagaban SMS Customer Care Bot
This module connects the FAQ database to Telegram
"""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from faq_database import get_response, is_exit_command, FAQ_DATA
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Store conversation logs
conversation_logs = []

class TelegramBotConfig:
    """Configuration for Telegram Bot"""
    # Get token from environment variable or use placeholder
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8535300318:AAH8QOFeo4xBpr6NBX1aqhsvzy4H2mBciII")
    
    @staticmethod
    def validate_token():
        if TelegramBotConfig.TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE" or not TelegramBotConfig.TOKEN:
            raise ValueError(
                "❌ ERROR: No Telegram Bot Token provided!\n\n"
                "To fix this:\n"
                "1. Open Telegram and search for @BotFather\n"
                "2. Send /newbot command\n"
                "3. Follow the instructions\n"
                "4. Copy your bot token\n"
                "5. Create a .env file in the project root\n"
                "6. Add: TELEGRAM_BOT_TOKEN=your_token_here\n"
            )

def log_conversation(user_id, user_message, bot_response):
    """Log conversation to file."""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "user_message": user_message,
        "bot_response": bot_response
    }
    conversation_logs.append(log_entry)
    
    try:
        with open("conversations.json", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        logger.error(f"Error saving conversation: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_message = f"""👋 **Welcome to Jagaban SMS!**

How may I be of help?

1️⃣ Site link
2️⃣ Payment issue
3️⃣ Registration issue
4️⃣ Facebook issue
5️⃣ TikTok issue
6️⃣ Twitter issue
7️⃣ Want to buy Facebook
8️⃣ Want to buy TikTok
9️⃣ Want to buy VPN
🔟 Want to buy Instagram
1️⃣1️⃣ Want to buy Twitter
1️⃣2️⃣ Want to buy WhatsApp
1️⃣3️⃣ Facebook 2FA issues
1️⃣4️⃣ Support

Just reply with the number or describe your issue!"""
    
    await update.message.reply_text(welcome_message)
    log_conversation(user.id, "/start", welcome_message)
    logger.info(f"User {user.id} started the bot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    help_text = """📋 Available Commands:
/start - Start the bot and see the menu
/help - Show this help message
/faq - View all FAQ categories
/reset - Start fresh conversation

Or just type your question or issue and I'll help! 😊"""
    
    await update.message.reply_text(help_text)
    log_conversation(update.effective_user.id, "/help", help_text)

async def faq_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Display all available FAQs."""
    faq_text = "📚 Available FAQ Categories:\n\n"
    
    for i, (category, data) in enumerate(FAQ_DATA.items(), 1):
        keywords_str = ", ".join(data["keywords"])
        faq_text += f"{i}. {category.upper()}\n   Keywords: {keywords_str}\n\n"
    
    await update.message.reply_text(faq_text)
    log_conversation(update.effective_user.id, "/faq", faq_text)

async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Reset the conversation."""
    response = get_response("hello")
    await update.message.reply_text(response)
    log_conversation(update.effective_user.id, "/reset", response)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages from users."""
    user_message = update.message.text
    user = update.effective_user
    
    logger.info(f"User {user.id} ({user.first_name}): {user_message}")
    
    # Check if user wants to exit
    if is_exit_command(user_message):
        farewell = "Thank you for contacting Jagaban SMS! 👋 Feel free to reach out anytime!"
        await update.message.reply_text(farewell)
        log_conversation(user.id, user_message, farewell)
        return
    
    # Get response from FAQ database
    response = get_response(user_message)
    await update.message.reply_text(response)
    log_conversation(user.id, user_message, response)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log the error and send a message to notify the user."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    
    if update:
        error_message = "Sorry, an error occurred. Please try again or type /help"
        await update.message.reply_text(error_message)

def main():
    """Start the bot."""
    
    # Validate token
    try:
        TelegramBotConfig.validate_token()
    except ValueError as e:
        print(str(e))
        return
    
    # Create the Application
    application = Application.builder().token(TelegramBotConfig.TOKEN).build()
    
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("faq", faq_command))
    application.add_handler(CommandHandler("reset", reset_command))
    
    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # log all errors
    application.add_error_handler(error_handler)
    
    # Check if running on Render or similar cloud platform
    port = int(os.getenv("PORT", "8443"))
    webhook_url = os.getenv("WEBHOOK_URL")
    
    # Run the bot
    print("\n" + "="*60)
    print("  🤖 JAGABAN SMS TELEGRAM BOT STARTED")
    print("="*60)
    
    if webhook_url:
        # Production mode - use webhook
        print(f"\n📡 Running in WEBHOOK mode on port {port}")
        print(f"🔗 Webhook URL: {webhook_url}")
        
        application.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path="/webhook",
            webhook_url=webhook_url
        )
    else:
        # Development mode - use polling
        print("\n✅ Bot is running and listening for messages...")
        print("📱 Open Telegram and start chatting with your bot!")
        print("\n⚠️  Press Ctrl+C to stop the bot\n")
        
        application.run_polling()

if __name__ == '__main__':
    main()
