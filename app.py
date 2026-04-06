import streamlit as st
import streamlit.components.v1 as components

# 1. ESTO DEBE IR PRIMERO QUE NADA
st.set_page_config(layout="wide", page_title="MDH Dashboard", initial_sidebar_state="collapsed")

class LoginApp:
    def __init__(self):
        self.usuario_correcto = "MDH.2026_G"
        self.password_correcto = "Mdh.2026"
        self.iframe_pbi = 'https://app.powerbi.com/view?r=eyJrIjoiOTI0OWE3YWUtYjE0OS00ZDkzLTg4ZjctNTRkMTg3ZDJhMmQ2IiwidCI6Ijc3NzI5YjA5LTRjNjQtNDc4MC1iZmJiLTE3YmFlMGU0Y2RmNyJ9'

    def aplicar_estilos_ios(self):
        st.markdown("""
            <style>
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
            }
            /* Centrado forzado del login */
            .main-login-wrapper {
                position: fixed;
                top: 0; left: 0;
                width: 100vw; height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
                background: inherit;
            }
            .login-card {
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(30px);
                -webkit-backdrop-filter: blur(30px);
                border-radius: 35px;
                border: 1px solid rgba(255, 255, 255, 0.25);
                padding: 40px;
                width: 350px;
                box-shadow: 0 25px 50px rgba(0,0,0,0.3);
                text-align: center;
                color: white;
            }
            .stTextInput > div > div > input {
                border-radius: 12px !important;
                background-color: rgba(255, 255, 255, 0.15) !important;
                color: white !important;
            }
            div.stButton > button {
                background: white !important;
                color: #000 !important;
                border-radius: 15px !important;
                width: 100%;
                font-weight: 700;
                height: 45px;
            }
            #MainMenu, header, footer {visibility: hidden;}
            </style>
        """, unsafe_allow_html=True)

    def mostrar_login(self):
        st.markdown('<div class="main-login-wrapper">', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="login-card">', unsafe_allow_html=True)
            st.markdown("<h1></h1><h3>MDH Access</h3>", unsafe_allow_html=True)
            
            # Usar on_change o botones simples para evitar bloqueos
            user = st.text_input("User", placeholder="Usuario", label_visibility="collapsed", key="u_field")
            password = st.text_input("Pass", type="password", placeholder="Contraseña", label_visibility="collapsed", key="p_field")
            
            if st.button("Entrar", key="btn_login"):
                if user == self.usuario_correcto and password == self.password_correcto:
                    st.session_state['autenticado'] = True
                    st.rerun()
                else:
                    st.error("Datos incorrectos")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    def mostrar_dashboard(self):
        with st.sidebar:
            st.markdown("###  Menú")
            if st.button("Cerrar Sesión"):
                st.session_state['autenticado'] = False
                st.rerun()
        
        st.title("📊 Reporte de Ejecución")
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
