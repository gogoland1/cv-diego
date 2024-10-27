import streamlit as st
from datetime import datetime
import qrcode
from PIL import Image
import io

def create_qr_code(url):
    """Crea un código QR de alta resolución"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="#234567", back_color="white")
    qr_image = qr_image.convert('RGB')
    
    img_byte_arr = io.BytesIO()
    qr_image.save(img_byte_arr, format='PNG', quality=100, optimize=False)
    return img_byte_arr.getvalue()

def main():
    # Inicializar contadores en session state
    if 'visits' not in st.session_state:
        st.session_state.visits = 0
    if 'likes' not in st.session_state:
        st.session_state.likes = 0
    if 'section_views' not in st.session_state:
        st.session_state.section_views = {
            'Expediciones': 0,
            'Formación': 0,
            'Habilidades': 0
        }
    
    # Incrementar visitas
    st.session_state.visits += 1

    # Configuración de la página
    st.set_page_config(
        page_title="Diego Hernández-Cerón - Oceanógrafo (Analytics)",
        page_icon="🌊",
        layout="wide"  # Cambiado a wide para mejor visualización
    )

    # Barra lateral con analytics
    with st.sidebar:
        st.title("📊 Analytics en Vivo")
        
        # Métricas principales
        col1, col2 = st.columns(2)
        with col1:
            st.metric("👀 Visitas", st.session_state.visits)
        with col2:
            st.metric("👍 Likes", st.session_state.likes)
        
        st.markdown("---")
        
        # Botón de Like
        if st.button("❤️ Me gusta este CV"):
            st.session_state.likes += 1
            st.balloons()
        
        # Tiempo de visita
        st.write("⏰ Última visita:")
        st.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

    # Contenido principal dividido en dos columnas
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("🌊 Diego Hernández-Cerón")
        st.subheader("Oceanógrafo e Investigador")
        
        # QR Code
        qr_image = create_qr_code("https://cv-diego-8g83wat9eekqxb8vkvgldt.streamlit.app/")
        st.image(qr_image, width=150)
        st.caption("Escanea para ver el CV completo")

    with col2:
        # Analytics detallados
        st.markdown("### 📈 Estadísticas Detalladas")
        
        # Visitas por sección
        if st.button("Ver Expediciones"):
            st.session_state.section_views['Expediciones'] += 1
        if st.button("Ver Formación"):
            st.session_state.section_views['Formación'] += 1
        if st.button("Ver Habilidades"):
            st.session_state.section_views['Habilidades'] += 1
        
        # Mostrar estadísticas por sección
        st.markdown("#### Secciones más visitadas:")
        for section, views in st.session_state.section_views.items():
            st.metric(section, views)

    # Gráficos y estadísticas
    st.markdown("### 📊 Visualización de Datos")
    
    # Gráfico de barras de secciones visitadas
    st.bar_chart(st.session_state.section_views)
    
    # Métricas de engagement
    st.markdown("### 🎯 Métricas de Engagement")
    engage_cols = st.columns(3)
    
    with engage_cols[0]:
        st.metric("Tasa de Likes", f"{(st.session_state.likes/st.session_state.visits*100):.1f}%")
    with engage_cols[1]:
        st.metric("Sección más popular", max(st.session_state.section_views, key=st.session_state.section_views.get))
    with engage_cols[2]:
        st.metric("Total Interacciones", sum(st.session_state.section_views) + st.session_state.likes)

    # Footer
    st.markdown("---")
    st.markdown(
        f"<div style='text-align: center; color: gray; font-size: 0.8em;'>"
        f"Última actualización: {datetime.now().strftime('%B %Y')} | "
        f"Visitas totales: {st.session_state.visits} | "
        f"Likes: {st.session_state.likes}"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
