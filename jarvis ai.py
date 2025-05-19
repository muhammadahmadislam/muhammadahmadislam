import speech_recognition as sr
import wikipedia
import pyttsx3
import datetime
import webbrowser
import random

# Optional: real ChatGPT access (if needed)
# import openai
# openai.api_key = "your_openai_api_key"

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)

def speak(text):
    print(f"Ahmad: {text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Yo! Good morning, bro!")
    elif 12 <= hour < 18:
        speak("Hey! Good afternoon, dude!")
    else:
        speak("Sup! Good evening, my guy!")
    speak("I'm Ahmad 😎, and my big bro is Asar. What can I do for ya today?")

def take_command():
    recognizer = sr.Recognizer()
    mic_index = 1  # 👈 Set your microphone index

    with sr.Microphone(device_index=mic_index) as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
        return query.lower()
    except Exception:
        speak("Yo, I didn't catch that. Say it again?")
        return ""

def ask_chatgpt(prompt):
    # 🔹 Simulated ChatGPT response (for offline use)
    responses = [
        "That's deep, bro. I'd say just go for it.",
        "Well, honestly, that depends on the situation.",
        "I think your best move is to chill and think it through.",
        "Haha, good one! But I ain't got all the answers, bro 😅",
        "Big brain stuff! Even ChatGPT would be impressed."
    ]
    return random.choice(responses)

    # 🔹 Uncomment below for real ChatGPT response if you have OpenAI API
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=prompt,
    #     max_tokens=100
    # )
    # return response['choices'][0]['text'].strip()

def run_assistant():
    greet_user()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak("Let me pull that from Wikipedia...")
            topic = query.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak("Here's what I found, bro:")
                speak(result)
            except:
                speak("Couldn't find anything solid on that one.")

        # --- Social Media ---
        elif 'open youtube' in query:
            speak("Opening YouTube, bro 🎬")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Heading to Google 🌐")
            webbrowser.open("https://www.google.com")

        elif 'open facebook' in query:
            speak("Facebook coming right up 👍")
            webbrowser.open("https://www.facebook.com")

        elif 'open instagram' in query:
            speak("Let’s hit Instagram 📸")
            webbrowser.open("https://www.instagram.com")

        elif 'open twitter' in query or 'open x' in query:
            speak("Twitter is on its way 🐦")
            webbrowser.open("https://www.twitter.com")

        elif 'open whatsapp' in query:
            speak("Opening WhatsApp Web 💬")
            webbrowser.open("https://web.whatsapp.com")

        elif 'open tiktok' in query:
            speak("Here comes TikTok 🎵")
            webbrowser.open("https://www.tiktok.com")

        elif 'open snapchat' in query:
            speak("Snapchat is loading 👻")
            webbrowser.open("https://www.snapchat.com")

        elif 'open linkedin' in query:
            speak("Going pro! LinkedIn it is 🔗")
            webbrowser.open("https://www.linkedin.com")

        # --- Time ---
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"It's {current_time}, my dude!")

        # --- ChatGPT Section ---
        elif 'ask chatgpt' in query or 'talk to chatgpt' in query:
            speak("Alright bro, shoot your question for ChatGPT.")
            prompt = take_command()
            if prompt:
                answer = ask_chatgpt(prompt)
                speak("Here's what ChatGPT says:")
                speak(answer)

        # --- Exit ---
        elif 'exit' in query or 'bye' in query:
            speak("Peace out, from me and my big bro Asar! ✌️")
            break

        # --- Default Response ---
        elif query:
            speak("Not sure I got that, try again bro.")

if __name__ == "__main__":
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Mic {index}: {name}")

    run_assistant()
