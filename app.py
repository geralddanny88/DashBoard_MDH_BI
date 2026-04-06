import streamlit as st
import streamlit.components.v1 as components

class LoginApp:
    def __init__(self):
        # Credenciales predefinidas
        self.usuario_correcto = "MDH.2026_G"
        self.password_correcto = "Mdh.2026"
        self.iframe_pbi = 'https://app.powerbi.com/view?r=eyJrIjoiOTI0OWE3YWUtYjE0OS00ZDkzLTg4ZjctNTRkMTg3ZDJhMmQ2IiwidCI6Ijc3NzI5YjA5LTRjNjQtNDc4MC1iZmJiLTE3YmFlMGU0Y2RmNyJ9'

    def aplicar_estilo_ios(self):
        """Inyecta CSS para dar un look moderno tipo iOS/Glassmorphism"""
        st.markdown("""
            <style>
            .stApp {
                background-color: #f5f5f7;
            }
            .login-container {
                background: rgba(255, 255, 255, 0.8);
                padding: 2rem;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.3);
                text-align: center;
            }
            div.stButton > button {
                background-color: #007aff;
                color: white;
                border-radius: 12px;
                width: 100%;
                border: none;
                padding: 10px;
                font-weight: bold;
            }
            </style>
        """, unsafe_allow_html=True)

    def mostrar_login(self):
        """Muestra la interfaz de acceso"""
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/561/561127.png", width=80) # Icono decorativo
        st.header("Acceso MDH 2026")
        
        user = st.text_input("ID de Usuario", placeholder="Ingrese su usuario")
        password = st.text_input("Contraseña", type="password", placeholder="••••••••")
        
        if st.button("Iniciar Sesión"):
            if user == self.usuario_correcto and password == self.password_correcto:
                st.session_state['autenticado'] = True
                st.rerun() # Recarga para mostrar el dashboard
            else:
                st.error("Credenciales incorrectas. Intente de nuevo.")
        st.markdown('</div>', unsafe_allow_html=True)

    def mostrar_dashboard(self):
        """Muestra el reporte de Power BI una vez autenticado"""
        st.set_page_config(layout="wide") # Cambia a modo ancho para el reporte
        st.sidebar.success(f"Bienvenido, {self.usuario_correcto}")
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state['autenticado'] = False
            st.rerun()

        st.title("📊 Ejecución MDH - Reporte Oficial")
        components.iframe(self.iframe_pbi, height=850, scrolling=True)

    def ejecutar(self):
        """Controlador principal de la aplicación"""
        self.aplicar_estilo_ios()
        
        # Manejo del estado de la sesión
        if 'autenticado' not in st.session_state:
            st.session_state['autenticado'] = False

        if not st.session_state['autenticado']:
            self.mostrar_login()
        else:
            self.mostrar_dashboard()

# Instanciar y correr la aplicación
if __name__ == "__main__":
    app = LoginApp()
    app.ejecutar()
