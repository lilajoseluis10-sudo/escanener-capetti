import streamlit as st
import requests
import os

# ==============================
# CONFIG API KEYS (ENV)
# ==============================
ODDS_API_KEY = os.getenv("ODDS_API_KEY")
TENNIS_API_KEY = os.getenv("TENNIS_API_KEY")

# ==============================
# GET PLAYER STATS
# ==============================
def get_player_stats(player):

    try:
        url = f"https://api-tennis.com/stats?player={player}&key={TENNIS_API_KEY}"
        r = requests.get(url)
        data = r.json()

        return {
            "serve": data.get("serve_points_won", 60),
            "return": data.get("return_points_won", 40),
            "break": data.get("break_points_won", 50),
            "form": data.get("last5_form", 50),
            "surface": data.get("surface_win", 50),
            "fatigue": data.get("matches_last7", 2),
            "momentum": data.get("momentum", 50),
            "h2h_style": data.get("style_vs_opponent", 50)
        }

    except:
        st.error("Error leyendo datos del jugador")
        return None


# ==============================
# REAL POWER MODEL
# ==============================
def real_power(stats):

    power = (
        stats["serve"] * 0.18 +
        stats["return"] * 0.18 +
        stats["break"] * 0.12 +
        stats["form"] * 0.14 +
        stats["surface"] * 0.10 -
        stats["fatigue"] * 0.08 +
        stats["h2h_style"] * 0.08 +
        stats["momentum"] * 0.12
    )

    return power


# ==============================
# STREAMLIT UI
# ==============================
st.set_page_config(page_title="Tennis Scanner Pro", layout="centered")

st.title("🎾 TENNIS SCANNER PRO")

player1 = st.text_input("Jugador 1")
player2 = st.text_input("Jugador 2")

market_prob1 = st.slider("Probabilidad Mercado Jugador 1 (%)", 1, 99, 55)
market_prob2 = 100 - market_prob1

if st.button("ESCANEAR MATCH"):

    if not player1 or not player2:
        st.warning("Ingresa ambos jugadores")
        st.stop()

    stats1 = get_player_stats(player1)
    stats2 = get_player_stats(player2)

    if stats1 and stats2:

        power1 = real_power(stats1)
        power2 = real_power(stats2)

        total = power1 + power2

        prob1 = (power1 / total) * 100
        prob2 = (power2 / total) * 100

        st.subheader("📊 RESULTADO")

        st.write(f"**{player1} → {round(prob1,2)}%**")
        st.write(f"**{player2} → {round(prob2,2)}%**")

        if prob1 > prob2:
            favorito = player1
            confianza = prob1 - prob2
        else:
            favorito = player2
            confianza = prob2 - prob1

        st.success(f"📈 Favorito real: {favorito}")
        st.write(f"🔥 Confianza: {round(confianza,2)}%")

        if confianza > 14:
            st.write("💎 PICK FUERTE")
        elif confianza > 7:
            st.write("⚡ PICK MEDIO")
        else:
            st.write("⚠️ MATCH PELIGROSO")
