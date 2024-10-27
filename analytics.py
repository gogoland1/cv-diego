import streamlit as st
from datetime import datetime
import qrcode
from PIL import Image
import io
import json
import os

# Función para cargar el contador de visitas
def load_visit_count():
    if 'visit_count' not in st.session_state:
        st.session_state.visit_count = 0
        if os.path.exists('.streamlit/analytics.json'):
            try:
                with open('.streamlit/analytics.json', 'r') as f:
                    data = json.load(f)
                    st.session_state.visit_count = data.get('visits', 0)
            except:
                st.session_state.visit_count = 0
    return st.session_state.visit_count

# Función para guardar el contador de visitas
def save_visit_count():
    if not os.path.exists('.streamlit'):
        os.makedirs('.streamlit')
    try:
        with open('.streamlit/analytics.json', 'w') as f:
            json.dump({'visits': st.session_state.visit_count + 1}, f)
    except:
        pass

# [Mantener la función create_qr_code() igual que antes...]

def main():
    # Incrementar contador de visitas
    visit_count = load_visit_count()
    st.session_state.visit_count += 1
    save_visit_count()

    # Configuración de la página
    st.set_page_config(
        page_title="Diego Hernández-Cerón - Oceanógrafo",
        page_icon="🌊",
        layout="centered"
    )

    # Sidebar con analytics
    with st.sidebar:
        st.title("📊 Analytics")
        st.metric("Visitas Totales", st.session_state.visit_count)
        st.write(f"Última visita: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        # Información para el administrador
        if st.checkbox("Mostrar detalles técnicos"):
            st.write("Información del sistema:")
            st.json({
                "Sistema Operativo": os.name,
                "Python Version": os.sys.version,
                "Streamlit Version": st.__version__
            })

    # [Resto del código del CV igual que antes...]

    # Footer con analytics básicos
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"👀 Visitas: {st.session_state.visit_count}")
    with col2:
        st.markdown(f"📅 Última actualización: {datetime.now().strftime('%B %Y')}")
    with col3:
        if st.button("💫 ¡Me gusta!"):
            if 'likes' not in st.session_state:
                st.session_state.likes = 0
            st.session_state.likes += 1
            st.metric("Likes", st.session_state.likes)

    # Tracker de secciones más visitadas
    if 'section_views' not in st.session_state:
        st.session_state.section_views = {
            'expediciones': 0,
            'habilidades': 0,
            'formacion': 0
        }

    # Analytics detallados (solo visible para ti)
    if st.checkbox("Ver Analytics Detallados", key="show_analytics"):
        st.markdown("### 📊 Analytics Detallados")
        
        # Gráfico de visitas por sección
        st.bar_chart(st.session_state.section_views)
        
        # Métricas adicionales
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Tasa de Interacción", f"{(st.session_state.likes/st.session_state.visit_count*100):.1f}%")
        with col2:
            st.metric("Sección más popular", max(st.session_state.section_views, key=st.session_state.section_views.get))

if __name__ == "__main__":
    main()
