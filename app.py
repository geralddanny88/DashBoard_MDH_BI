import streamlit as st
import streamlit.components.v1 as components

class LoginApp:
    def __init__(self):
        # Credenciales
        self.usuario_correcto = "FABRY"
        self.password_correcto = "12345"
        self.iframe_pbi = 'https://app.powerbi.com/view?r=eyJrIjoiOTI0OWE3YWUtYjE0OS00ZDkzLTg4ZjctNTRkMTg3ZDJhMmQ2IiwidCI6Ijc3NzI5YjA5LTRjNjQtNDc4MC1iZmJiLTE3YmFlMGU0Y2RmNyJ9'

    def aplicar_estilos_ios(self):
        """Inyecta CSS con paleta Apple Blue/Teal y sin scroll"""
        st.markdown("""
            <style>
            /* Fondo Animado Apple (Sin Rosado) */
            @keyframes gradient {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .stApp {
                background: linear-gradient(-45deg, #2c3e50, #2980b9, #23a6d5, #23d5ab);
                background-size: 400% 400%;
                animation: gradient 12s ease infinite;
                height: 100vh;
                overflow: hidden; /* Evita scroll en la página principal */
            }

            /* Contenedor Centrado Vertical y Horizontal */
            .main-login-wrapper {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 100%;
                display: flex;
                justify-content: center;
                z-index: 999;
            }

            .login-card {
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(30px);
                -webkit-backdrop-filter: blur(30px);
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                padding: 30px;
                width: 320px; /* Tamaño compacto tipo iPhone */
                box-shadow: 0 20px 60px rgba(0,0,0,0.2);
                text-align: center;
                color: white;
            }

            /* Inputs Compactos */
            .stTextInput > div > div > input {
                border-radius: 12px !important;
                background-color: rgba(255, 255, 255, 0.15) !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                color: white !important;
                height: 40px !important;
                margin-bottom: -10px;
            }

            /* Botón Apple Style */
            div.stButton > button {
                background: white !important;
                color: #000 !important;
                border-radius: 15px !important;
                width: 100%;
                border: none !important;
                height: 45px;
                font-weight: 700;
                margin-top: 10px;
            }

            /* Ocultar elementos de Streamlit para limpieza total */
            #MainMenu, header, footer {visibility: hidden;}
            .embedded-pbi { border: none; border-radius: 15px; }
            </style>
        """, unsafe_allow_html=True)

    def mostrar_login(self):
        """Interfaz de acceso sin scroll"""
        st.markdown('<div class="main-login-wrapper">', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="login-card">', unsafe_allow_html=True)
            st.markdown("<h2 style='margin-bottom: 5px;'></h2>", unsafe_allow_html=True)
            st.markdown("<h3 style='font-weight: 500; margin-top: 0; margin-bottom: 20px;'>MDH Access</h3>", unsafe_allow_html=True)
            
            # Usamos keys únicas para evitar conflictos de refresco
            user = st.text_input("User", placeholder="Usuario", label_visibility="collapsed", key="u_input")
            password = st.text_input("Pass", type="password", placeholder="Contraseña", label_visibility="collapsed", key="p_input")
            
            if st.button("Sign In"):
                if user == self.usuario_correcto and password == self.password_correcto:
                    st.session_state['autenticado'] = True
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas")
            
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    def mostrar_dashboard(self):
        """Muestra el reporte tras la validación"""
        st.set_page_config(layout="wide", page_title="MDH Dashboard")
        
        with st.sidebar:
            st.markdown("###  MDH 2026")
            st.info(f"Conectado como: {self.usuario_correcto}")
            if st.button("Cerrar Sesión"):
                st.session_state['autenticado'] = False
                st.rerun()

        # Render del Power BI
        components.iframe(self.iframe_pbi, height=800, scrolling=True)

    def ejecutar(self):
        if 'autenticado' not in st.session_state:
            st.session_state['autenticado'] = False

        if not st.session_state['autenticado']:
            self.aplicar_estilos_ios()
            self.mostrar_login()
        else:
            self.mostrar_dashboard()

if __name__ == "__main__":
    app = LoginApp()
    app.ejecutar()
