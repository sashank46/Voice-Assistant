# 🎙️ BABU – Your Personal Voice Assistant

> 🤖 Meet **BABU**, your own friendly Python Voice Assistant — smart enough to listen, talk, play music, tell jokes, and open your favorite apps or websites, all with your voice!

---

## 🚀 Features

✨ **Voice Recognition** – Listens using Google Speech API  
🗣️ **Text-to-Speech** – Talks back using `pyttsx3`  
🌐 **Web Browsing** – Opens or searches websites  
🎶 **YouTube Music** – Plays songs via `pywhatkit`  
🕒 **Time Telling** – Speaks current time  
📚 **Wikipedia Info** – Answers “Who is…” queries  
🤣 **Jokes** – Tells random jokes using `pyjokes`  
⚙️ **App Launcher** – Opens Chrome or VS Code  
❌ **Exit Command** – Stops when you say *exit*, *stop*, or *bye*

---

## 🧰 Requirements

- 🐍 Python 3.8 or higher  
- 💻 Code editor (VS Code recommended)  
- 🎤 Working microphone  
- 🌐 Internet connection (for YouTube & Wikipedia)

---

## ⚙️ Setup Instructions

Follow these steps carefully 👇  

---

### 🪄 **Step 1: Create Project Folder**

```bash
mkdir voice-desktop-assistant
cd voice-desktop-assistant
```
### **Step 2: Create and Activate Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate

```

### **Step 3: Install All Dependencies**
```bash
SpeechRecognition
pyttsx3
pywhatkit
wikipedia
pyjokes
```
```bash
pip install -r requirements.txt
```
### **Step 4: Create the Main Script**
```bash
Create a file named Babu.py inside your folder and paste the assistant code from this repository.
Make sure your microphone and internet are active before running it!
```
### **Step 5: Run the Assistant**
```bash
python Babu.py
```

