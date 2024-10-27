import streamlit as st
from datetime import datetime
import qrcode
from PIL import Image
import io

def create_qr_code(url):
    """Crea un código QR con estilo personalizado"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear QR con colores personalizados
    qr_image = qr.make_image(fill_color="#234567", back_color="white")
    
    # Convertir a bytes para mostrar en Streamlit
    img_byte_arr = io.BytesIO()
    qr_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return img_byte_arr

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Diego Hernández-Cerón - Oceanógrafo",
        page_icon="🌊",
        layout="centered"
    )

    # URL de tu CV online
    cv_url = "https://cv-diego-8g83wat9eekqxb8vkvgldt.streamlit.app/"

    # Crear dos columnas para el encabezado
    col1, col2 = st.columns([3, 1])

    with col1:
        # Encabezado
        st.title("🌊 Diego Hernández-Cerón")
        st.subheader("Oceanógrafo e Investigador")

    with col2:
        # Generar y mostrar QR
        qr_image = create_qr_code(cv_url)
        st.image(qr_image, width=150)
        st.caption("Escanea para compartir")

    # Información de Contacto
    st.markdown("### 📬 Contacto")
    st.write("📧 diego.jhc@gmail.com")
    st.write("📱 +569 32104924")
    st.write("📍 Quilpué, Chile")

    # Formación Académica
    st.markdown("### 🎓 Formación Académica")
    
    with st.expander("PhD Student - Alfred Wegener Institute", expanded=True):
        st.write("**Abril 2024-Agosto 2024**")
        st.write("The effect of land-runoff on Antarctic coastal habitats")
    
    with st.expander("Magister en Oceanografía PUCV/UV", expanded=True):
        st.write("**17 April 2023**")
        st.write("Bottom-up controls on summer phytoplankton dynamics")
    
    with st.expander("Grado de Oceanografía PUCV", expanded=True):
        st.write("**September 2015**")
        st.write("Submarine landforms in fjords and bays of the Gerlache Strait")

    # Expediciones
    st.markdown("### 🚢 Expediciones Destacadas")
    
    with st.expander("AWI - Investigación Antártica", expanded=True):
        st.write("**2024 | Alfred Wegener Institute**")
        st.markdown("""
        - Calibración de sensores multiparamétricos EXO-2
        - Procesamiento de datos CTD
        - Visualización en ArcGIS Pro
        - Procesamiento de imágenes RGB y multispectral
        """)
    
    with st.expander("Cimar 28 - Islas Oceánicas", expanded=True):
        st.write("**2023 | Expedición Oceanográfica**")
        st.markdown("""
        - Muestreo de contaminantes orgánicos persistentes
        - Muestreo de carbono orgánico disuelto
        - Muestreo de fitoplancton
        """)

    # Habilidades Técnicas
    st.markdown("### 💻 Habilidades Técnicas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### GIS y Batimetría")
        st.markdown("""
        - ArcGIS Pro
        - CARIS-HIPS
        - Global Mapper
        - DJI Terra/Pix4D
        """)
        
    with col2:
        st.markdown("#### Análisis de Datos")
        st.markdown("""
        - R/RStudio (Expert)
        - Python/Matlab
        - Análisis Estadístico
        - Modelamiento Oceanográfico
        """)

    # Becas
    st.markdown("### 🏆 Becas Destacadas")
    st.info("""
    - ANID National Master's Scholarship (14000 USD x 2 años)
    - Fondap-IDEAL151500
    - FONDECYT regular 1211338
    - Contrato AWI (14000 EUR por 5 meses)
    """)

    # Footer
    st.markdown("---")
    st.markdown(
        f"<div style='text-align: center; color: gray; font-size: 0.8em;'>Actualizado: {datetime.now().strftime('%B %Y')}</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
