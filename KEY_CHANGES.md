# Quick Reference: Key Changes from Original Bot

## 🔄 What Changed?

### 1. **Content Loading (MAJOR CHANGE)**
**Before:**
```python
LISTENING_FILE = os.path.join(CONTENT_DIR, 'listening.json')
TRANSLATION_FILE = os.path.join(CONTENT_DIR, 'translation.json')
```

**After:**
```python
# Reads from GitHub using date-based filenames
# Example: "November 24 English.txt" and "November 24 Russian.txt"
def load_sentences_from_github(filename):
    url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/{filename}"
    response = requests.get(url)
    sentences = [line.strip() for line in response.text.split('\n') if line.strip()]
    return sentences
```

### 2. **File Format**
**Before:** JSON files
```json
["sentence 1", "sentence 2", "sentence 3"]
```

**After:** Plain text files (one sentence per line)
```
sentence 1
sentence 2
sentence 3
```

### 3. **Configuration**
You must update these variables in the code:
```python
GITHUB_USERNAME = "yourusername"     # Your GitHub username
GITHUB_REPO = "english-practice-bot"  # Your repository name
GITHUB_BRANCH = "main"                # Usually "main" or "master"
```

### 4. **New Commands**
- `/reload` - Manually reload today's sentences from GitHub

### 5. **Automatic Daily Updates**
- Bot reloads content at midnight (00:01) automatically
- Bot also reloads content when sending daily reminders (09:00)

## 📅 File Naming Convention

### Date Format
The bot uses: `datetime.now().strftime("%B %d")`
- This creates: "November 24", "December 1", "January 15"
- **No leading zeros**: "November 1" not "November 01"
- **Full month name**: "November" not "Nov"

### Required Files (Daily)
For each day, you need TWO files:
1. `[Date] English.txt` - English sentences
2. `[Date] Russian.txt` - Russian translations

### Examples
✅ Correct:
- `November 24 English.txt`
- `November 24 Russian.txt`
- `December 1 English.txt`
- `December 1 Russian.txt`

❌ Wrong:
- `November 24th English.txt` (no "th")
- `Nov 24 English.txt` (abbreviated month)
- `November 01 English.txt` (leading zero)
- `24 November English.txt` (wrong order)

## 🌐 How It Works

```
┌─────────────────┐
│   GitHub Repo   │
│                 │
│  Nov 24 Eng.txt │─┐
│  Nov 24 Rus.txt │ │
│  Nov 25 Eng.txt │ │  Your daily sentence files
│  Nov 25 Rus.txt │ │
└─────────────────┘ │
                    │
                    │ Bot fetches via HTTP
                    ▼
┌─────────────────────────┐
│    Render.com Server    │
│                         │
│  english_practice_bot   │  Running 24/7
│         .py             │
└─────────────────────────┘
                    │
                    │ Telegram API
                    ▼
┌─────────────────────────┐
│   Telegram Users        │
│   📱 Your Students      │
└─────────────────────────┘
```

## 🔐 Security Notes

### Bot Token
**Method 1 (Recommended):** Environment Variable
- Set `BOT_TOKEN` in Render.com dashboard
- Bot reads from: `os.environ.get('BOT_TOKEN')`

**Method 2 (Fallback):** Hardcoded
- Token in code as backup
- **NEVER commit token to public GitHub!**
- Use environment variables in production

### GitHub Files
- Repository must be **PUBLIC** for bot to read files
- Or use GitHub Personal Access Token (advanced)

## 🆚 Comparison Table

| Feature | Original Bot | New Bot |
|---------|-------------|---------|
| Runs from | Your computer | Cloud (Render.com) |
| Data storage | Local JSON files | GitHub text files |
| Availability | Only when computer on | 24/7 |
| Updates | Manual file edit | Upload to GitHub |
| File format | JSON | Plain text |
| Daily content | Static | Dynamic (date-based) |

## 📦 Dependencies

```
pyTelegramBotAPI==4.14.0  # Telegram bot library
gTTS==2.5.0               # Text-to-speech for audio
schedule==1.2.0            # Daily task scheduling
requests==2.31.0           # HTTP requests to GitHub
```

## 🎯 Quick Start Checklist

- [ ] Create Telegram bot with @BotFather
- [ ] Create GitHub repository (public)
- [ ] Upload bot files to GitHub
- [ ] Update GITHUB_USERNAME and GITHUB_REPO in code
- [ ] Create today's sentence files
- [ ] Create Render.com account
- [ ] Deploy to Render.com
- [ ] Add BOT_TOKEN environment variable
- [ ] Test bot with /start command
- [ ] Test practice with /practice command

## 💡 Tips for Daily Use

1. **Prepare files in advance**: Create files for the whole week
2. **Consistent format**: Always use same structure
3. **Backup**: Keep a local copy of all sentence files
4. **Test locally**: You can still run locally to test new sentences
5. **Monitor**: Check Render logs occasionally

## 🐛 Common Issues

### "No content available for today"
→ File naming doesn't match today's date
→ Files not uploaded to GitHub
→ Check GITHUB_USERNAME/GITHUB_REPO settings

### Bot doesn't update to new day's content
→ Wait until midnight or use `/reload`
→ Check that new files are uploaded

### Audio not working
→ gTTS service might be down (rare)
→ Check Render logs for errors

---

**Remember**: The key difference is that your bot now reads from GitHub instead of local files, and uses the current date to determine which files to read!
