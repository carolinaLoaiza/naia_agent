
import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from voice.voice_assistant import VoiceAssistant
from assistant.groq_chat import GroqChat
from history.ChatHistoryManager import ChatHistoryManager
from history.SymptomManager import SymptomManager
from datetime import datetime
import streamlit as st
from history.EmergencyMonitor import EmergencyMonitor

if not st.session_state.get("authentication_status"):
    st.warning("Please log in first.")
    st.stop()

username = st.session_state["username"]




st.set_page_config(
    page_title="GPT Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"  # o "collapsed"
)


st.title("NAIA")
st.subheader("Your post-surgery assistant")

groqChat = GroqChat()
voice = VoiceAssistant()
#chatHistoryManager = ChatHistoryManager()
chatHistoryManager = ChatHistoryManager(user_id=username)
symptom_manager = SymptomManager(user_id=username)
emergency_monitor = EmergencyMonitor()

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


if user_input:
    st.session_state.messages.append(groqChat.human_message(user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    response = groqChat.get_response(st.session_state.messages)
    st.session_state.messages.append(groqChat.ai_message(response))

    chatHistoryManager.save(st.session_state.messages) 
  
    symptom_data = groqChat.extract_symptoms(user_input)
    # Validar que sea un diccionario
    if isinstance(symptom_data, list) and symptom_data:
        symptom_data = symptom_data[0]
    elif not isinstance(symptom_data, dict):
        symptom_data = None  # O manejar error

    if symptom_data:
        symptom_data["mensaje_original"] = user_input
        symptom_data["timestamp"] = datetime.now().isoformat()
        symptom_data["user_id"] = username  
        symptom_manager.add_entry(symptom_data)

     # Check for emergency
    #if emergency_monitor.check_and_handle(symptom_data):
    #    st.error("🚨 Your symptoms may be severe. Please seek emergency care immediately.")    

    with st.chat_message("assistant"):
        st.markdown(response)

    #if modo == "Voice":
    if mic_clicked:
        voice.speak(response) 

