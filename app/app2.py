import streamlit as st

st.title("Voice input test")

if "voice_text" not in st.session_state:
    st.session_state.voice_text = ""

# Mostrar el texto capturado por voz
st.write("Voice input:", st.session_state.voice_text)

# Campo de texto normal para fallback
text_input = st.text_input("Or type here:")

if text_input:
    st.write("You typed:", text_input)

# Componente HTML con JS para capturar voz
st.components.v1.html(
    """
    <button onclick="startRecognition()">🎤 Speak</button>
    <script>
    function startRecognition() {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'en-GB';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            // Mandar el texto a Streamlit usando window.parent.postMessage
            window.parent.postMessage({type: 'VOICE_INPUT', text: transcript}, '*');
        };

        recognition.start();
    }
    </script>
    """,
    height=100,
)

# Capturamos el mensaje enviado por JS desde el iframe
from streamlit_js_eval import streamlit_js_eval

voice_message = streamlit_js_eval(
    js_expressions="""
        (() => {
            return new Promise((resolve, reject) => {
                window.addEventListener('message', event => {
                    if (event.data.type === 'VOICE_INPUT') {
                        resolve(event.data.text);
                    }
                });
            });
        })();
    """,
    key="voice_eval"
)

if voice_message:
    st.session_state.voice_text = voice_message
