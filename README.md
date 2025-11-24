# 🎓 English Practice Bot - Complete Package

## 📦 What You Have

This package contains everything you need to deploy your Telegram English practice bot to run 24/7 in the cloud!

### Files Included:

1. **english_practice_bot.py** - The main bot code (modified to read from GitHub)
2. **requirements.txt** - Python dependencies
3. **gitignore.txt** - Files to exclude from GitHub (rename to `.gitignore`)
4. **November 24 English.txt** - Example English sentences
5. **November 24 Russian.txt** - Example Russian translations
6. **DEPLOYMENT_GUIDE.md** - Complete step-by-step instructions
7. **KEY_CHANGES.md** - Summary of what changed from your original bot

## 🚀 Quick Start (5 Steps)

### 1️⃣ GitHub Setup (10 minutes)
- Create a new public repository on GitHub
- Upload all the files
- Update the code with your GitHub username/repo name

### 2️⃣ Create Telegram Bot (5 minutes)
- Message @BotFather on Telegram
- Get your bot token

### 3️⃣ Deploy to Render.com (10 minutes)
- Sign up at render.com
- Connect your GitHub repository
- Add your bot token as an environment variable
- Click "Deploy"

### 4️⃣ Test (2 minutes)
- Open your bot in Telegram
- Send `/start`
- Try `/practice`

### 5️⃣ Daily Updates (5 minutes per day)
- Upload new sentence files to GitHub daily
- Format: `November 25 English.txt` and `November 25 Russian.txt`

## 🎯 Three Ways to Deploy

### Option 1: Render.com (Recommended - Free)
✅ Easy setup
✅ Free tier available
✅ Automatic deployments from GitHub
✅ Simple dashboard
⚠️ Sleeps after 15 min inactivity on free tier

### Option 2: Railway.app (Alternative - Free)
✅ Similar to Render
✅ Free tier with $5 monthly credit
✅ Good for small bots
✅ Easy GitHub integration

### Option 3: Heroku (Paid)
⚠️ No free tier anymore
💰 $5/month minimum
✅ Very reliable
✅ Large community

**We recommend Render.com for beginners!**

## 📝 Important Configuration

Before deploying, you MUST update these lines in `english_practice_bot.py`:

```python
# Line 14-16
GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"  # ← Change this!
GITHUB_REPO = "YOUR_REPO_NAME"            # ← Change this!
GITHUB_BRANCH = "main"                     # Usually "main"
```

Example:
```python
GITHUB_USERNAME = "john_doe"
GITHUB_REPO = "english-practice-bot"
GITHUB_BRANCH = "main"
```

## 📅 Daily File Naming Rules

### ✅ Correct Format:
```
November 24 English.txt
November 24 Russian.txt
December 1 English.txt
December 1 Russian.txt
January 15 English.txt
```

### ❌ Wrong Format:
```
November 24th English.txt  ← No "th"
Nov 24 English.txt         ← Full month name
November 01 English.txt    ← No leading zero
24-11-2024 English.txt     ← Wrong format
```

### File Content:
```
First sentence in English
Second sentence in English
Third sentence in English
```
(One sentence per line, plain text)

## 🔧 Customization Options

You can easily customize:

```python
REMINDER_TIME = "09:00"  # Change reminder time
```

In the code, you can also modify:
- Welcome messages
- Button texts
- Practice flow
- Audio settings

## 🎬 Complete Workflow

```
You                     GitHub                 Render.com              Students
│                          │                        │                      │
│─── Upload bot code ─────>│                        │                      │
│                          │                        │                      │
│─── Upload daily files ──>│                        │                      │
│                          │                        │                      │
│                          │<─── Auto deploy ───────│                      │
│                          │                        │                      │
│                          │                        │<──── /start ─────────│
│                          │                        │                      │
│                          │<─── Fetch files ───────│                      │
│                          │                        │                      │
│                          │──── Return data ──────>│                      │
│                          │                        │                      │
│                          │                        │─── Send practice ───>│
```

## ⏰ Timeline

**Initial Setup:** ~30 minutes
- Create accounts: 10 min
- Upload files: 5 min
- Deploy: 10 min
- Test: 5 min

**Daily Maintenance:** ~5 minutes
- Create sentence files: 3 min
- Upload to GitHub: 2 min

**Weekly Batch:** ~30 minutes
- Create 7 days of files at once
- Upload all at once
- Bot handles the rest automatically

## 🆘 Getting Help

### Check These First:
1. **Render.com Logs** - Shows all errors
2. **GitHub Files** - Verify naming is correct
3. **Bot Token** - Make sure it's set in Render
4. **Repository** - Must be public

### Common Solutions:
- Bot not responding? → Check Render logs
- Can't find sentences? → Check file naming
- Bot offline? → Free tier might be asleep
- Errors in logs? → Check GitHub username/repo settings

## 🎓 Learning Resources

### Render.com Documentation:
https://render.com/docs

### Python Telegram Bot:
https://github.com/eternnoir/pyTelegramBotAPI

### Telegram Bot API:
https://core.telegram.org/bots/api

## 📊 What's Different from Your Original Bot?

| Feature | Old Bot | New Bot |
|---------|---------|---------|
| Location | Your computer | Cloud (24/7) |
| Data source | Local JSON | GitHub files |
| Updates | Manual edit | Upload to GitHub |
| Daily content | Static | Date-based, automatic |
| Availability | When PC on | Always |

## ✨ Benefits of New Setup

1. **24/7 Availability** - Bot runs even when your computer is off
2. **Easy Updates** - Just upload new files to GitHub
3. **Automatic Daily Changes** - Bot picks correct file by date
4. **Version Control** - GitHub tracks all changes
5. **Multiple Students** - Create multiple bots from same code
6. **Backup** - All files safely stored on GitHub
7. **Professional** - Industry-standard deployment

## 🔐 Security Reminders

1. **Never share your bot token publicly**
2. **Use environment variables for tokens**
3. **Don't commit tokens to GitHub**
4. **Keep repository public only for sentence files**
5. **Consider private repo + access token (advanced)**

## 📞 Next Steps

1. Read **DEPLOYMENT_GUIDE.md** for detailed instructions
2. Read **KEY_CHANGES.md** to understand modifications
3. Follow the 5-step Quick Start above
4. Test thoroughly before giving to students
5. Prepare first week of sentence files

---

## 🎉 You're Ready!

You now have everything needed to:
- ✅ Deploy a cloud-hosted Telegram bot
- ✅ Manage content via GitHub
- ✅ Provide 24/7 English practice to your students
- ✅ Easily create bots for multiple students

**Good luck with your English teaching bot!** 🚀

---

*Questions? Check the DEPLOYMENT_GUIDE.md for troubleshooting!*
