import streamlit as st
import streamlit.components.v1 as components

class LoginApp:
    def __init__(self):
        # Credenciales
        self.usuario_correcto = "MDH.2026_G"
        self.password_correcto = "Mdh.2026"
        self.iframe_pbi = 'https://app.powerbi.com/view?r=eyJrIjoiOTI0OWE3YWUtYjE0OS00ZDkzLTg4ZjctNTRkMTg3ZDJhMmQ2IiwidCI6Ijc3NzI5YjA5LTRjNjQtNDc4MC1iZmJiLTE3YmFlMGU0Y2RmNyJ9'

    def aplicar_estilos_ios(self):
        """Inyecta CSS para centrar el login y dar estética iOS 26"""
        st.markdown("""
            <style>
            /* Fondo general inspirado en wallpapers de iOS */
            .stApp {
                background: linear-gradient(135deg, #e0e0e7 0%, #ffffff 100%);
            }

            /* Contenedor Centrado y Estrecho */
            .main-login-wrapper {
                display: flex;
                justify-content: center;
                align-items: center;
                padding-top: 50px;
            }

            .login-card {
                background: rgba(255, 255, 255, 0.7);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border-radius: 35px;
                border: 1px solid rgba(255, 255, 255, 0.4);
                padding: 40px;
                width: 100%;
                max-width: 400px; /* Evita que se expanda demasiado */
                box-shadow: 0 20px 40px rgba(0,0,0,0.08);
                text-align: center;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica;
            }

            /* Ajustes de inputs tipo iOS */
            .stTextInput > div > div > input {
                border-radius: 12px !important;
                background-color: rgba(200, 200, 200, 0.1) !important;
                border: none !important;
                padding: 12px !important;
            }

            /* Botón Azul Apple */
            div.stButton > button {
                background-color: #007AFF !important;
                color: white !important;
                border-radius: 14px !important;
                width: 100%;
                border: none !important;
                height: 45px;
                font-weight: 600;
                transition: all 0.3s ease;
            }

            div.stButton > button:hover {
                background-color: #0056b3 !important;
                transform: scale(1.02);
            }
            
            /* Ocultar elementos innecesarios de Streamlit en el login */
            header, footer {visibility: hidden;}
            </style>
        """, unsafe_allow_html=True)

    def mostrar_login(self):
        """Interfaz de acceso centrada"""
        # Usamos columnas de Streamlit para ayudar al centrado vertical/horizontal
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown('<div class="main-login-wrapper">', unsafe_allow_html=True)
            st.markdown('<div class="login-card">', unsafe_allow_html=True)
            
            # Icono de candado o FaceID style
            st.markdown("### ") 
            st.title("Inicia sesión")
            st.caption("Introduce tus credenciales para acceder al reporte de ejecución.")
            
            user = st.text_input("Usuario", placeholder="nombre@ejemplo.com", label_visibility="collapsed")
            password = st.text_input("Contraseña", type="password", placeholder="Contraseña", label_visibility="collapsed")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("Continuar"):
                if user == self.usuario_correcto and password == self.password_correcto:
                    st.session_state['autenticado'] = True
                    st.rerun()
                else:
                    st.error("Acceso denegado")
            
            st.markdown('</div></div>', unsafe_allow_html=True)

    def mostrar_dashboard(self):
        """Dashboard a pantalla completa tras el login"""
        st.set_page_config(layout="wide", page_title="MDH Dashboard")
        
        # Barra lateral minimalista para cerrar sesión
        with st.sidebar:
            st.title("MDH 2026")
            st.write(f"Sesión: {self.usuario_correcto}")
            if st.button("Cerrar Sesión"):
                st.session_state['autenticado'] = False
                st.rerun()

        # Reporte
        components.iframe(self.iframe_pbi, height=900, scrolling=True)

    def ejecutar(self):
        # Inicializar estado
        if 'autenticado' not in st.session_state:
            st.session_state['autenticado'] = False

        if not st.session_state['autenticado']:
            # En el login no usamos wide mode para que se vea centrado
            self.aplicar_estilos_ios()
            self.mostrar_login()
        else:
            self.mostrar_dashboard()

if __name__ == "__main__":
    app = LoginApp()
    app.ejecutar()
