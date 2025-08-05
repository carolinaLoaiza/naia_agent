
import streamlit as st
from streamlit_chat import message
import openai

# Clase para manejar el chat con TTS de OpenAI (Whisper)
class WhisperChatApp:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.init_session()

    def init_session(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "voice" not in st.session_state:
            st.session_state.voice = "echo"  # Valor por defecto

    def generate_audio(self, text, voice="echo"):
        response = openai.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text
        )
        return response.content

    def display_chat(self):
        st.title("🗣️ Texto a Voz con Whisper (TTS)")

        st.markdown("Selecciona la voz que prefieres para el audio:")

        voice = st.selectbox(
            "Voz",
            options=["echo", "alloy", "onyx", "nova", "fable", "shimmer"],
            index=["echo", "alloy", "onyx", "nova", "fable", "shimmer"].index(st.session_state.voice),
            key="voice_select"
        )

        st.session_state.voice = voice  # Actualiza la voz seleccionada

        for i, msg in enumerate(st.session_state.messages):
            is_user = (i % 2 == 0)
            message(msg["text"], is_user=is_user)

        user_input = st.chat_input("Escribe el texto que deseas convertir en audio...")

        if user_input:
            st.session_state.messages.append({"text": user_input, "role": "user"})

            audio_bytes = self.generate_audio(user_input, voice=st.session_state.voice)
            st.session_state.messages.append({
                "text": f"Aquí tienes el audio con la voz **{st.session_state.voice}**:",
                "role": "assistant"
            })

            st.audio(audio_bytes, format="audio/mp3")

# Interfaz principal
def main():
    st.set_page_config(page_title="Whisper TTS Chat", page_icon="🔊")

    api_key = st.secrets.get("OPENAI_API_KEY") or st.text_input("Introduce tu API Key de OpenAI", type="password")

    if api_key:
        app = WhisperChatApp(api_key)
        app.display_chat()
    else:
        st.warning("Por favor, introduce tu API Key para continuar.")

if __name__ == "__main__":
    main()
