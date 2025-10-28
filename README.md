# VOICE ASSISTANT
# 🎙️ BABU – Your Personal Voice Assistant

> 🤖 Meet **BABU**, a smart and friendly **Python Voice Assistant** built with love — capable of recognizing your voice, speaking naturally, playing songs, answering questions, telling jokes, and opening your favorite apps or websites!

---

##  Features

✨ **Voice Recognition** — Understands your voice using Google Speech API  
🗣️ **Text-to-Speech (TTS)** — Speaks back naturally using `pyttsx3`  
🌐 **Web Access** — Opens websites or searches with commands like “Open Nike”  
🎶 **YouTube Integration** — Plays songs directly using `pywhatkit`  
🕒 **Tells Current Time** — Gives the real-time clock update  
📚 **Wikipedia Answers** — Responds to “Who is…” questions  
🤣 **Jokes** — Tells random jokes to lighten your mood  
⚙️ **App Control** — Opens local apps like Chrome or VS Code  
❌ **Exit Command** — Shuts down gracefully on “exit”, “stop”, or “bye”

---

##  Requirements

- 🐍 Python **3.8 or above**
- 💻 A code editor (VS Code recommended)
- 🎤 A working microphone
- 🌐 Internet connection (for YouTube and Wikipedia)

---

## ⚙️ Setup Instructions

Follow these simple steps to run **BABU** locally:

```bash
# STEP:1 Create project folder
mkdir voice-desktop-assistant
cd voice-desktop-assistant

# STEP:2 Create and activate virtual environment
python -m venv venv

# For Windows
venv\Scripts\activate

# For macOS/Linux
source venv/bin/activate

# STEP:3 Install all dependencies
pip install -r requirements.txt

# STEP:4 Create the main script
# Create a file named Babu.py and paste the code from this repository

# STEP:5 Run the assistant
python Babu.py
