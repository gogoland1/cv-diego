import streamlit as st
from datetime import datetime

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Diego Hernández-Cerón - Oceanógrafo",
        page_icon="🌊",
        layout="centered"
    )

    # Estilos CSS básicos
    st.markdown("""
        <style>
        .header {
            text-align: center;
            padding: 1rem;
            background: linear-gradient(135deg, #234567 0%, #2874A6 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Encabezado
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.title("🌊 Diego Hernández-Cerón")
    st.subheader("Oceanógrafo e Investigador")
    st.markdown("</div>", unsafe_allow_html=True)

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
