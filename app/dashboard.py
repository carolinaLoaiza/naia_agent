import streamlit as st

menu = st.sidebar.selectbox("Navegación", ["Historial Médico", "Checklist", "Registro de síntomas", "Subir imagen", "Recordatorios"])

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Historial Médico", "Checklist", "Registro de síntomas", "Subir imagen", "Recordatorios"])

with tab1:
    st.header("🩺 Historial Médico")
    # Código historial médico

with tab2:
    st.header("✅ Checklist de cuidados")
    # Código checklist

with tab3:
    st.header("💬 Registro de síntomas")
    # Código síntomas

with tab4:
    st.header("📷 Subir imagen")
    # Código subir imagen

with tab5:
    st.header("⏰ Recordatorio simulado")
    # Código recordatorios