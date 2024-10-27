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
    # Configuración de la página
    st.set_page_config(
        page_title="Analytics CV Diego",
        page_icon="📊",
        layout="wide"
    )

    # Inicializar variables en session state
    if 'visits' not in st.session_state:
        st.session_state.visits = 0
    if 'likes' not in st.session_state:
        st.session_state.likes = 0
    if 'expediciones' not in st.session_state:
        st.session_state.expediciones = 0
    if 'formacion' not in st.session_state:
        st.session_state.formacion = 0
    if 'habilidades' not in st.session_state:
        st.session_state.habilidades = 0

    # Incrementar visitas
    st.session_state.visits += 1

    # Sidebar con métricas principales
    with st.sidebar:
        st.title("📊 Analytics en Vivo")
        st.metric("👀 Visitas", st.session_state.visits)
        st.metric("👍 Likes", st.session_state.likes)
        
        if st.button("❤️ Me gusta este CV"):
            st.session_state.likes += 1
            st.balloons()
        
        st.markdown("---")
        st.write("⏰ Última visita:")
        st.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

    # Contenido principal
    st.title("Analytics del Curriculum")
    
    # Secciones visitadas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📚 Ver Expediciones"):
            st.session_state.expediciones += 1
        st.metric("Expediciones", st.session_state.expediciones)
        
    with col2:
        if st.button("🎓 Ver Formación"):
            st.session_state.formacion += 1
        st.metric("Formación", st.session_state.formacion)
        
    with col3:
        if st.button("💻 Ver Habilidades"):
            st.session_state.habilidades += 1
        st.metric("Habilidades", st.session_state.habilidades)

    # Visualización de datos
    st.markdown("### 📊 Visualización de Datos")
    data = {
        'Expediciones': st.session_state.expediciones,
        'Formación': st.session_state.formacion,
        'Habilidades': st.session_state.habilidades
    }
    st.bar_chart(data)

    # Métricas de engagement
    st.markdown("### 🎯 Métricas de Engagement")
    eng_col1, eng_col2 = st.columns(2)
    
    with eng_col1:
        if st.session_state.visits > 0:
            tasa_likes = (st.session_state.likes / st.session_state.visits) * 100
        else:
            tasa_likes = 0
        st.metric("Tasa de Likes", f"{tasa_likes:.1f}%")
        
    with eng_col2:
        total_interacciones = (st.session_state.expediciones + 
                             st.session_state.formacion + 
                             st.session_state.habilidades + 
                             st.session_state.likes)
        st.metric("Total Interacciones", total_interacciones)

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        f"Última actualización: {datetime.now().strftime('%B %Y')} | "
        f"Visitas totales: {st.session_state.visits}"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
