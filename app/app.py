import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from voice.voice_assistant import VoiceAssistant
from assistant.groq_chat import GroqChat
from history.ChatHistoryManager import ChatHistoryManager
import streamlit as st

st.title("NAIA")
st.subheader("Your post-surgery assistant")

chat = GroqChat()
voice = VoiceAssistant()
chatHistoryManager = ChatHistoryManager()

#modo = st.radio("How would you like to talk to your recovery assistant?", ["Text", "Voice"])


if "messages" not in st.session_state:
    st.session_state.messages = chatHistoryManager.load()


for msg in st.session_state.messages:
    role = "user" if msg.type == "human" else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)

# Mostrar input de texto y botón de micrófono al mismo tiempo
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.chat_input("Write your message:")
with col2:
    mic_clicked = st.button("🎤", help="Click to speak")

# Si se hizo clic en el botón de micrófono
if mic_clicked:
    user_input = voice.listen()
    st.write(f"You said: {user_input}")

#if modo == "Text":
#    user_input = st.chat_input("Write your message:")
#else:
#    if st.button("Start Speaking"):
#        user_input = voice.listen()
#        st.write(f"You said: {user_input}")
#    else:
#        user_input = None

if user_input:
    st.session_state.messages.append(chat.human_message(user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    response = chat.get_response(st.session_state.messages)
    st.session_state.messages.append(chat.ai_message(response))

    chatHistoryManager.save(st.session_state.messages) 
    
    with st.chat_message("assistant"):
        st.markdown(response)

    #if modo == "Voice":
    if mic_clicked:
        voice.speak(response) 
 
    