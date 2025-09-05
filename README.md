# VOICE ASSISTANT

👋
Hello ! we’re going to build a super cool Python project called BABU – Your Personal Voice Assistant

it can:

- 🎤 Voice recognition using Google Speech API
- 🗣️ Text-to-speech responses using pyttsx3
- 🌐 Opens websites or searches (e.g. "Open Nike")
- 🎶 Plays YouTube music (e.g. "Play Shape of You")
- 🕐 Tells current time
- 📚 Answers "Who is..." using Wikipedia
- 🤣 Tells jokes using pyjokes
- 🚀 Opens apps like Chrome and VS Code
- ❌ Exits on command ("exit", "stop", "bye")

Sounds cool? Let’s get started 👇

🛠️ Tools Required:
-Python 3.8 or above
-VS Code (or any editor)
-A microphone
-Internet connection for YouTube/Wikipedia

Step 1: Create Project Folder
Open VS Code → Create a new folder:

mkdir voice-desktop-assistant
cd voice-desktop-assistant

🧪 Step 2: Set Up a Virtual Environment
Run this to create a virtual environment:

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

You’ll see (venv) in your terminal – that means you’re good to go!

Step 3: Install Required Libraries
Run this to install all dependencies:

pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes

Step 4: Create the BABU Script
Create a file Babu.py and paste this full code.

How to Run the Project
After you activate the venv, run:

python Babu.py

Then start talking!

🗣️ Try:

"Play Calm Down"
"Open Nike"
"What's the time"
"Who is Elon Musk"
"Exit"

And BABU will respond like a pro! 🤖


