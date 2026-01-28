# Deploying to Render.com

## Problem You're Experiencing
`Conflict: terminated by other getUpdates request; make sure that only one bot instance is running`

This happens because the **polling method** allows multiple bot instances to run simultaneously, causing conflicts. The solution is to use **webhook mode** on Render.

## Solution: Use Webhook Mode

### Step 1: Stop Current Bot on Render
1. Go to https://render.com/dashboard
2. Find your service
3. Click "Suspend" or "Deleted" (clear any running instances)
4. Wait 2-3 minutes

### Step 2: Update Environment Variables
In Render Dashboard → Environment:

```
TELEGRAM_BOT_TOKEN=8535300318:AAH8QOFeo4xBpr6NBX1aqhsvzy4H2mBciII
WEBHOOK_URL=https://your-service-name.onrender.com/webhook
```

Replace `your-service-name` with your actual Render service name.

### Step 3: Update .env File Locally (for testing)
```bash
TELEGRAM_BOT_TOKEN=8535300318:AAH8QOFeo4xBpr6NBX1aqhsvzy4H2mBciII
WEBHOOK_URL=https://your-service-name.onrender.com/webhook
```

### Step 4: Commit and Deploy
```bash
git add .
git commit -m "Switch to webhook mode for production deployment"
git push origin main
```

Render will auto-deploy on push.

### Step 5: Verify
The bot will now:
- Use **webhook mode** if `WEBHOOK_URL` is set
- Use **polling mode** locally for development

## Why Webhook is Better for Render

| Feature | Polling | Webhook |
|---------|---------|---------|
| Multiple instances | ❌ Conflicts | ✅ Works fine |
| Server resources | High | Low |
| Real-time | ~1-2 seconds delay | Instant |
| Best for | Development | Production |

## If It Still Fails

1. **Reset API offset:**
   - Open browser: `https://api.telegram.org/bot{YOUR_TOKEN}/getMe`
   - Replace `{YOUR_TOKEN}` with your actual token

2. **Create new bot token:**
   - Open Telegram → @BotFather
   - Send `/mybots`
   - Select your bot → /revoke
   - Create new bot with /newbot

3. **Clear old deployment:**
   - Stop all dynos/services
   - Wait 5 minutes before restarting

## Local Testing (Polling)
```bash
# Make sure WEBHOOK_URL is NOT set in .env
unset WEBHOOK_URL
python telegram_bot.py
```

## Production Deployment (Webhook)
```bash
# WEBHOOK_URL MUST be set in environment variables
export WEBHOOK_URL=https://your-domain.onrender.com/webhook
python telegram_bot.py
```

---

Need help? Check Render docs: https://render.com/docs
