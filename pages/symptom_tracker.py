import os
import json
import streamlit as st
from datetime import datetime
from history.SymptomManager import SymptomManager

st.set_page_config(page_title="My Symptoms", page_icon="💊")

st.title("🩺 My Symptoms")
st.subheader("Here's a summary of your reported symptoms")

# Autenticación
if not st.session_state.get("authentication_status"):
    st.warning("Please log in first.")
    st.stop()

username = st.session_state["username"]
symptom_manager = SymptomManager(user_id=username)

symptoms = symptom_manager.symptoms

if not symptoms:
    st.info("You haven’t reported any symptoms yet.")
    st.stop()

# Mostrar los síntomas en tarjetas simples
for entry in reversed(symptoms[-10:]):  # Solo los últimos 10 para no saturar
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**📝 Symptoms:** {', '.join(entry.get('detected_symptoms', []))}")
            st.markdown(f"**📍 Location:** {entry.get('location', 'Not specified')}")
            st.markdown(f"**📆 Date:** {entry.get('timestamp', 'N/A')[:10]}")
            st.markdown(f"**⏳ Duration:** {entry.get('duration', 'N/A')}")
            st.markdown(f"**⚠️ Severity:** `{entry.get('severity', 'unknown')}`")
        with col2:
            if entry.get("requires_attention"):
                st.error("🚨 Requires Attention")
            else:
                st.success("✅ Stable")
        st.markdown("---")

import streamlit as st
import pandas as pd
import os
import json

from datetime import datetime

# Obtener usuario desde session_state
if not st.session_state.get("authentication_status"):
    st.warning("Please log in first.")
    st.stop()

username = st.session_state["username"]
file_path = f"data/symptoms_{username}.json"

st.set_page_config(page_title="Symptom Tracker", page_icon="🩺", layout="wide")

st.title("🩺 Symptom Tracker")
st.markdown("Monitor your post-surgery symptoms over time.")

# Cargar síntomas
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        symptom_data = json.load(f)
else:
    st.info("No symptom data available.")
    st.stop()

# Mostrar tabla
df = pd.DataFrame(symptom_data)

# Ordenar por fecha (si existe)
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(by="timestamp", ascending=False)

# Mostrar tabla bonita
st.dataframe(
    df[["timestamp", "detected_symptoms", "severity", "duration", "location", "requires_attention"]],
    use_container_width=True,
    hide_index=True
)

# Expansor con mensajes originales
with st.expander("🗣️ View original messages"):
    for entry in df.itertuples():
        st.markdown(f"**🕒 {entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')}**")
        st.markdown(f"**💬 Original Message:** {entry.mensaje_original}")
        st.divider()
