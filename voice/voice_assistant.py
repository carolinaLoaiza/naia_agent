import speech_recognition as sr
import pyttsx3
import threading

class VoiceAssistant:
    def __init__(self, voice_index=1, rate=140, volume=0.9):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')  
        if voice_index < len(voices):
            self.engine.setProperty('voice', voices[voice_index].id)
        else:
            print(f"Voice index {voice_index} is out of range. Using default voice.")
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)   
        self.recognizer = sr.Recognizer()

   
    def listen(self):
        with sr.Microphone() as source:
            try:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=10)
                return self.recognizer.recognize_google(audio, language="en-GB")
            except:
                return "I'm sorry, I couldn't understand what you said."
    


    def speak(self, text):
        try:
            # Crear una nueva instancia del motor cada vez
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(f"Error during speech synthesis: {e}")