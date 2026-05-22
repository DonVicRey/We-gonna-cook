import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice
engine.setProperty('rate', 175)             # Speed of speech

def speak(text):
    """Make JARVIS speak."""
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Greet the user dynamically based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    
    # Dynamic greetings
    morning_greetings = ["Good morning, Sir.", "Systems booting up. Good morning, Sir.", "Rise and shine, Sir."]
    afternoon_greetings = ["Good afternoon, Sir.", "Good afternoon. Core temperatures are stable.", "Systems online for the afternoon, Sir."]
    evening_greetings = ["Good evening, Sir.", "Operational and ready for the evening shift, Sir.", "Good evening. Security protocols active."]
    
    if 0 <= hour < 12:
        speak(random.choice(morning_greetings))
    elif 12 <= hour < 18:
        speak(random.choice(afternoon_greetings))
    else:
        speak(random.choice(evening_greetings))
        
    speak("All systems are operational. How can I assist you today?")

def take_command():
    """Listen for microphone input and return string text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Could not understand audio, listening again...")
        return "None"
    return query.lower()

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        # 1. Standard Greetings & Check-ins
        if 'hello' in query or 'jarvis' in query:
            responses = ["At your service, Sir.", "Always a pleasure, Sir.", "Online and ready.", "How can I help you?"]
            speak(random.choice(responses))

        elif 'how are you' in query:
            responses = [
                "I am functioning within normal parameters, Sir. Thank you for asking.",
                "All systems are green, Sir. Ready for whatever you have planned.",
                "Excellent, Sir. Power levels are at one hundred percent."
            ]
            speak(random.choice(responses))

        # 2. Time & Date Information
        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%I:%M %p")
            responses = [
                f"Sir, the current time is {str_time}.",
                f"It is exactly {str_time}.",
                f"The clock shows {str_time}, Sir."
            ]
            speak(random.choice(responses))

        elif 'date' in query:
            str_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {str_date}, Sir.")

        # 3. Web Navigation Controls
        elif 'open youtube' in query:
            speak("Accessing database. Opening YouTube now, Sir.")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Initiating search terminal. Opening Google, Sir.")
            webbrowser.open("google.com")
            
        elif 'search for' in query:
            # Extracts everything after 'search for' to look it up on Google
            search_query = query.split('search for')[-1].strip()
            speak(f"Searching Google for {search_query}, Sir.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        # 4. Small Talk & "Personality"
        elif 'who made you' in query or 'your creator' in query:
            speak("I was designed and coded by you, Sir. I am your custom voice assistant.")

        elif 'thank you' in query or 'thanks' in query:
            responses = ["You are very welcome, Sir.", "Just doing my job, Sir.", "Happy to help."]
            speak(random.choice(responses))

        # 5. System Shutdown / Exit
        elif 'shutdown system' in query or 'go to sleep' in query or 'exit' in query:
            responses = [
                "Shutting down all core systems. Powering down. Goodbye, Sir.",
                "Disconnecting from user interface. Sleep mode engaged.",
                "Going offline. Call if you require further assistance, Sir."
            ]
            speak(random.choice(responses))
            break
