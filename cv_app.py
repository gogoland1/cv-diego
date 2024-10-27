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
        box_size=15,        # Mayor resolución
        border=1,           # Borde más delgado
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Crear QR con colores personalizados
    qr_image = qr.make_image(fill_color="#234567", back_color="white")
    
    # Asegurar que la imagen esté en modo RGB para mejor calidad
    qr_image = qr_image.convert('RGB')
    
    # Convertir a bytes con alta calidad
    img_byte_arr = io.BytesIO()
    qr_image.save(img_byte_arr, format='PNG', quality=100, optimize=False)
    return img_byte_arr.getvalue()

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
        st.title("🌊 Diego Hernández-Cerón")
        st.subheader("Oceanógrafo")

    with col2:
        qr_image = create_qr_code(cv_url)
        st.image(qr_image, width=200)  # Mayor tamaño de visualización
        st.caption("Escanea para compartir")

    # Información de Contacto
    st.markdown("### 📬 Contacto")
    col1, col2 = st.columns(2)
    with col1:
        st.write("📧 diego.jhc@gmail.com")
        st.write("📱 +569 32104924")
    with col2:
        st.write("🌍 Quilpué, Chile")
        st.write("🎂 20/09/1989")

    # Formación Académica
    st.markdown("### 🎓 Formación Académica")
    
    with st.expander("PhD Student - Alfred Wegener Institute", expanded=True):
        st.write("**Abril 2024-Agosto 2024 | Bremerhaven, Alemania**")
        st.write("The effect of land-runoff on Antarctic coastal habitats")
    
    with st.expander("Magister en Oceanografía PUCV/UV", expanded=True):
        st.write("**17 April 2023**")
        st.write("Bottom-up controls on summer phytoplankton dynamics in the surface waters of the Gerlache-Bismarck Strait area, Western Antarctic Peninsula")
    
    with st.expander("Grado de Oceanografía PUCV", expanded=True):
        st.write("**September 2015**")
        st.write("Submarine landforms in fjords and bays of the Gerlache Strait, Western Antarctic Peninsula")
        st.write("[Ver tesis](http://opac.pucv.cl/pucv_txt/txt-2500/UCC2858_01.pdf)")

    # Expediciones Antárticas
    st.markdown("### ❄️ Expediciones Antárticas")
    
    with st.expander("Expedición AWI (2024)", expanded=True):
        st.write("**Abril 2024-Agosto 2024 | Alfred Wegener Institute**")
        st.markdown("""
        - Uso y calibración de sensores multiparamétricos EXO-2
        - Procesamiento de datos de CTD in situ de grandes bases de datos Antárticas
        - Visualización en ArcGIS Pro
        - Procesamiento de imágenes RGB y multispectral de drone
        - Organización y logística de campaña Antártica SIGMA-II
        - Análisis de material particulado suspendido (SPM)
        - Preparación de muestras para análisis químico en ICP-OES
        """)

    with st.expander("Expedición Antártica ECA-58 (2021-2022)", expanded=True):
        st.write("**Octubre 2021 - Enero 2022 | Proyecto FONDECYT 1211338**")
        st.markdown("""
        **Área de estudio:** Bahía Maxwell, Península Antártica Occidental
        
        **Tareas principales:**
        - CTD-casts completos (Temperatura, Salinidad, Oxígeno disuelto, Turbidez, Fluorescencia)
        - Muestreo con botellas Niskin y GO-FLO
        - Análisis de clorofila-a, macronutrientes, pH y alcalinidad
        - Muestreo de bacterioplancton para RNA-metabarcoding
        - Muestreo de agua dulce de glaciares para análisis de metales trazas
        """)
    
    with st.expander("Expedición OPERANTAR XXXIV (2015)", expanded=True):
        st.write("**25 Octubre - 18 Noviembre 2015 | Marina de Brasil**")
        st.markdown("""
        **Áreas de estudio:** 
        - Paso Drake
        - Estrecho de Bransfield
        - Islas Shetland del Sur (King George y Decepción)
        
        **Tareas principales:**
        - Adquisición de datos de batimetría multihaz
        - Operación de perfilador sub-acústico
        - Muestreo de sedimentos con gravity corer (~1000 m depth)
        - Muestreo de bentos con box corer
        - Muestreo de columna de agua con sistema CTD-roseta
        """)

    # Otras Expediciones
    st.markdown("### 🚢 Otras Expediciones")
    
    with st.expander("Cimar 28 - Islas Oceánicas (2023)", expanded=True):
        st.write("**Septiembre - Octubre 2023**")
        st.markdown("""
        **Ruta:** Valparaíso-Caldera-Islas Desventuradas-Juan Fernández
        
        **Tareas principales:**
        - Muestreo de contaminantes orgánicos persistentes (POPs)
        - Análisis de fases disueltas y particuladas
        - Muestreo de carbono orgánico disuelto (DOC)
        - Operación de sistemas de filtración avanzados
        """)

    # Habilidades Técnicas
    st.markdown("### 💻 Habilidades Técnicas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Análisis de Datos")
        st.markdown("""
        - R/RStudio (Expert)
        - Python/Matlab (Intermediate)
        - Análisis estadístico avanzado:
          - PCA, cluster analysis
          - NMDS, RDA, db-RDA
          - ANOVA, CCA
          - GAMs
          - Machine Learning en R
        """)
        
    with col2:
        st.markdown("#### Oceanografía y GIS")
        st.markdown("""
        - Ocean Data View
        - CARIS-HIPS/Fledermaus
        - ArcGIS Pro
        - DJI Terra/Pix4D
        - Procesamiento batimétrico
        - Análisis de datos CTD
        """)

    # Becas y Financiamiento
    st.markdown("### 🏆 Becas y Financiamiento")
    st.info("""
    - ANID National Master's Scholarship (14000 USD x 2 años)
    - Fondap-IDEAL151500
    - FONDECYT regular 1211338
    - Contrato AWI (14000 EUR)
    - DFG Project - GEOMAR-Kiel
    """)

    # Otros
    st.markdown("### 📄 Certificaciones")
    st.success("""
    - Licencia de operación de drones europea
    - ArcGIS Pro Training (2024)
    - Inglés Intermedio profesional
    - Licencia de conducir vigente
    """)

    # Footer
    st.markdown("---")
    st.markdown(
        f"<div style='text-align: center; color: gray; font-size: 0.8em;'>Actualizado: {datetime.now().strftime('%B %Y')}</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
