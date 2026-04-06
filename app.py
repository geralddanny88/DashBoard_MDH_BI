import streamlit as st
import streamlit.components.v1 as components

class LoginApp:
    def __init__(self):
        # Credenciales
        self.usuario_correcto = "MDH.2026_G"
        self.password_correcto = "Mdh.2026"
        self.iframe_pbi = 'https://app.powerbi.com/view?r=eyJrIjoiOTI0OWE3YWUtYjE0OS00ZDkzLTg4ZjctNTRkMTg3ZDJhMmQ2IiwidCI6Ijc3NzI5YjA5LTRjNjQtNDc4MC1iZmJiLTE3YmFlMGU0Y2RmNyJ9'

    def aplicar_estilos_ios(self):
        """Inyecta CSS con paleta Apple Blue/Teal y centrado absoluto"""
        st.markdown("""
            <style>
            /* Fondo Animado Apple (Sin Rosado) */
            @keyframes gradient {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .stApp {
                background: linear-gradient(-45deg, #1c2a38, #2980b9, #23a6d5, #23d5ab);
                background-size: 400% 400%;
                animation: gradient 12s ease infinite;
                height: 100vh;
                width: 100vw;
            }

            /* Forzamos el centrado total del login sin importar el layout de la página */
            .main-login-wrapper {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
            }

            .login-card {
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(30px);
                -webkit-backdrop-filter: blur(30px);
                border-radius: 35px;
                border: 1px solid rgba(255, 255, 255, 0.25);
                padding: 40px 30px;
                width: 340px; /* Ancho fijo para que nunca se estire */
                box-shadow: 0 25px 50px rgba(0,0,0,0.3);
                text-align: center;
                color: white;
            }

            /* Inputs y Botón */
            .stTextInput > div > div > input {
                border-radius: 12px !important;
                background-color: rgba(255, 255, 255, 0.15) !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                color: white !important;
                height: 45px !important;
            }

            div.stButton > button {
                background: white !important;
                color: #000 !important;
                border-radius: 15px !important;
                width: 100%;
                border: none !important;
                height: 48px;
                font-weight: 700;
                margin-top: 15px;
            }

            /* Limpieza de interfaz Streamlit */
            #MainMenu, header, footer {visibility: hidden;}
            </style>
        """, unsafe_allow_html=True)

    def mostrar_login(self):
        """Interfaz de acceso centrada mediante CSS Fixed"""
        # Contenedor que ignora el layout de la página para centrarse
        st.markdown('<div class="main-login-wrapper">', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="login-card">', unsafe_allow_html=True)
            st.markdown("<h1 style='font-size: 2.5rem; margin-bottom: 0;'></h1>", unsafe_allow_html=True)
            st.markdown("<h3 style='font-weight: 400; margin-top: 5px; margin-bottom: 25px;'>MDH Access</h3>", unsafe_allow_html=True)
            
            user = st.text_input("User", placeholder="Usuario", label_visibility="collapsed", key="user_login")
            password = st.text_input("Pass", type="password", placeholder="Contraseña", label_visibility="collapsed", key="pass_login")
            
            if st.button("Iniciar Sesión"):
                if user == self.usuario_correcto and password == self.password_correcto:
                    st.session_state['autenticado'] = True
                    st.rerun()
                else:
                    st.error("Acceso incorrecto")
            
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    def mostrar_dashboard(self):
        """Muestra el reporte de Power BI"""
        # Aquí sí necesitamos el modo ancho
        st.set_page_config(layout="wide", page_title="MDH Dashboard")
        
        with st.sidebar:
            st.markdown("###  MDH 2026")
            st.write(f"Usuario: {self.usuario_correcto}")
            if st.button("Cerrar Sesión"):
                st.session_state['autenticado'] = False
                # Al cerrar sesión, forzamos un reinicio completo
                st.rerun()

        st.title("📊 Ejecución MDH")
        components.iframe(self.iframe_pbi, height=850, scrolling=True)

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
