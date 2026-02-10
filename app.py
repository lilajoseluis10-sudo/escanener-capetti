import streamlit as st
import requests

# Configuración de tus llaves
API_TENIS = "75315ae5e6153c3f9e3800bbc9814b7ae88313bdc9f6dcb289bf30a27fe20892"
API_ODDS = "3db0a5661a71c0de875e685c4aa533a3"

st.title("🎾 Escáner Capetti v1.0")

player = st.text_input("Apellido del jugador:", "Alcaraz")

if st.button("Escanear"):
    st.write(f"Buscando a {player} en PrizePicks...")
    # El servidor hará el resto automáticamente
