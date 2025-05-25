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
    # ✅ Estilos personalizados para mejorar la presentación
    st.markdown("""
        <style>
            .titulo {
                font-size: 36px;
                font-weight: bold;
                color: #1565C0; /* Azul Power BI */
                text-align: center;
            }
            .nombre {
                font-size: 28px;
                font-weight: bold;
                color: #0D47A1; /* Azul oscuro */
                text-align: center;
                margin-bottom: 20px;
            }
            .texto {
                font-size: 18px;
                color: #1E88E5; /* Azul intermedio */
                font-weight: bold;
            }
            .tabla {
                background-color: #E3F2FD;
                color: #1565C0;
                font-size: 16px;
                text-align: center;
            }
            .resaltado {
                background-color: #BBDEFB;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # ✅ Título y nombre resaltados
    st.markdown('<div class="titulo">Evaluación Módulo 4 - Power BI</div>', unsafe_allow_html=True)
    st.markdown('<div class="nombre">Cristina Ana Puertas Camarero</div>', unsafe_allow_html=True)

    st.subheader("Proyecto: Consumo de Agua en España (2020-2022)")

    # 📍 Contexto del Proyecto
    st.markdown('<div class="resaltado">España ha enfrentado sequías prolongadas en los últimos años...</div>', unsafe_allow_html=True)

    # 📊 Tabla de variación de consumo de agua en España
    st.subheader("Evolución del Consumo de Agua en España")

    consumo_data = """
    <table class="tabla">
        <tr>
            <th>Año</th>
            <th>Consumo Promedio (L/día)</th>
            <th>Variación</th>
        </tr>
        <tr>
            <td>2020</td>
            <td>131.1 L</td>
            <td>-</td>
        </tr>
        <tr>
            <td>2022</td>
            <td>130.26 L</td>
            <td>-0.84 L/día</td>
        </tr>
    </table>
    """

    st.markdown(consumo_data, unsafe_allow_html=True)

    # 📍 Fuentes de Datos
    st.subheader("Fuentes de Datos Utilizadas")
    st.markdown("""
    <div class="resaltado">
    ✅ Estudios Nacionales de Consumo de Agua (INE) y Fundación Aquae  
    🔗 [Fundación Aquae](https://www.fundacionaquae.org/en-que-se-utiliza-el-agua-en-espana/)  
    🔗 [INE - Epdata](https://www.epdata.es/datos/graficos-situacion-agua-mundo-espana/333)  
    ✅ Informes de Power BI generados para el curso de la UNED  
    ✅ Análisis comparativos con estándares internacionales  
    </div>
    """, unsafe_allow_html=True)

    # 📌 Preguntas Clave del Informe
    st.subheader("Preguntas Clave del Informe")

    preguntas_clave = [
        "¿Se ha reducido o incrementado el consumo de agua en España en los últimos años?",
        "¿Cuál es la cantidad media de agua consumida por persona?",
        "¿Corresponde la cantidad de agua disponible con el consumo real?",
        "¿España está gestionando de manera eficiente sus recursos hídricos?"
    ]

    for pregunta in preguntas_clave:
        st.markdown(f'<div class="resaltado">✔ {pregunta}</div>', unsafe_allow_html=True)

    # 💡 Importancia del Proyecto
    st.subheader("Importancia del Proyecto")
    st.markdown("""
    <div class="resaltado">
    Comprender el consumo de agua nos permite tomar decisiones clave para asegurar el acceso al agua potable  
    en el futuro y diseñar estrategias de gestión sostenible del recurso.  

    Este estudio proporciona una visión objetiva y basada en datos sobre el tema, respaldada por informes dinámicos generados en Power BI.
    </div>
    """, unsafe_allow_html=True)

  # 📌 Página 2: Datos Principales - Cuadro de mando y visualizaciones
if seleccion == "Datos Principales":
    # ✅ Estilos personalizados para mejorar la presentación
    st.markdown("""
        <style>
            .titulo {
                font-size: 32px;
                font-weight: bold;
                color: #1565C0; /* Azul Power BI */
                text-align: center;
            }
            .subtitulo {
                font-size: 24px;
                font-weight: bold;
                color: #0D47A1; /* Azul oscuro */
                margin-bottom: 10px;
            }
            .texto {
                font-size: 18px;
                color: #1E88E5; /* Azul intermedio */
                font-weight: bold;
            }
            .tabla {
                background-color: #E3F2FD;
                color: #1565C0;
                font-size: 16px;
                text-align: center;
            }
            .resaltado {
                background-color: #BBDEFB;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # ✅ Título destacado
    st.markdown('<div class="titulo">📊 Cuadro de Mando - Consumo de Agua en España</div>', unsafe_allow_html=True)

    # 📌 Informe de Variación de Consumo
    st.markdown('<div class="subtitulo">Informe de Variación de Consumo (2020-2022)</div>', unsafe_allow_html=True)
    st.image("imagenes/variacion_promedio_nacional..png", caption="Informe de variación de consumo")

    # 📊 Tabla de evolución del consumo de agua en España
    st.subheader("Evolución del Consumo de Agua en España")

    consumo_data = """
    <table class="tabla">
        <tr>
            <th>Año</th>
            <th>Consumo Promedio (L/día)</th>
            <th>Variación</th>
        </tr>
        <tr>
            <td>2020</td>
            <td>131.1 L</td>
            <td>-</td>
        </tr>
        <tr>
            <td>2022</td>
            <td>130.26 L</td>
            <td>-0.84 L/día</td>
        </tr>
    </table>
    """

    st.markdown(consumo_data, unsafe_allow_html=True)

    # 📍 Interpretación de los datos
    st.markdown('<div class="subtitulo">Interpretación de los Datos</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="resaltado">
    ✔ **España mantiene un consumo estable**, con una ligera reducción de **-0.84 L** entre 2020 y 2022.  
    
    ✔ **Algunas comunidades superan el umbral recomendado de 200 L/día** debido a factores agrícolas e industriales.  
    
    ✔ **Las restricciones han influido en los hábitos de consumo**, favoreciendo el uso eficiente del agua.  
    </div>
    """, unsafe_allow_html=True)
 # 📌 Página 3: Análisis de Variación del Consumo de Agua
if seleccion == "Análisis de Variación":
    # ✅ Estilos personalizados para mejorar la presentación
    st.markdown("""
        <style>
            .titulo {
                font-size: 32px;
                font-weight: bold;
                color: #1565C0; /* Azul Power BI */
                text-align: center;
            }
            .subtitulo {
                font-size: 24px;
                font-weight: bold;
                color: #0D47A1; /* Azul oscuro */
                margin-bottom: 10px;
            }
            .texto {
                font-size: 18px;
                color: #1E88E5; /* Azul intermedio */
                font-weight: bold;
            }
            .tabla {
                background-color: #E3F2FD;
                color: #1565C0;
                font-size: 16px;
                text-align: center;
            }
            .resaltado {
                background-color: #BBDEFB;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # ✅ Título destacado
    st.markdown('<div class="titulo">📈 Evolución y Variación del Consumo de Agua (2020-2022)</div>', unsafe_allow_html=True)

    # 📊 Comparación de Consumo por Comunidades Autónomas
    st.markdown('<div class="subtitulo">Comparación de Consumo por Comunidades Autónomas</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="resaltado">
    Algunas comunidades han reducido su consumo gracias a políticas de eficiencia hídrica, mientras que  
    otras han enfrentado **mayores demandas** por factores climáticos y económicos.
    </div>
    """, unsafe_allow_html=True)

    # 📌 Imagen del consumo por comunidad
    st.image("imagenes/consumo_promedio_comunidad.png", caption="Consumo de agua por comunidad")

    # 📊 Tabla de evolución del consumo de agua por comunidad
    st.subheader("Evolución del Consumo de Agua por Comunidad Autónoma")

    consumo_comunidad = """
    <table class="tabla">
        <tr>
            <th>Comunidad Autónoma</th>
            <th>Consumo 2020 (L/día)</th>
            <th>Consumo 2022 (L/día)</th>
            <th>Variación</th>
        </tr>
        <tr>
            <td>Andalucía</td>
            <td>147 L</td>
            <td>144 L</td>
            <td>-3 L</td>
        </tr>
        <tr>
            <td>Cataluña</td>
            <td>138 L</td>
            <td>133 L</td>
            <td>-5 L</td>
        </tr>
        <tr>
            <td>Madrid</td>
            <td>130 L</td>
            <td>125 L</td>
            <td>-5 L</td>
        </tr>
        <tr>
            <td>País Vasco</td>
            <td>128 L</td>
            <td>119 L</td>
            <td>-9 L</td>
        </tr>
    </table>
    """

    st.markdown(consumo_comunidad, unsafe_allow_html=True)

    # 📢 Análisis de Datos
    st.markdown('<div class="subtitulo">Análisis de Datos</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="resaltado">
    ✔ **Andalucía** mantiene uno de los consumos más altos, aunque ha reducido su gasto de **147L a 144L**.  
    ✔ **Cataluña y Madrid** han ajustado su consumo, bajando de **138L a 133L**, y **130L a 125L**, respectivamente.  
    ✔ **País Vasco** ha experimentado una reducción significativa, pasando de **128L a 119L**.  
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
         .tabla {
             width: 100%;
             border-collapse: collapse;
            }
         .tabla th, .tabla td {
             border: 1px solid #1565C0; /* Azul Power BI */
             padding: 8px;
             text-align: center;
            }
            .tabla th {
             background-color: #BBDEFB; /* Azul claro */
             font-weight: bold;
         }
            .tabla td {
             background-color: #E3F2FD;
         }
        </style>
    """, unsafe_allow_html=True)

    factores_consumo = """ 
    <table class="tabla">
     <tr>
            <th>Factor</th>
            <th>Impacto en el consumo</th>
        </tr>
        <tr>
            <td>Restricciones gubernamentales</td>
            <td>Limitaciones en consumo individual y eficiencia en infraestructuras.</td>
        </tr>
        <tr>
            <td>Condiciones climáticas</td>
            <td>Años con menos precipitaciones han afectado el consumo en ciertas regiones.</td>
        </tr>
        <tr>
         <td>Concienciación social</td>
         <td>Campañas de ahorro han promovido mejores hábitos de consumo.</td>
        </tr>
    </table>
    """

    st.markdown(factores_consumo, unsafe_allow_html=True)


# 📌 Página 4: Factores que Impactan el Consumo de Agua
if seleccion == "Factores del Consumo":
    st.title(" Hábitos de Consumo ")
    st.subheader("🔎 Hábitos del Consumo de Agua en España")

    st.write("""
    El consumo de agua en España varía significativamente según la actividad realizada.  
    A continuación, analizamos **los principales factores** que determinan el uso del agua en el hogar:
    """)
    st.image("imagenes/suma_consumo_agua.png", caption="Consumo de agua por actividad")
    st.subheader("🔹 **1️⃣ Baños y Duchas**")
    st.write("""
    ✔ **Baños largos representan el mayor consumo**, alcanzando hasta **200L** por sesión.  
    ✔ **Duchas reducen el gasto**, con un promedio de **52.5L** por ducha.  
    ✔ Optar por **duchas cortas y sistemas de ahorro** puede reducir el consumo hasta en un **30%**.
    """)

    st.subheader("🔹 **2️⃣ Lavado de Vajilla y Ropa**")
    st.write("""
    ✔ **Lavar la vajilla a mano requiere hasta 100L**, mientras que una **lavadora eficiente solo usa 34L**.  
    ✔ **Lavar ropa consume 80L**, pero **programas ecológicos pueden reducir este gasto** significativamente.  
    ✔ Usar **electrodomésticos eficientes y cargas completas** optimiza el consumo.
    """)

    st.subheader("🔹 **3️⃣ Afeitado y Higiene Personal**")
    st.write("""
    ✔ **Afeitarse con agua corriendo gasta hasta 57.5L**, mientras que cerrando el grifo se reduce a menos de 10L.  
    ✔ **Lavarse los dientes consume 30L si se deja el grifo abierto**, pero cerrándolo se reduce a **2L**.  
    ✔ Pequeños cambios en la rutina **pueden generar grandes ahorros**.
    """)

    st.subheader("🔹 **4️⃣ Descarga de la Cisterna y Limpieza del Hogar**")
    st.write("""
    ✔ **Cada descarga de cisterna usa 3L**, por lo que **sistemas de doble descarga** pueden reducir el consumo.  
    ✔ **Limpieza del hogar consume 27.5L** en promedio, pero reutilizar agua puede disminuir este impacto.  
    ✔ Uso de **productos ecológicos y métodos eficientes** favorecen el ahorro.
    """)
# 📌 Página 5: Conclusiones sobre el Consumo de Agua en España
if seleccion == "Conclusiones":
    # ✅ Estilos personalizados para mejorar la presentación
    st.markdown("""
        <style>
            .titulo {
                font-size: 32px;
                font-weight: bold;
                color: #1565C0; /* Azul Power BI */
                text-align: center;
            }
            .subtitulo {
                font-size: 24px;
                font-weight: bold;
                color: #0D47A1; /* Azul oscuro */
                margin-bottom: 10px;
            }
            .texto {
                font-size: 18px;
                color: #1E88E5; /* Azul intermedio */
                font-weight: bold;
            }
            .tabla {
                background-color: #E3F2FD;
                color: #1565C0;
                font-size: 16px;
                text-align: center;
            }
            .resaltado {
                background-color: #BBDEFB;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # ✅ Título destacado
    st.markdown('<div class="titulo"> Conclusión: Hacia una Gestión Sostenible del Agua</div>', unsafe_allow_html=True)

    # 📍 Resumen de Hallazgos
    st.markdown('<div class="subtitulo"> Resumen de Hallazgos</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="resaltado">
    📌 **España ha mantenido un consumo estable**, con una leve reducción de **-0.84 L** entre 2020 y 2022.  
    
    📌 **Las comunidades con mayor consumo per cápita** incluyen Andalucía, Cantabria y Castilla y León.  
    
    📌 **El sector agrícola es el principal consumidor**, representando **55%** del uso total.  
    
    📌 **Las políticas de ahorro han influido positivamente**, reduciendo el consumo en varias regiones.  
    </div>
    """, unsafe_allow_html=True)

    
    # 📌 Imagen del consumo comparativo
    st.image("imagenes/consumo_comparativa_promedio.png", caption="Gasto por actividad comparado con el uso medio diario")

    # 📊 Estrategias de Optimización
    st.markdown('<div class="subtitulo">🌍 Estrategias de Optimización</div>', unsafe_allow_html=True)

    estrategias_agua = """
    <table class="tabla">
        <tr>
            <th>Estrategia</th>
            <th>Impacto en el Consumo</th>
        </tr>
        <tr>
            <td>Uso eficiente en hogares</td>
            <td>Reducción de desperdicios en baños y limpieza.</td>
        </tr>
        <tr>
            <td>Mejoras en riego agrícola</td>
            <td>Implementación de tecnologías de irrigación más avanzadas.</td>
        </tr>
        <tr>
            <td>Optimización industrial</td>
            <td>Sistemas de reciclaje de agua en fábricas.</td>
        </tr>
        <tr>
            <td>Concienciación social</td>
            <td>Programas educativos para fomentar el ahorro de agua.</td>
        </tr>
    </table>
    """

    st.markdown(estrategias_agua, unsafe_allow_html=True)

    # 📌 Panel de Power BI embebido
    st.markdown('<div class="subtitulo">Panel de Análisis Final en Power BI</div>', unsafe_allow_html=True)
    st.markdown("""
    <iframe title="Informe Power BI Aguas - Conclusiones" width="1000" height="600"
    src="https://drive.google.com/file/d/1AHJuKLcy6AfCyzLwC_DZiwbvX_uXmm7o/view?usp=sharing"
    frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)
    
    # 📌 Reflexiones Finale
    st.markdown('Muchas gracias', unsafe_allow_html=True)
    st.markdown('Cristina Ana Puertas Camarero', unsafe_allow_html=True)
    st.markdown('Evaluación Módulo 4 - Power BI', unsafe_allow_html=True)
    st.markdown('UNED', unsafe_allow_html=True)
    
    
