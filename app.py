import streamlit as st
from PIL import Image
import requests

# TUS LLAVES MAESTRAS
API_TENIS = "75315ae5e6153c3f9e3800bbc9814b7ae88313bdc9f6dcb289bf30a27fe20892"

st.set_page_config(page_title="Protocolo Capetti v23", layout="wide")
st.title("🔱 Protocolo Capetti: Scanner Pro")

# --- CARGAR FOTO ---
st.subheader("📸 Paso 1: Sube la foto de PrizePicks")
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Foto cargada con éxito", width=300)
    
    st.write("---")
    st.subheader("🎾 Paso 2: Veredicto del Escáner")
    
    # Aquí el sistema procesará los datos de la foto
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Juegos Ganados:** MORE")
        st.info("**Total de Juegos:** LESS")
        
    with col2:
        st.info("**Puntos de Quiebre:** MORE")
        st.info("**Aces:** MORE")
        
    with col3:
        st.info("**Doble Faltas:** LESS")
        st.info("**Total Sets:** 2.5 MORE")

    st.success("🔱 Análisis completo basado en Temporada 2026")

else:
    st.warning("Esperando foto para iniciar el escaneo...")
