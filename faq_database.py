"""
FAQ Database Module for Jagaban SMS Customer Care Bot
Contains all FAQ responses and pattern matching for customer queries
"""

# FAQ Database with keywords and responses
FAQ_DATA = {
    "welcome": {
        "keywords": ["hello", "hi", "start", "help", "howdy", "hey"],
        "response": """👋 **Welcome to Jagaban SMS!**

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
    },
    "site_link": {
        "keywords": ["site link", "site", "register", "website", "1"],
        "response": """🌐 **Site Link**

Kindly use the site and register 👉 **https://jagabansmsandlogs.com.ng/products**"""
    },
    "payment_issue": {
        "keywords": ["payment issue", "payment", "billing", "pay", "2"],
        "response": """💰 **Payment Issues**

Kindly watch this video to avoid these issues again:
👉 **https://youtube.com/shorts/a_4NUQ0Kn8I?si=qjzxu3k0hatxLTF**

**How to get your reference:**
1. Check your email for a message from Kora Pay
2. Scroll down to find your reference
3. Copy your reference
4. Send it to our email: **Wisdom9f@gmail.com**

We're here to help! 😊"""
    },
    "registration_issue": {
        "keywords": ["registration issue", "registration", "register", "account", "sign up", "3"],
        "response": """📝 **Registration Issues**

**Important Notes:**
• Username must be only small letters (no capitals)
• You can skip the ZIP code field

📺 **Watch Tutorial:**
👉 **https://youtu.be/jelkFB5KMRQ?si=UHCZsmnPgkfA_YY4**

Follow the steps in the video and you'll be set up in no time! 🚀"""
    },
    "facebook_issue": {
        "keywords": ["facebook issue", "facebook", "fb", "4"],
        "response": """📘 **Facebook Issues**

📺 **Watch this video on how to rectify your issues:**
👉 **https://youtu.be/Txad9v0aE5I?si=tp_-py0gnXuzn_aO**

**Important Tips:**
✅ Make sure you are using Chrome browser
✅ Don't forget to turn ON your VPN

Follow these steps and your issue will be resolved! 💯"""
    },
    "tiktok_issue": {
        "keywords": ["tiktok issue", "tiktok", "tik tok", "5"],
        "response": """🎵 **TikTok Issues**

**Login to your email here:**
👉 **https://mail.rambler.ru/**

From there, you can access and resolve your TikTok issues. Let us know if you need further assistance! 😊"""
    },
    "twitter_issue": {
        "keywords": ["twitter issue", "twitter", "tweet", "6"],
        "response": """🐦 **Twitter Issues**

📺 **Please watch this video to learn how to get 2FA code:**
👉 **https://youtube.com/shorts/q9WarZ--KaM?si=wAA67uL1ofQMwhZH**

Follow the steps and you'll resolve your Twitter issues! ✅"""
    },
    "buy_facebook": {
        "keywords": ["buy facebook", "want to buy facebook", "purchase facebook", "7"],
        "response": """📘 **Buy Facebook**

Kindly use the site and register 👉 **https://jagabansmsandlogs.com.ng/products**

You'll find all available Facebook packages there! 🎉"""
    },
    "buy_tiktok": {
        "keywords": ["buy tiktok", "want to buy tiktok", "purchase tiktok", "8"],
        "response": """🎵 **Buy TikTok**

Kindly use the site and register 👉 **https://jagabansmsandlogs.com.ng/products**

Choose from our TikTok packages and start today! 🚀"""
    },
    "buy_vpn": {
        "keywords": ["buy vpn", "want to buy vpn", "purchase vpn", "vpn", "9"],
        "response": """🔒 **Buy VPN**

Please message us on **WhatsApp: 08101719615**

Our team will assist you with VPN purchase options! 💬"""
    },
    "buy_instagram": {
        "keywords": ["buy instagram", "want to buy instagram", "purchase instagram", "instagram", "10"],
        "response": """📸 **Buy Instagram**

Kindly use the site and register 👉 **https://jagabansmsandlogs.com.ng/products**

Get your Instagram packages now! ✨"""
    },
    "buy_twitter": {
        "keywords": ["buy twitter", "want to buy twitter", "purchase twitter", "11"],
        "response": """🐦 **Buy Twitter**

Kindly use the site and register 👉 **https://jagabansmsandlogs.com.ng/products**

Start your Twitter journey with us today! 🚀"""
    },
    "buy_whatsapp": {
        "keywords": ["buy whatsapp", "want to buy whatsapp", "purchase whatsapp", "whatsapp", "12"],
        "response": """💬 **Buy WhatsApp**

Please message us on **WhatsApp: 08101719615**

Our team will help you get the perfect WhatsApp solution! 📱"""
    },
    "facebook_2fa_issue": {
        "keywords": ["facebook 2fa", "2fa issue", "2fa", "facebook 2fa issue", "13"],
        "response": """📘 **Facebook 2FA Issues**

**To resolve your 2FA issue:**

Kindly message us via email with the following:
1. Screenshot of your logs
2. Your 2FA key (copy it exactly)

**Send to:** 📧 **Wisdom9f@gmail.com**

We'll get back to you ASAP! ⚡"""
    },
    "support": {
        "keywords": ["support", "14", "contact", "help us", "email"],
        "response": """📞 **Support**

Need help? Contact us!

📧 **Email:** **Wisdom9f@gmail.com**

Our support team is ready to assist you 24/7! 🎯"""
    },
    "general_help": {
        "keywords": ["other", "general", "issue"],
        "response": """👋 **Welcome to Jagaban SMS!**

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
    }
}

def normalize_text(text):
    """Normalize text for comparison."""
    return text.lower().strip()

def get_response(user_message):
    """
    Get FAQ response based on user message.
    Uses keyword matching to find the most relevant FAQ.
    """
    normalized_message = normalize_text(user_message)
    
    # Check for direct keyword matches
    for category, data in FAQ_DATA.items():
        for keyword in data["keywords"]:
            if keyword in normalized_message:
                return data["response"]
    
    # If no match found, return general help
    return FAQ_DATA["general_help"]["response"]

def is_exit_command(user_message):
    """Check if user wants to exit conversation."""
    exit_keywords = ["exit", "quit", "bye", "goodbye", "thanks", "thank you", "done", "thanks bye"]
    normalized_message = normalize_text(user_message)
    
    return any(keyword in normalized_message for keyword in exit_keywords)

def get_all_faqs():
    """Return all FAQs in a formatted way."""
    faqs = []
    for category, data in FAQ_DATA.items():
        faqs.append({
            "category": category.replace("_", " ").title(),
            "keywords": data["keywords"],
            "response": data["response"]
        })
    return faqs
