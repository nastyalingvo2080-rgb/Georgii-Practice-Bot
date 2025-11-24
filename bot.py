# bot.py
import os
import time
import threading
import requests
from datetime import datetime
from gtts import gTTS
import telebot
from telebot import types
from urllib.parse import quote_plus

# ---------- CONFIG ----------
# Put your real TELEGRAM BOT TOKEN into Render's environment variables as BOT_TOKEN
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("Set BOT_TOKEN environment variable")

# Set the folder name for this student (Georgii)
STUDENT_FOLDER = "Georgii"

# Raw GitHub base (auto for your repo)
GITHUB_RAW_BASE = os.environ.get(
    "GITHUB_RAW_BASE",
    "https://raw.githubusercontent.com/nastyalingvo2080-rgb/Georgii-Practice-Bot/main"
)

# Optional: daily reminder time if you want scheduled reminders (HH:MM)
REMINDER_TIME = os.environ.get("REMINDER_TIME", "09:00")

# ---------- END CONFIG ----------

bot = telebot.TeleBot(BOT_TOKEN)
user_states = {}

AUDIO_CACHE_DIR = "/tmp/bot_audio"
os.makedirs(AUDIO_CACHE_DIR, exist_ok=True)


class UserState:
    def __init__(self):
        self.stage = None
        self.sentence_index = 0
        self.show_text = False
        self.text_message_id = None
        self.listening_sentences = []
        self.translation_items = []  # list of dicts {russian, english}


def get_user_state(user_id):
    if user_id not in user_states:
        user_states[user_id] = UserState()
    return user_states[user_id]


def reset_user_state(user_id):
    if user_id in user_states:
        del user_states[user_id]


def build_file_url(folder: str, filename: str):
    # Join and URL-encode the path
    # Example filename: "November 24 English" or "November 24 English.txt"
    path = f"{quote_plus(folder)}/{quote_plus(filename)}"
    return f"{GITHUB_RAW_BASE}/{path}"


def try_fetch_file(folder: str, filename_base: str):
    """
    Try a list of candidate extensions / names and return text (or None).
    """
    candidates = [
        filename_base,
        filename_base + ".txt",
        filename_base + ".md",
        filename_base + ".json"
    ]
    for cand in candidates:
        url = build_file_url(folder, cand)
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200 and r.text.strip():
                return r.text
        except Exception:
            pass
    return None


def parse_listening_text(text: str):
    # One sentence per line, ignore empty lines
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    return lines


def parse_translation_text(text: str):
    """
    Accepts:
      - pairs (Russian line followed by English line separated by blank lines)
      - or alternating lines
      - or single language lines (then english field empty)
    Returns list of dicts: {russian: str, english: str}
    """
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    items = []
    i = 0
    while i < len(lines):
        ru = lines[i]
        en = ""
        if i + 1 < len(lines):
            # if next line contains ASCII letters, assume it's English
            nxt = lines[i + 1]
            # crude test: presence of Latin letters or apostrophe
            if any(c.isalpha() and c.lower() in "abcdefghijklmnopqrstuvwxyz" for c in nxt):
                en = nxt
                i += 2
            else:
                # no english next, keep english empty
                i += 1
        else:
            i += 1
        items.append({"russian": ru, "english": en})
    return items


def fetch_today_content(folder):
    # Build date like "November 24"
    today = datetime.now()
    date_str = today.strftime("%B %-d" if os.name != "nt" else "%B %#d")  # NB: %-d works on Unix; Render is Unix
    # to be safe, also build with zero-padded day
    date_str_alt = today.strftime("%B %d")  # "November 24" or "November 04"
    # Try first format without leading zeros
    name_base_1 = f"{date_str} English"
    name_base_2 = f"{date_str_alt} English"

    listening_text = try_fetch_file(folder, name_base_1) or try_fetch_file(folder, name_base_2)
    if listening_text:
        listening = parse_listening_text(listening_text)
    else:
        listening = []

    # Russian translations
    rname_base_1 = f"{date_str} Russian"
    rname_base_2 = f"{date_str_alt} Russian"
    translation_text = try_fetch_file(folder, rname_base_1) or try_fetch_file(folder, rname_base_2)
    translation_items = parse_translation_text(translation_text) if translation_text else []

    return listening, translation_items


def generate_audio(text, idx, prefix="listening"):
    # create filename deterministic for caching
    safe_name = f"{prefix}_{idx}.mp3"
    path = os.path.join(AUDIO_CACHE_DIR, safe_name)
    if os.path.exists(path):
        return path
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(path)
        return path
    except Exception as e:
        print("gTTS error:", e)
        return None


# ---- Telegram handlers (similar to your original bot) ----

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "👋 Welcome to English Practice Bot!\n\n"
                 "I'm ready to fetch today's practice when you press /practice.\n\n"
                 "Commands:\n"
                 "/practice - Start today's practice\n"
                 "/help - Get help\n\n"
                 "Make sure you've pressed Start so I can message you.")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,
                 "🤖 How to use this bot:\n\n"
                 "1. Type /practice to start\n"
                 "2. Part 1: Listen and repeat sentences (I will send audio)\n"
                 "3. Part 2: Translate Russian sentences to English\n\n"
                 "If I can't find today's files on the server, I'll tell you.")


@bot.message_handler(commands=['practice'])
def start_practice(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    reset_user_state(user_id)
    state = get_user_state(user_id)

    markup = types.InlineKeyboardMarkup()
    btn_yes = types.InlineKeyboardButton("✅ Yes, let's start!", callback_data="start_practice")
    markup.add(btn_yes)
    bot.send_message(chat_id,
                     "🎯 Ready for today's English practice?\n\n"
                     "I'll fetch today's files from the server and start the session.",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    user_id = call.from_user.id
    state = get_user_state(user_id)

    if call.data == "start_practice":
        bot.answer_callback_query(call.id)
        # fetch today's content live from GitHub
        listening, translations = fetch_today_content(STUDENT_FOLDER)
        state.listening_sentences = listening
        state.translation_items = translations

        if not listening and not translations:
            bot.send_message(call.message.chat.id,
                             "❌ I couldn't find today's files on the server.\n"
                             "Please make sure the files are in the repository under folder "
                             f"'{STUDENT_FOLDER}' and named like 'November 24 English' and 'November 24 Russian'.")
            return

        # Start Part 1
        state.stage = 'listening'
        state.sentence_index = 0
        state.show_text = False
        bot.send_message(call.message.chat.id,
                         "📚 *Part 1: Listen and Repeat*\n\nInstructions:\n1. Listen\n2. Repeat aloud\n3. Click Next",
                         parse_mode='Markdown')
        time.sleep(1)
        send_listening_sentence(call.message.chat.id, user_id)

    elif call.data == "show_text":
        if not state.show_text:
            state.show_text = True
            sentence = state.listening_sentences[state.sentence_index]
            sent_msg = bot.send_message(call.message.chat.id, f"📝 {sentence}")
            state.text_message_id = sent_msg.message_id
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn_hide = types.InlineKeyboardButton("🙈 Hide text", callback_data="hide_text")
            btn_next = types.InlineKeyboardButton("➡️ Next", callback_data="next_listening")
            markup.add(btn_hide, btn_next)
            try:
                bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                             message_id=call.message.message_id,
                                             reply_markup=markup)
            except:
                pass
        bot.answer_callback_query(call.id)

    elif call.data == "hide_text":
        if state.show_text and state.text_message_id:
            try:
                bot.delete_message(chat_id=call.message.chat.id,
                                   message_id=state.text_message_id)
            except:
                pass
            state.show_text = False
            state.text_message_id = None
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn_show = types.InlineKeyboardButton("📝 Show text", callback_data="show_text")
            btn_next = types.InlineKeyboardButton("➡️ Next", callback_data="next_listening")
            markup.add(btn_show, btn_next)
            try:
                bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                             message_id=call.message.message_id,
                                             reply_markup=markup)
            except:
                pass
        bot.answer_callback_query(call.id)

    elif call.data == "next_listening":
        bot.answer_callback_query(call.id)
        state.sentence_index += 1
        state.show_text = False
        state.text_message_id = None
        if state.sentence_index < len(state.listening_sentences):
            send_listening_sentence(call.message.chat.id, user_id)
        else:
            start_translation(call.message.chat.id, user_id)

    elif call.data == "play_audio":
        bot.answer_callback_query(call.id)
        idx = state.sentence_index
        if idx < len(state.translation_items):
            item = state.translation_items[idx]
            audio_filename = f"translation_{idx:02d}.mp3"
            audio_path = generate_audio(item.get('english', item.get('russian', '')), idx, prefix="translation")
            if audio_path and os.path.exists(audio_path):
                with open(audio_path, 'rb') as audio:
                    bot.send_voice(call.message.chat.id, audio)

    elif call.data == "next_translation":
        bot.answer_callback_query(call.id)
        state.sentence_index += 1
        state.show_text = False
        if state.sentence_index < len(state.translation_items):
            send_translation_sentence(call.message.chat.id, user_id)
        else:
            finish_practice(call.message.chat.id, user_id)


def send_listening_sentence(chat_id, user_id):
    state = get_user_state(user_id)
    if state.sentence_index >= len(state.listening_sentences):
        start_translation(chat_id, user_id)
        return
    sentence = state.listening_sentences[state.sentence_index]
    audio_path = generate_audio(sentence, state.sentence_index, prefix="listening")
    if audio_path and os.path.exists(audio_path):
        with open(audio_path, 'rb') as audio:
            bot.send_voice(chat_id, audio)
    time.sleep(0.3)
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_show = types.InlineKeyboardButton("📝 Show text", callback_data="show_text")
    btn_next = types.InlineKeyboardButton("➡️ Next", callback_data="next_listening")
    markup.add(btn_show, btn_next)
    bot.send_message(chat_id, "Repeat the sentence aloud", reply_markup=markup)


def start_translation(chat_id, user_id):
    state = get_user_state(user_id)
    state.stage = 'translation'
    state.sentence_index = 0
    bot.send_message(chat_id, "✅ Great job on Part 1!")
    time.sleep(1)
    bot.send_message(chat_id,
                     "🌍 *Part 2: Translation*\n\n"
                     "Instructions:\n"
                     "1. Read the Russian sentence\n"
                     "2. Say the translation in English\n"
                     "3. Record your voice and send it (I will reply with the correct answer)",
                     parse_mode='Markdown')
    time.sleep(1)
    send_translation_sentence(chat_id, user_id)


def send_translation_sentence(chat_id, user_id):
    state = get_user_state(user_id)
    if state.sentence_index >= len(state.translation_items):
        finish_practice(chat_id, user_id)
        return
    item = state.translation_items[state.sentence_index]
    bot.send_message(chat_id, f"🇷🇺 {item.get('russian','')}")


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    user_id = message.from_user.id
    state = get_user_state(user_id)
    if state.stage == 'translation':
        if state.sentence_index < len(state.translation_items):
            item = state.translation_items[state.sentence_index]
            bot.send_message(message.chat.id, f"✅ Correct answer:\n{item.get('english','(no answer provided)')}")
            time.sleep(0.3)
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn_play = types.InlineKeyboardButton("🔊 Play audio", callback_data="play_audio")
            btn_next = types.InlineKeyboardButton("➡️ Next", callback_data="next_translation")
            markup.add(btn_play, btn_next)
            bot.send_message(message.chat.id, "If you want, listen to the correct answer or go to the next sentence.", reply_markup=markup)


def finish_practice(chat_id, user_id):
    reset_user_state(user_id)
    bot.send_message(chat_id,
                     "🎉 Great job!\n\n"
                     "See you tomorrow on your next practice! 👋")


# MAIN: run polling (Render will keep the process alive)
if __name__ == "__main__":
    print("Starting Georgii Practice Bot...")
    bot.infinity_polling(timeout=60, long_polling_timeout=5)
