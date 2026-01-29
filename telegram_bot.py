import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

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
        "How to get your reference: kindly go to your email, you will see a message from kora pay, scroll down you will see your reference.\n"
        "Kindly copy it and send it to our email Wisdom9f@gmail.com"
    ),
    "3": (
        "Note that username must be only small letters and you can skip zip code.\n"
        "Watch Tutorial on how to register https://youtu.be/jelkFB5KMRQ?si=UHCZsmnPgkfA_YY4"
    ),
    "4": (
        "Kindly watch this video (https://youtu.be/Txad9v0aE5I?si=tp_-py0gnXuzn_aO)\n"
        "on how to rectify your issues. Make sure you are using chrome and don’t forget to on VPN."
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
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=ReplyKeyboardMarkup(REPLY_KEYBOARD, one_time_keyboard=True, resize_keyboard=True))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()
    if text == "hello":
        await update.message.reply_text(WELCOME_MESSAGE, reply_markup=ReplyKeyboardMarkup(REPLY_KEYBOARD, one_time_keyboard=True, resize_keyboard=True))
    elif text in RESPONSES:
        await update.message.reply_text(RESPONSES[text])
    else:
        await update.message.reply_text("Please type 'hello' to start or choose an option (1-14) from the menu.")

def main():
    import os
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        print("Please set the TELEGRAM_BOT_TOKEN environment variable.")
        return
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
...existing code...
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
    
    # Run the bot
    print("\n" + "="*60)
    print("  🤖 JAGABAN SMS TELEGRAM BOT STARTED")
    print("="*60)
    print("\n✅ Bot is running and listening for messages...")
    print("📱 Open Telegram and start chatting with your bot!")
    print("\n⚠️  Press Ctrl+C to stop the bot\n")
    
