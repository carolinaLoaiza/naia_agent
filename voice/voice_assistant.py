import speech_recognition as sr
from gtts import gTTS
import tempfile
import os


class VoiceAssistant:
    def __init__(self, lang='en'):
        self.recognizer = sr.Recognizer()
        self.lang = lang  # 'en' o 'es' dependiendo del idioma que quieras usar

    def listen(self):
        with sr.Microphone() as source:
            try:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=30)
                return self.recognizer.recognize_google(audio, language="en-GB")
            except:
                return "I'm sorry, I couldn't understand what you said."

    def speak(self, text):
        try:
            tts = gTTS(text=text, lang=self.lang)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                return fp.name  # Devuelve el path al archivo MP3 para reproducir
        except Exception as e:
            print(f"Error generating speech: {e}")
            return None



