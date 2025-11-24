# English Practice Telegram Bot - Deployment Guide

This bot helps students practice English through listening and translation exercises. It reads daily sentences from GitHub files and runs 24/7 on a cloud platform.

## 📋 Prerequisites

- A Telegram account
- A GitHub account
- A Render.com account (free tier works fine)

## 🚀 Step-by-Step Setup Guide

### STEP 1: Create Your Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` command
3. Choose a name for your bot (e.g., "English Practice Bot")
4. Choose a username (must end in 'bot', e.g., "my_english_practice_bot")
5. **SAVE THE TOKEN** - you'll get something like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`
6. Keep this token secret!

### STEP 2: Set Up GitHub Repository

#### 2.1 Create a New Repository
1. Go to https://github.com
2. Click the **+** button (top right) → **New repository**
3. Repository name: `english-practice-bot` (or any name you prefer)
4. Make it **Public** (important for the bot to access files)
5. Check **"Add a README file"**
6. Click **Create repository**

#### 2.2 Upload Bot Files
1. In your repository, click **Add file** → **Upload files**
2. Upload these files:
   - `english_practice_bot.py`
   - `requirements.txt`
   - `.gitignore`

3. Click **Commit changes**

#### 2.3 Upload Daily Sentence Files
1. In your repository, click **Add file** → **Create new file**
2. Name it exactly: `November 24 English.txt` (use today's date)
3. Add sentences, one per line:
   ```
   I need to finish this project by Friday.
   The weather is beautiful today.
   Can you help me with my homework?
   ```
4. Click **Commit new file**

5. Repeat for Russian sentences:
   - Filename: `November 24 Russian.txt`
   - Content (Russian translations, same order):
   ```
   Мне нужно закончить этот проект к пятнице.
   Погода сегодня прекрасная.
   Можешь помочь мне с домашним заданием?
   ```

**IMPORTANT FILE NAMING:**
- Format: `[Month] [Day] English.txt` and `[Month] [Day] Russian.txt`
- Examples: 
  - ✅ `November 24 English.txt`
  - ✅ `December 1 English.txt`
  - ❌ `November 24th English.txt` (no "th")
  - ❌ `Nov 24 English.txt` (full month name)

#### 2.4 Update Bot Configuration
1. In your repository, click on `english_practice_bot.py`
2. Click the **pencil icon** (Edit this file)
3. Find these lines (near the top):
   ```python
   GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"
   GITHUB_REPO = "YOUR_REPO_NAME"
   GITHUB_BRANCH = "main"
   ```
4. Replace with your actual values:
   ```python
   GITHUB_USERNAME = "yourusername"
   GITHUB_REPO = "english-practice-bot"
   GITHUB_BRANCH = "main"
   ```
5. Click **Commit changes**

### STEP 3: Deploy to Render.com

#### 3.1 Create Render Account
1. Go to https://render.com
2. Sign up with your GitHub account (click "Sign up with GitHub")
3. Authorize Render to access your GitHub

#### 3.2 Create a New Web Service
1. Click **New +** → **Web Service**
2. Click **"Build and deploy from a Git repository"**
3. Click **Configure account** to connect your GitHub
4. Find your `english-practice-bot` repository
5. Click **Connect**

#### 3.3 Configure the Service
Fill in these settings:

- **Name**: `english-practice-bot` (or any name)
- **Region**: Choose closest to you
- **Branch**: `main`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python english_practice_bot.py`
- **Instance Type**: Select **Free**

#### 3.4 Add Environment Variable
1. Scroll down to **Environment Variables**
2. Click **Add Environment Variable**
3. Key: `BOT_TOKEN`
4. Value: Paste your Telegram bot token from Step 1
5. Click **Add**

#### 3.5 Deploy
1. Click **Create Web Service** at the bottom
2. Wait 2-5 minutes for deployment
3. Watch the logs - you should see:
   ```
   🤖 English Practice Bot is starting...
   📚 Loaded 5 listening sentences
   🌍 Loaded 5 translation sentences
   ```

### STEP 4: Test Your Bot

1. Open Telegram
2. Search for your bot (the username you created)
3. Send `/start`
4. You should see the welcome message!
5. Try `/practice` to test

### STEP 5: Daily Updates

**Every day, you need to upload new sentence files:**

1. Go to your GitHub repository
2. Click **Add file** → **Create new file**
3. Name it with today's date (e.g., `November 25 English.txt`)
4. Add sentences
5. Repeat for Russian file
6. The bot will automatically load new files at midnight!

**OR use `/reload` command:**
- After uploading new files to GitHub
- Send `/reload` to your bot in Telegram
- It will fetch the latest files immediately

## 📁 File Structure

Your GitHub repository should look like this:
```
english-practice-bot/
├── english_practice_bot.py
├── requirements.txt
├── .gitignore
├── README.md
├── November 24 English.txt
├── November 24 Russian.txt
├── November 25 English.txt
├── November 25 Russian.txt
└── ... (more daily files)
```

## 🎯 Tips

1. **File Format**: Plain text, one sentence per line, UTF-8 encoding
2. **Same Number**: English and Russian files must have the same number of lines
3. **Advance Preparation**: Upload files for multiple days in advance
4. **Check Logs**: On Render.com, click "Logs" to see if files loaded correctly
5. **Keep Bot Token Secret**: Never share it publicly!

## ⚠️ Troubleshooting

### Bot doesn't respond
- Check Render logs for errors
- Make sure BOT_TOKEN is set correctly
- Verify the bot is running (green "Live" badge on Render)

### Can't find sentences
- Check file naming exactly matches format: `November 24 English.txt`
- Verify files are in the root of your repository
- Check GITHUB_USERNAME and GITHUB_REPO in code
- Try `/reload` command

### Render service stopped
- Free tier sleeps after 15 minutes of inactivity
- It will wake up when you message the bot
- For 24/7 uptime, consider upgrading to paid tier

## 📱 Bot Commands

- `/start` - Start the bot and see welcome message
- `/practice` - Begin today's practice session
- `/reload` - Manually reload today's sentences from GitHub
- `/help` - Show help message

## 🔧 Advanced: Keeping Free Tier Awake

Render's free tier sleeps after 15 minutes. To keep it awake:

1. Use a service like **cron-job.org**
2. Create a scheduled job to ping your Render URL every 10 minutes
3. URL format: `https://your-service-name.onrender.com`

## 📝 Notes

- Bot token in code is a backup; environment variable takes priority
- Audio files are generated on-demand and stored temporarily
- The bot automatically reloads content at midnight
- Daily reminders sent at 09:00 (configurable in code)

---

**Need help?** Check the Render logs for error messages!
