import streamlit as st
import streamlit.components.v1 as components

class LoginApp:
    def __init__(self):
        self.usuario_correcto = "MDH.2026_G"
        self.password_correcto = "Mdh.2026"
        self.iframe_pbi = 'https://app.powerbi.com/view?r=eyJrIjoiOTI0OWE3YWUtYjE0OS00ZDkzLTg4ZjctNTRkMTg3ZDJhMmQ2IiwidCI6Ijc3NzI5YjA5LTRjNjQtNDc4MC1iZmJiLTE3YmFlMGU0Y2RmNyJ9'

    def aplicar_estilos_ios(self):
        """Inyecta CSS con gradiente animado de Apple y login centrado"""
        st.markdown("""
            <style>
            /* Fondo Animado con Paleta de Colores Apple (iOS Dynamic Wallpaper) */
            @keyframes gradient {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .stApp {
                background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
                background-size: 400% 400%;
                animation: gradient 15s ease infinite;
                height: 100vh;
            }

            /* Contenedor de la Tarjeta de Login */
            .main-login-wrapper {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 80vh;
            }

            .login-card {
                background: rgba(255, 255, 255, 0.25); /* Ultra Glassmorphism */
                backdrop-filter: blur(25px);
                -webkit-backdrop-filter: blur(25px);
                border-radius: 40px;
                border: 1px solid rgba(255, 255, 255, 0.3);
                padding: 50px 40px;
                width: 100%;
                max-width: 380px;
                box-shadow: 0 25px 50px rgba(0,0,0,0.15);
                text-align: center;
                color: white; /* Texto blanco para resaltar sobre el fondo colorido */
            }

            /* Estilo de los Inputs */
            .stTextInput > div > div > input {
                border-radius: 15px !important;
                background-color: rgba(255, 255, 255, 0.2) !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                color: white !important;
                height: 45px;
            }
            
            .stTextInput > div > div > input::placeholder {
                color: rgba(255, 255, 255, 0.6) !important;
            }

            /* Botón de Acción Principal */
            div.stButton > button {
                background: white !important;
                color: #000 !important;
                border-radius: 18px !important;
                width: 100%;
                border: none !important;
                height: 50px;
                font-weight: 700;
                margin-top: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }

            div.stButton > button:hover {
                transform: scale(1.03);
                background-color: rgba(255,255,255,0.9) !important;
            }

            /* Ocultar elementos de Streamlit */
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
        """, unsafe_allow_html=True)

    def mostrar_login(self):
        # Usamos un contenedor vacío para forzar el estilo centrado
        st.markdown('<div class="main-login-wrapper">', unsafe_allow_html=True)
        
        # Estructura del Login
        with st.container():
            col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
            with col2:
                st.markdown('<div class="login-card">', unsafe_allow_html=True)
                st.markdown("<h1 style='font-size: 3rem; margin-bottom: 0;'></h1>", unsafe_allow_html=True)
                st.markdown("<h2 style='font-weight: 600; margin-top: 0;'>MDH 2026</h2>", unsafe_allow_html=True)
                st.markdown("<p style='font-size: 0.9rem; opacity: 0.8;'>Ingresa tus credenciales</p>", unsafe_allow_html=True)
                
                user = st.text_input("User", placeholder="Usuario", label_visibility="collapsed")
                password = st.text_input("Pass", type="password", placeholder="Contraseña", label_visibility="collapsed")
                
                if st.button("Entrar"):
                    if user == self.usuario_correcto and password == self.password_correcto:
                        st.session_state['autenticado'] = True
                        st.rerun()
                    else:
                        st.error("Credenciales no válidas")
                
                st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    def mostrar_dashboard(self):
        st.set_page_config(layout="wide", page_title="Dashboard Ejecutivo MDH")
        
        with st.sidebar:
            st.markdown("###  Menú")
            st.write(f"Usuario: **{self.usuario_correcto}**")
            if st.button("Cerrar Sesión"):
                st.session_state['autenticado'] = False
                st.rerun()

        # El iframe de Power BI
        components.iframe(self.iframe_pbi, height=900, scrolling=True)

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
