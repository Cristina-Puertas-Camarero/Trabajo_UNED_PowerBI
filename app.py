import streamlit as st


# 📌 Configuración del diseño global
st.set_page_config(page_title="Consumo de Agua en España", layout="wide")

# 📌 Estilos CSS para mejorar la apariencia
st.markdown("""
    <style>
        /* Cambiar el color del fondo */
        .main {
            background-color: #E3F2FD; /* Azul agua */
        }
        /* Estilizar la barra lateral */
        [data-testid="stSidebar"] {
            background-color: #1565C0; /* Azul profundo */
        }
        /* Mejorar los títulos */
        .stTitle {
            font-size: 26px;
            font-weight: bold;
            color: #0D47A1;
        }
    </style>
""", unsafe_allow_html=True)

# 📌 Sidebar estático con el menú fijo
with st.sidebar:
    st.markdown("### Secciones del Proyecto")
    seleccion = st.selectbox(
        "Selecciona una sección:",
        ["Inicio", "Datos Principales", "Análisis de Variación", "Factores del Consumo", "Conclusiones"]
    )

# 📌 Página 1: Inicio - Introducción al Proyecto
if seleccion == "Inicio":
    st.title("Evaluación Módulo 4, Power BI. ")
    
    st.subheader("Cristina Ana Puertas Camarero")

    st.subheader(" Proyecto: Consumo de Agua en España (2020-2022)")
    st.write("""
    En los últimos años, España ha enfrentado **sequías prolongadas**, lo que ha generado la necesidad de establecer  
    límites de consumo de agua para la población. La medida más extendida fija el consumo máximo por persona  
    en **200 litros/día**.  
    """)
    
    st.write("""
    Este proyecto analiza los datos históricos de consumo de agua en España entre **2020 y 2022**,  
    evaluando si la población está cumpliendo con los estándares recomendados y cómo se comparan estos valores  
    con otras regiones del mundo.
    """)
    
    

    st.write("""
    🔹 **2020:** 131.1 L/día  
    🔹 **2022:** 130.26 L/día  
    🔹 **Diferencia:** -0.84 L/día (leve reducción en consumo)
    """)

    st.subheader("📍 Fuentes de Datos")
    st.write("""
    Para este análisis, hemos utilizado información de:  
    - **Estudios Nacionales de Consumo de Agua (INE) y Fundación Aquae**  
    -Fundación Aquae:  
    URL: https://www.fundacionaquae.org/en-que-se-utiliza-el-agua-en-espana/
    - INE - Epdata:
    URL: https://www.epdata.es/datos/graficos-situacion-agua-mundo-espana/333

    - **Informes de Power BI generados para el curso de la UNED**  
    - **Análisis comparativos con estándares internacionales**
    """)

    st.subheader("📌 Preguntas Clave del Informe")
    st.write("""
    ✔ ¿Se ha **reducido** o **incrementado** el consumo de agua en España en los últimos años?  
    ✔ ¿Cuál es la cantidad **media de agua consumida** por persona?  
    ✔ ¿Corresponde la cantidad de agua disponible con el consumo real?  
    ✔ ¿España está **gestionando de manera eficiente** sus recursos hídricos?  
    """)

    st.subheader("💡 Importancia del Proyecto")
    st.write("""
    📢 **Comprender el consumo de agua** nos permite tomar decisiones clave para asegurar el acceso al agua potable  
    en el futuro y diseñar estrategias de **gestión sostenible** del recurso.  
    Este estudio proporciona una visión **objetiva y basada en datos** sobre el tema, respaldada por informes  
    dinámicos generados en Power BI.
    """)

    
# 📌 Página 2: Datos Principales - Cuadro de mando y visualizaciones
if seleccion == "Datos Principales":
    st.title("📊 Cuadro de Mando - Consumo de Agua en España")
    
    st.subheader("📌 Informe de Variación de Consumo (2020-2022)")
    st.markdown("""
    <iframe title="Informe Power BI Aguas2" width="1000" height="600"
    src="https://drive.google.com/file/d/10CuIDb-ZuZ3Qkayre_cdl-0k88uxI8CC/view?usp=sharing"
    frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)

    st.subheader("📌 Análisis de Consumo por Comunidad Autónoma")
    st.markdown("""
    <iframe title="Informe Power BI Aguas" width="1000" height="600"
    src="https://drive.google.com/file/d/1AHJuKLcy6AfCyzLwC_DZiwbvX_uXmm7o/view?usp=sharing"
    frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)

    st.write("""
    🔍 **Interpretación de los Datos:**  
    ✔ **España mantiene un consumo estable**, con una ligera reducción de **-0.84 L** entre 2020 y 2022.  
    ✔ **Algunas comunidades superan el umbral recomendado de 200 L/día** debido a factores agrícolas e industriales.  
    ✔ **Las restricciones han influido en los hábitos de consumo**, favoreciendo el uso eficiente del agua.  
    """)

    
# 📌 Página 3: Análisis de Variación del Consumo de Agua
if seleccion == "Análisis de Variación":
    st.title("📈 Evolución y Variación del Consumo de Agua (2020-2022)")

    st.subheader("📊 Comparación de Consumo por Comunidades Autónomas")
    st.write("""
    Esta sección analiza cómo ha cambiado el consumo de agua en distintas regiones de España.  
    Algunas comunidades han reducido su consumo gracias a políticas de eficiencia hídrica, mientras que  
    otras han enfrentado **mayores demandas** por factores climáticos y económicos.
    """)

    

    st.subheader("📢 Análisis de Datos")
    st.write("""
    🔹 **Andalucía** mantiene uno de los consumos más altos, aunque ha reducido su gasto de **147L a 144L**.  
    🔹 **Cataluña y Madrid** han ajustado su consumo, bajando de **138L a 133L**, y **130L a 125L**, respectivamente.  
    🔹 **País Vasco** ha experimentado una reducción significativa, pasando de **128L a 119L**.  
    """)

    st.subheader("🔎 Factores que han influido en la variación del consumo:")
    st.write("""
    ✔ **Restricciones gubernamentales**: Limitaciones en consumo individual y eficiencia en infraestructuras.  
    ✔ **Condiciones climáticas**: Años con menos precipitaciones han afectado el consumo en ciertas regiones.  
    ✔ **Concienciación social**: Campañas de ahorro han promovido mejores hábitos de consumo.  
    """)

    # 📌 Panel de Power BI embebido
    st.subheader("📌 Panel de Análisis en Power BI")
    st.markdown("""
    <iframe title="Informe Power BI Aguas2 - Variación del Consumo" width="1000" height="600"
    src="https://drive.google.com/file/d/10CuIDb-ZuZ3Qkayre_cdl-0k88uxI8CC/view?usp=sharing"
    frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)

    
# 📌 Página 4: Factores que Impactan el Consumo de Agua
if seleccion == "Factores del Consumo":
    st.title("🔎 Factores que Impactan el Consumo de Agua en España")
    
    st.subheader("🌍 Sectores con Mayor Consumo")
    st.write("""
    El consumo de agua en España varía según el sector.  
    Estas son las principales fuentes de consumo y sus impactos:
    """)

    

    st.subheader("🔹 **1️⃣ Riego Agrícola**")
    st.write("""
    ✔ Representa aproximadamente **55% del consumo total** en España.  
    ✔ Depende de la temporada y del tipo de cultivo.  
    ✔ Las sequías han llevado a la implementación de **sistemas de riego más eficientes**.
    """)

    st.subheader("🔹 **2️⃣ Uso Doméstico**")
    st.write("""
    ✔ Aporta el **30% del consumo total** en el país.  
    ✔ Hábitos como baños largos y uso excesivo en limpieza pueden aumentar el gasto.  
    ✔ Implementar cambios en el hogar puede **optimizar el consumo**.
    """)

    st.subheader("🔹 **3️⃣ Consumo Industrial y Turístico**")
    st.write("""
    ✔ El consumo en **industria y turismo representa un 15%** del total.  
    ✔ Ciudades con alta actividad comercial tienen **mayores demandas de agua**.  
    ✔ Uso responsable en hoteles, restaurantes y fábricas **puede reducir costos**.
    """)

    # 📌 Panel de Power BI embebido
    st.subheader("📌 Panel de Análisis en Power BI")
    st.markdown("""
    <iframe title="Informe Power BI Aguas - Factores del Consumo" width="1000" height="600"
    src="https://drive.google.com/file/d/1AHJuKLcy6AfCyzLwC_DZiwbvX_uXmm7o/view?usp=sharing"
    frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)

   
# 📌 Página 5: Conclusiones sobre el Consumo de Agua en España
if seleccion == "Conclusiones":
    st.title("📢 Conclusión: Hacia una Gestión Sostenible del Agua")
    
    st.subheader("🔍 Resumen de Hallazgos")
    st.write("""
    📌 **España ha mantenido un consumo estable**, con una leve reducción de **-0.84 L** entre 2020 y 2022.  
    📌 **Las comunidades con mayor consumo per cápita** incluyen Andalucía, Cantabria y Castilla y León.  
    📌 **El sector agrícola es el principal consumidor**, representando **55%** del uso total.  
    📌 **Las políticas de ahorro han influido positivamente**, reduciendo el consumo en varias regiones.  
    """)

    


    st.subheader("🌍 Estrategias de Optimización")
    st.write("""
    ✔ **Uso eficiente en hogares**: Reducir desperdicios en baños y limpieza.  
    ✔ **Mejoras en riego agrícola**: Tecnologías de irrigación más avanzadas.  
    ✔ **Optimización industrial**: Sistemas de reciclaje de agua en fábricas.  
    ✔ **Concienciación social**: Educación sobre la importancia del ahorro.  
    """)

    

    
