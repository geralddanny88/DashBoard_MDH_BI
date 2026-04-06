import streamlit as st
import streamlit.components.v1 as components

# Configuramos la página en modo ancho para que el reporte se vea mejor
st.set_page_config(page_title="Dashboard MDH", layout="wide")

st.title("Visualización de Reporte: Ejecución MDH")

# Extraemos solo el link del src de tu iframe
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiOTI0OWE3YWUtYjE0OS00ZDkzLTg4ZjctNTRkMTg3ZDJhMmQ2IiwidCI6Ijc3NzI5YjA5LTRjNjQtNDc4MC1iZmJiLTE3YmFlMGU0Y2RmNyJ9"

# Renderizamos el reporte
# Nota: He ajustado el height a 800 para una mejor visualización en escritorio
components.iframe(power_bi_url, height=800, scrolling=True)
