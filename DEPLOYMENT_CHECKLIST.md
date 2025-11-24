# ✅ Deployment Checklist

Use this checklist to deploy your bot step-by-step. Check off each item as you complete it!

## 📋 Pre-Deployment Checklist

### Accounts Setup
- [ ] Create GitHub account (if you don't have one)
- [ ] Create Render.com account
- [ ] Have Telegram installed on your phone/computer

---

## 🤖 STEP 1: Create Telegram Bot

- [ ] Open Telegram
- [ ] Search for @BotFather
- [ ] Send `/newbot` command
- [ ] Enter bot name (e.g., "English Practice Bot")
- [ ] Enter username (must end in 'bot', e.g., "my_english_bot")
- [ ] **COPY AND SAVE the bot token** (looks like: `123456789:ABCdef...`)
- [ ] Test: Search for your bot in Telegram and start it

**Bot Token:** `_________________________________` (write it here)

---

## 📁 STEP 2: Setup GitHub Repository

### Create Repository
- [ ] Go to https://github.com
- [ ] Click **+** button → **New repository**
- [ ] Name: `english-practice-bot` (or your choice)
- [ ] Select **Public** (important!)
- [ ] Check **"Add a README file"**
- [ ] Click **Create repository**

### Upload Bot Files
- [ ] Click **Add file** → **Upload files**
- [ ] Upload: `english_practice_bot.py`
- [ ] Upload: `requirements.txt`
- [ ] Upload: `gitignore.txt` (rename to `.gitignore` during upload)
- [ ] Click **Commit changes**

### Configure Bot Code
- [ ] Click on `english_practice_bot.py` in your repo
- [ ] Click **pencil icon** (Edit this file)
- [ ] Find line 14: `GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"`
- [ ] Replace with YOUR GitHub username: `GITHUB_USERNAME = "yourusername"`
- [ ] Find line 15: `GITHUB_REPO = "YOUR_REPO_NAME"`
- [ ] Replace with YOUR repo name: `GITHUB_REPO = "english-practice-bot"`
- [ ] Click **Commit changes**

**Your Settings:**
- GitHub Username: `_________________________________`
- Repository Name: `_________________________________`

### Upload Today's Sentence Files
- [ ] Click **Add file** → **Create new file**
- [ ] Filename: `November 24 English.txt` (use today's date!)
- [ ] Add 5-10 English sentences (one per line)
- [ ] Click **Commit new file**
- [ ] Click **Add file** → **Create new file**
- [ ] Filename: `November 24 Russian.txt` (same date!)
- [ ] Add Russian translations (same number of lines, same order)
- [ ] Click **Commit new file**

**Verify File Naming:**
- [ ] Format is: `[Month] [Day] English.txt` (e.g., "November 24")
- [ ] No "th", "st", "nd", "rd" after day number
- [ ] Full month name (November, not Nov)
- [ ] Space between month and day
- [ ] Both files exist for today

---

## ☁️ STEP 3: Deploy to Render.com

### Connect GitHub
- [ ] Go to https://render.com
- [ ] Click **Sign up with GitHub**
- [ ] Authorize Render to access GitHub
- [ ] Confirm email if required

### Create Web Service
- [ ] Click **New +** → **Web Service**
- [ ] Click **"Build and deploy from a Git repository"**
- [ ] Click **"Configure account"** to connect GitHub (if needed)
- [ ] Find your `english-practice-bot` repository
- [ ] Click **Connect** next to your repository

### Configure Service Settings
Fill in exactly as shown:

- [ ] **Name**: `english-practice-bot` (or your choice)
- [ ] **Region**: (Choose closest to you)
- [ ] **Branch**: `main`
- [ ] **Runtime**: `Python 3`
- [ ] **Build Command**: `pip install -r requirements.txt`
- [ ] **Start Command**: `python english_practice_bot.py`
- [ ] **Instance Type**: Select **Free**

### Add Environment Variable
- [ ] Scroll to **Environment Variables** section
- [ ] Click **Add Environment Variable**
- [ ] **Key**: `BOT_TOKEN`
- [ ] **Value**: (Paste your bot token from Step 1)
- [ ] Click **Add**

### Deploy!
- [ ] Scroll to bottom
- [ ] Click **Create Web Service**
- [ ] Wait 2-5 minutes (watch the build logs)
- [ ] Look for success messages in logs

### Verify Deployment
Check the logs for these messages:
- [ ] "🤖 English Practice Bot is starting..."
- [ ] "📚 Loaded X listening sentences"
- [ ] "🌍 Loaded X translation sentences"
- [ ] "🔔 Daily reminders set for 09:00"
- [ ] Status shows **"Live"** (green indicator)

**Render Service URL:** `_________________________________`

---

## 🧪 STEP 4: Test Your Bot

- [ ] Open Telegram
- [ ] Search for your bot username
- [ ] Click **Start** or send `/start`
- [ ] Verify: You receive welcome message
- [ ] Send `/practice`
- [ ] Verify: Practice session starts
- [ ] Complete Part 1: Listen to a sentence
- [ ] Verify: Audio plays correctly
- [ ] Click "Next" through a few sentences
- [ ] Complete Part 2: See a Russian sentence
- [ ] Send a voice message
- [ ] Verify: English translation appears
- [ ] Complete practice session
- [ ] Verify: Success message appears

### If Something Doesn't Work:
- [ ] Check Render logs for errors
- [ ] Verify BOT_TOKEN is set correctly
- [ ] Check GitHub file naming
- [ ] Try `/reload` command
- [ ] Restart service on Render (Manual Deploy button)

---

## 📅 STEP 5: Prepare for Tomorrow

### Create Tomorrow's Files
- [ ] Go to your GitHub repository
- [ ] Click **Add file** → **Create new file**
- [ ] Filename: `November 25 English.txt` (tomorrow's date!)
- [ ] Add 5-10 new English sentences
- [ ] Click **Commit new file**
- [ ] Create corresponding Russian file
- [ ] Filename: `November 25 Russian.txt`
- [ ] Add Russian translations
- [ ] Click **Commit new file**

### Optional: Batch Create Files
- [ ] Plan your sentences for the week
- [ ] Create 7 days worth of files
- [ ] Upload all at once
- [ ] Bot will automatically use correct file each day

---

## 🎯 Daily Routine (Going Forward)

### Every Day (5 minutes):
- [ ] Create today's date English.txt file
- [ ] Create today's date Russian.txt file
- [ ] Upload both to GitHub
- [ ] (Optional) Test with `/reload` command

### Every Week (Optional):
- [ ] Check Render logs for any errors
- [ ] Verify bot is responding
- [ ] Create next week's files in advance

### Monthly:
- [ ] Review which sentences worked well
- [ ] Adjust difficulty level if needed
- [ ] Clean up old sentence files (optional)

---

## 🎓 Advanced Setup (Optional)

### Keep Free Tier Awake (Prevent Sleep)
- [ ] Go to https://cron-job.org
- [ ] Create free account
- [ ] Create new cron job
- [ ] URL: Your Render service URL
- [ ] Schedule: Every 10 minutes
- [ ] This keeps your bot awake 24/7

### Multiple Students (Create Multiple Bots)
For each student:
- [ ] Repeat Step 1 (create new bot with @BotFather)
- [ ] Create new Render service
- [ ] Use same GitHub repository (or create separate ones)
- [ ] Each bot uses different BOT_TOKEN

### Set Custom Reminder Time
- [ ] Edit `english_practice_bot.py` on GitHub
- [ ] Find line: `REMINDER_TIME = "09:00"`
- [ ] Change to your preferred time (24-hour format)
- [ ] Commit changes
- [ ] Render will auto-redeploy

---

## 🆘 Troubleshooting Checklist

### Bot Not Responding
- [ ] Check Render dashboard - is service "Live"?
- [ ] Check logs for errors
- [ ] Verify BOT_TOKEN is correct
- [ ] Try restarting service (Manual Deploy)

### Can't Find Sentences
- [ ] Verify file naming matches today's date exactly
- [ ] Check files are in repository root (not in folder)
- [ ] Verify GITHUB_USERNAME is correct in code
- [ ] Verify GITHUB_REPO is correct in code
- [ ] Repository is PUBLIC
- [ ] Try `/reload` command

### Audio Not Working
- [ ] Check Render logs for gTTS errors
- [ ] Verify internet connection on Render
- [ ] Audio files are generated on-demand (first use takes longer)

### Daily Reminder Not Sent
- [ ] Free tier might be asleep - set up cron-job.org
- [ ] Check timezone settings
- [ ] Verify scheduler is running (check logs)

### Files Not Updating
- [ ] Wait until midnight for automatic update
- [ ] Or use `/reload` command immediately
- [ ] Verify new files uploaded to GitHub
- [ ] Check file naming is correct

---

## ✅ Final Verification

### Everything Should Be:
- [ ] ✅ Bot created in Telegram
- [ ] ✅ Code uploaded to GitHub
- [ ] ✅ Configuration updated (username, repo)
- [ ] ✅ Today's sentence files uploaded
- [ ] ✅ Bot deployed to Render.com
- [ ] ✅ BOT_TOKEN added as environment variable
- [ ] ✅ Service showing "Live" status
- [ ] ✅ Bot responding in Telegram
- [ ] ✅ Practice session works end-to-end
- [ ] ✅ Tomorrow's files prepared

---

## 🎉 Success!

**Congratulations!** Your bot is now:
- ✅ Running 24/7 in the cloud
- ✅ Reading daily content from GitHub
- ✅ Automatically updating each day
- ✅ Ready for your students to use

### Share with Students:
Give them your bot username: `@_________________________________`

Tell them to:
1. Search for the bot in Telegram
2. Send `/start`
3. Use `/practice` daily

---

## 📝 Notes & Reminders

**Things to Remember:**
- Upload new files BEFORE midnight for automatic update
- Or use `/reload` after uploading anytime
- File naming must be exact: `[Full Month] [Day] English.txt`
- Keep bot token secret
- Check Render logs if issues occur

**Save These Links:**
- Your GitHub Repo: `https://github.com/_______________/_______________`
- Your Render Service: `https://dashboard.render.com/`
- Render Logs: (Click on service → Logs tab)

---

**Date Completed:** _______________

**Your Bot Username:** @_______________

**Service Status:** ☐ Live  ☐ Testing  ☐ Issues

---

*Keep this checklist for reference when creating additional bots!*
