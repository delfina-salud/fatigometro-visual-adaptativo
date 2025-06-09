# Fatigómetro Visual Adaptativo

Asistente visual para la prevención del burnout en entornos sanitarios.

Este sistema analiza señales faciales captadas desde la cámara (como parpadeo, postura, expresión) y genera una pauta de autocuidado adaptada usando inteligencia artificial (GPT-4).

## Fundamento científico del Fatigómetro
El Fatigómetro Visual Adaptativo es una herramienta open source para la detección temprana de fatiga en profesionales sanitarios. Utiliza visión por computadora y GPT-4 para generar pautas de intervención personalizadas.

El modelo combina biomarcadores visuales (parpadeo, postura, expresividad) con indicadores emocionales autorreportados o inferidos por IA, generando un Índice de Fatiga Funcional (IFF) de 0 a 6 puntos.

Este índice se inspira en escalas clínicas validadas como:

FAS (Fatigue Assessment Scale)

KSS (Karolinska Sleepiness Scale)

OFER-15 (Occupational Fatigue Exhaustion/Recovery)

MBI-HSS (Maslach Burnout Inventory)

Cada nivel de fatiga activa un protocolo de intervención adaptativa, empática y profesional, con el objetivo de prevenir el burnout antes de que se cronifique.

## Tecnologías utilizadas

- Streamlit
- MediaPipe (en desarrollo)
- OpenAI API (GPT-4)
- Python 3.10+

## Cómo usar

1. Cloná el repositorio o descargá el ZIP
2. Instalá dependencias con `pip install -r requirements.txt`
3. Ejecutá `streamlit run app.py`

## Licencia

MIT License — Libre para usar, mejorar y compartir con atribución.
