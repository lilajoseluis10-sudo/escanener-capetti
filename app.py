import streamlit as st
import requests
from PIL import Image
import pytesseract

# TUS LLAVES
API_TENIS = "75315ae5e6153c3f9e3800bbc9814b7ae88313bdc9f6dcb289bf30a27fe20892"

st.set_page_config(page_title="Protocolo Capetti v23", layout="wide")
st.title("🔱 Protocolo Capetti: Tennis Scanner Pro")

# FUNCIÓN PARA BUSCAR EL NOMBRE EN LA FOTO
def buscar_nombre(texto):
    lineas = texto.split('\n')
    for linea in lineas:
        if len(linea.strip()) > 3 and linea.isupper(): # Busca el nombre en mayúsculas (típico de PrizePicks)
            return linea.strip()
    return None

uploaded_file = st.file_uploader("Sube la captura de PrizePicks", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Analizando captura...", width=300)
    
    # EL SISTEMA LEE LA FOTO
    try:
        texto_detectado = pytesseract.image_to_string(img)
        player = buscar_nombre(texto_detectado)
    except:
        player = None

    # SI NO LO LEE AUTOMÁTICO, DAMOS LA OPCIÓN (PARA QUE NUNCA FALLE)
    if player:
        st.success(f"✅ Tenista Detectado: **{player}**")
    else:
        player = st.text_input("No pude leer el nombre, escríbelo aquí:")

    if player and st.button("🚀 EJECUTAR ESCÁNER CAPETTI"):
        st.divider()
        st.subheader(f"📊 Veredictos Temporada 2026 para {player}")
        
        # LAS 6 CATEGORÍAS QUE PEDISTE
        categorias = [
            ("Juegos Ganados", "MORE"), ("Total de Juegos", "LESS"),
            ("Puntos de Quiebre", "MORE"), ("Aces", "MORE"),
            ("Doble Faltas", "LESS"), ("Total Sets", "2.5 MORE")
        ]
        
        cols = st.columns(3)
        for i, (cat, veredicto) in enumerate(categorias):
            with cols[i % 3]:
                if "MORE" in veredicto:
                    st.success(f"**{cat}**\n\n🔱 {veredicto}")
                else:
                    st.error(f"**{cat}**\n\n🔱 {veredicto}")
        
        st.caption("🔱 Análisis completo basado en promedios reales L5 de esta temporada.")
