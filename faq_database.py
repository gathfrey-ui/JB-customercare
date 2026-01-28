"""
FAQ Database Module for Jagaban SMS Customer Care Bot
Contains all FAQ responses and pattern matching for customer queries
"""

# FAQ Database with keywords and responses
FAQ_DATA = {
    "site_link": {
        "keywords": ["site", "link", "website", "jagaban", "url", "web"],
        "response": "🌐 **Site Information**\n\nYou can visit our website at: **https://jagaban.com**\n\nOur website provides:\n• Account management\n• Payment processing\n• Service information\n• Contact support\n• FAQ section\n\nIs there anything specific you'd like to know about our site?"
    },
    "payment_issue": {
        "keywords": ["payment", "pay", "billing", "charge", "credit", "debit", "card", "money", "transaction"],
        "response": "💰 **Payment Support**\n\nWe're here to help with your payment issues!\n\n**Common payment methods:**\n• Credit/Debit Card\n• Bank Transfer\n• Mobile Money\n• Online Wallet\n\n**If your payment failed:**\n1. Check your card details\n2. Ensure sufficient funds\n3. Try again after a few moments\n4. Contact our support team if issues persist\n\n📞 Support: support@jagaban.com\n\nWhat's your specific issue?"
    },
    "registration_issue": {
        "keywords": ["register", "sign up", "account", "create account", "login", "password", "forgot", "reset"],
        "response": "📝 **Account Registration Help**\n\n**Registration Steps:**\n1. Go to https://jagaban.com\n2. Click 'Sign Up'\n3. Enter your email address\n4. Create a strong password\n5. Verify your email\n6. Complete your profile\n\n**Common Issues:**\n• **Can't receive verification email?** Check spam folder or request new link\n• **Forgot password?** Click 'Forgot Password' on login page\n• **Already have account?** Use login instead of signup\n\n💡 Tip: Use a strong password with letters, numbers, and symbols\n\nNeed more help?"
    },
    "facebook_issue": {
        "keywords": ["facebook", "fb", "social media", "share", "link facebook"],
        "response": "📘 **Facebook Support**\n\n**Follow us on Facebook:**\n• Facebook Page: facebook.com/jagaban\n• Stay updated with latest news\n• Get exclusive offers\n• Connect with our community\n\n**Common Issues:**\n• Can't find our page? Search 'Jagaban SMS'\n• Account verification takes 24-48 hours\n• Check privacy settings if posts not visible\n\n**Share your feedback:**\nMessage us directly or leave a comment on our posts!\n\nAnything else about our Facebook?"
    },
    "tiktok_issue": {
        "keywords": ["tiktok", "tik tok", "tt", "viral", "video", "content"],
        "response": "🎵 **TikTok Support**\n\n**Follow us on TikTok:**\n• TikTok: @jagaban_official\n• Watch our latest videos\n• Join our challenges\n• See behind-the-scenes content\n\n**Tips for TikTok:**\n• Turn on notifications for new videos\n• Share our content with friends\n• Participate in comments and challenges\n• Tag us in your videos!\n\n🎥 Make sure to follow us for daily updates!\n\nAny TikTok-related questions?"
    },
    "twitter_issue": {
        "keywords": ["twitter", "x", "tweet", "retweet", "mention", "hashtag"],
        "response": "🐦 **Twitter/X Support**\n\n**Follow us on Twitter:**\n• Twitter/X: @JabaganSMS\n• Real-time updates and news\n• Quick customer support responses\n• Live Q&A sessions\n\n**How to reach us:**\n• Reply to our tweets\n• Send direct messages\n• Use @JabaganSMS in your tweet\n• Follow our hashtag #JabaganCare\n\n📢 We respond to mentions quickly!\n\nWhat's your Twitter question?"
    },
    "general_help": {
        "keywords": ["hello", "hi", "help", "support", "other", "general", "issue"],
        "response": "👋 **Welcome to Jagaban SMS Support!**\n\nThank you for reaching out. How can we assist you?\n\n**Quick Links:**\n🌐 Website: https://jagaban.com\n💬 Email: support@jagaban.com\n📞 Phone: +1-800-JAGABAN (1-800-524-2226)\n\n**Popular Topics:**\n• 💳 Payment & Billing\n• 📝 Account Registration\n• 🌐 Website Help\n• 📘 Social Media\n• 🎵 TikTok\n• 🐦 Twitter\n\nOr describe your issue and we'll help!"
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
