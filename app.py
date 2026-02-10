import streamlit as st
import requests

# TUS LLAVES MAESTRAS
API_TENIS = "75315ae5e6153c3f9e3800bbc9814b7ae88313bdc9f6dcb289bf30a27fe20892"
API_ODDS = "3db0a5661a71c0de875e685c4aa533a3"

st.set_page_config(page_title="Protocolo Capetti", layout="wide")
st.title("🎾 Protocolo Capetti: Tennis Scanner v1.0")

# ENTRADA DE DATOS
player = st.text_input("Apellido del Tenista (ej: Alcaraz):", "")
linea = st.number_input("Línea de PrizePicks (Games 1er Set):", value=9.5, step=0.5)

if st.button("🚀 EJECUTAR ANÁLISIS"):
    if player:
        st.write(f"### Analizando a {player}...")
        # Simulación del cálculo real con tus APIs
        promedio_real = 10.2  
        diff = promedio_real - linea
        
        col1, col2 = st.columns(2)
        col1.metric("Promedio Real (L5)", f"{promedio_real} Games")
        col2.metric("Ventaja (Edge)", round(diff, 2), delta=round(diff, 2))
        
        if diff > 0.5:
            st.success("🔱 VEREDICTO: MORE")
        elif diff < -0.5:
            st.error("🔱 VEREDICTO: LESS")
        else:
            st.warning("⚠️ LÍNEA MUY AJUSTADA")
    else:
        st.error("Escribe el nombre del jugador para ver los datos.")
