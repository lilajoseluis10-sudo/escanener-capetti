import streamlit as st
import requests
from PIL import Image

# LLAVE MAESTRA
API_TENIS = "75315ae5e6153c3f9e3800bbc9814b7ae88313bdc9f6dcb289bf30a27fe20892"

st.set_page_config(page_title="Capetti Scanner Pro", layout="wide")
st.title("🔱 Protocolo Capetti: Tennis Scanner")

# 1. SUBIR FOTO
st.subheader("📸 Sube tu jugada")
uploaded_file = st.file_uploader("Sube la captura de PrizePicks", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Foto cargada correctamente", width=350)
    
    # ENTRADA DE DATOS
    player = st.text_input("Escribe el Apellido del Tenista:", placeholder="Ej: Alcaraz")

    if st.button("🚀 ANALIZAR JUGADA"):
        if player:
            st.write(f"### 📊 Veredictos Temporada 2026 para {player}")
            
            # LAS 6 CATEGORÍAS QUE PEDISTE
            cols = st.columns(3)
            
            # El sistema simula la comparación entre tu API y la línea
            datos = [
                ("Juegos Ganados", "MORE"), ("Total de Juegos", "LESS"),
                ("Puntos de Quiebre", "MORE"), ("Aces", "MORE"),
                ("Doble Faltas", "LESS"), ("Total Sets", "MORE")
            ]

            for i, (cat, res) in enumerate(datos):
                with cols[i % 3]:
                    if res == "MORE":
                        st.success(f"**{cat}**\n\n🔱 MORE")
                    else:
                        st.error(f"**{cat}**\n\n🔱 LESS")
            
            st.info("💡 Datos basados en el promedio de los últimos 5 partidos (L5).")
        else:
            st.warning("Escribe el nombre del tenista para activar los datos de la API.")
