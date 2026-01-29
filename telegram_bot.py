import logging
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

WELCOME_MESSAGE = (
    "Welcome to Jagaban SMS and Log! How may I be of help?\n"
    "1: site link\n"
    "2: payment issue\n"
    "3: registration issue\n"
    "4: facebook issue\n"
    "5: TikTok issue\n"
    "6: Twitter issue\n"
    "7: want to buy Facebook\n"
    "8: want to buy TikTok\n"
    "9: want to buy VPN\n"
    "10: want to buy instagram\n"
    "11: want to buy twitter\n"
    "12: want to buy WhatsApp\n"
    "13: Facebook 2fa issues\n"
    "14: support"
)

RESPONSES = {
    "1": "Kindly use the site and register 👉https://jagabansmsandlogs.com.ng/products",
    "2": (
        "Kindly watch this video to avoid this issues again https://youtube.com/shorts/a_4NUQ0Kn8I?si=qjzxu3k0hatxLTF-\n"
        "and learn how to avoid this problem but kindly provide your reference.\n"
        "How to get your reference: kindly go to your email, you will see a message from kora pay, scroll down you will see your reference. "
        "Kindly copy it and send it to our email Wisdom9f@gmail.com"
    ),
    "3": (
        "Note that username must be only small letters and you can skip zip code.\n"
        "Watch Tutorial on how to register https://youtu.be/jelkFB5KMRQ?si=UHCZsmnPgkfA_YY4"
    ),
    "4": (
        "Kindly watch this video (https://youtu.be/Txad9v0aE5I?si=tp_-py0gnXuzn_aO)\n"
        "on how to rectify your issues. Make sure you are using chrome and don't forget to on VPN."
    ),
    "5": "Login the email here 👉https://mail.rambler.ru/",
    "6": (
        "Please watch this video and learn how to get 2fa code https://youtube.com/shorts/q9WarZ--KaM?si=wAA67uL1ofQMwhZH"
    ),
    "7": "Kindly use the site and register 👉https://jagabansmsandlogs.com.ng/products",
    "8": "Kindly use the site and register 👉https://jagabansmsandlogs.com.ng/products",
    "9": "Message us on WhatsApp 08101719615",
    "10": "Kindly use the site and register 👉https://jagabansmsandlogs.com.ng/products",
    "11": "Kindly use the site and register 👉https://jagabansmsandlogs.com.ng/products",
    "12": "Kindly message us on WhatsApp 08101719615",
    "13": (
        "Kindly message us via email, send your screenshot of your logs and copy the 2fa key and send to our email Wisdom9f@gmail.com"
    ),
    "14": "Support: Wisdom9f@gmail.com"
}

REPLY_KEYBOARD = [[str(i)] for i in range(1, 15)]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    logger.info(f"User {user.id} started the bot")
    await update.message.reply_text(
        WELCOME_MESSAGE, 
        reply_markup=ReplyKeyboardMarkup(REPLY_KEYBOARD, one_time_keyboard=True, resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages from users."""
    text = update.message.text.strip().lower()
    user = update.effective_user
    
    logger.info(f"User {user.id} ({user.first_name}): {text}")
    
    if text == "hello":
        await update.message.reply_text(
            WELCOME_MESSAGE, 
            reply_markup=ReplyKeyboardMarkup(REPLY_KEYBOARD, one_time_keyboard=True, resize_keyboard=True)
        )
    elif text in RESPONSES:
        await update.message.reply_text(RESPONSES[text])
    else:
        await update.message.reply_text("Please type 'hello' to start or choose an option (1-14) from the menu.")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log the error and send a message to notify the user."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    
    if update and update.message:
        error_message = "Sorry, an error occurred. Please try again or type 'hello' to restart."
        await update.message.reply_text(error_message)

def main():
    """Start the bot."""
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        print("ERROR: Please set the TELEGRAM_BOT_TOKEN environment variable.")
        return
    
    # Create the Application
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    
    # Add message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Add error handler
    app.add_error_handler(error_handler)
    
    # Run the bot
    print("\n" + "="*60)
    print("  🤖 JAGABAN SMS TELEGRAM BOT STARTED")
    print("="*60)
    print("\n✅ Bot is running and listening for messages...")
    print("📱 Open Telegram and start chatting with your bot!")
    print("\n⚠️  Press Ctrl+C to stop the bot\n")
    
    app.run_polling()

if __name__ == "__main__":
    main()
