import streamlit as st
from utils.face_analysis import detectar_nivel_fatiga
from openai_prompt.generador_pauta import generar_pauta

st.set_page_config(page_title="Fatigómetro Visual Adaptativo")
st.title("🧠 Fatigómetro Visual Adaptativo")

st.markdown("""
Este sistema analiza tu rostro para detectar signos visibles de fatiga y, en base a eso, genera una pauta breve de autocuidado con ayuda de inteligencia artificial.

**Paso 1:** Activá tu cámara (en desarrollo).  
**Paso 2:** El sistema estima tu nivel de fatiga según parpadeo, postura y expresión.  
**Paso 3:** Recibís una sugerencia de cuidado adaptada a tu estado actual.
""")

# Simulación de entrada (hasta tener captura real)
nivel_simulado = st.slider("Simulador de nivel de fatiga (0 = alerta, 3 = muy alta)", 0, 3, 1)

if st.button("Evaluar y recibir pauta"):
    pauta = generar_pauta(nivel_simulado)
    st.success("Tu pauta de hoy:")
    st.markdown(f"**{pauta}**")