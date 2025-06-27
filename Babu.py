import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    print("🎙️ Babu:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("🗣️ You said:", command)
    except sr.UnknownValueError:
        talk("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

def run_babu():
    command = take_command()

    if command == "":
        return

    if "exit" in command or "stop" in command or "bye" in command:
        talk("Okay, see you later 👋")
        sys.exit()

    elif "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song} on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "what's the time" in command or "what is the time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif command == "open chrome":
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome not found 😬")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif command.startswith("open "):
        topic = command.replace("open", "").strip()
        if topic:
            url = f"https://www.google.com/search?q={topic}"
            talk(f"Opening {topic} in Chrome 🌐")
            webbrowser.open(url)
        else:
            talk("What should I open?")

    else:
        talk("I heard you, but I don’t understand that yet 😅")

# Start the assistant
talk("Yo! I'm Babu – your voice assistant 💡. Ask me anything.")
while True:
    run_babu()
