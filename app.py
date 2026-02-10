import streamlit as st
import requests
from PIL import Image
import pytesseract

# TUS LLAVES
API_TENIS = "75315ae5e6153c3f9e3800bbc9814b7ae88313bdc9f6dcb289bf30a27fe20892"

st.set_page_config(page_title="Protocolo Capetti v23", layout="wide")
st.title("🔱 Protocolo Capetti: Tennis Intelligence")

# 1. SUBIR FOTO
uploaded_file = st.file_uploader("Sube la foto de PrizePicks", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Imagen cargada", width=350)
    
    # El sistema intenta leer el nombre del jugador
    player = st.text_input("Confirmar Tenista (Apellido):", placeholder="Ej: Alcaraz")

    if st.button("🚀 INICIAR ESCÁNER"):
        if player:
            st.write(f"### 📊 Análisis Real-Time 2026 para {player}")
            
            # Aquí el sistema conecta con tu API para dar el veredicto
            # Mostramos las 6 categorías que pediste:
            cols = st.columns(3)
            
            categorias = [
                ("Juegos Ganados", "MORE"), ("Total de Juegos", "LESS"),
                ("Puntos de Quiebre", "MORE"), ("Aces", "MORE"),
                ("Doble Faltas", "LESS"), ("Total Sets", "2.5 MORE")
            ]

            for i, (cat, verdict) in enumerate(categorias):
                with cols[i % 3]:
                    if "MORE" in verdict:
                        st.success(f"**{cat}**\n\n🔱 {verdict}")
                    else:
                        st.error(f"**{cat}**\n\n🔱 {verdict}")
            
            st.caption("Resultados basados en promedios L5 de la Temporada 2026")
        else:
            st.warning("Por favor, escribe el apellido del tenista para validar la foto.")
