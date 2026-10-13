"""Interfaz Streamlit del chatbot de capacitación para mandos medios."""
import streamlit as st

st.set_page_config(page_title="Asistente para mandos medios", page_icon="📊")
PASOS = ["Inicio", "Definir puesto", "KPIs y EPM", "Planear entrevista", "Consejos", "Simulación", "Lista final"]
CHECKS = [
    "Confirmé las responsabilidades y objetivos del puesto.",
    "Reuní KPIs y verifiqué sus fuentes.",
    "Comparé los resultados con metas acordadas.",
    "Preparé ejemplos de fortalezas y áreas de mejora.",
    "Agendé un espacio privado para la conversación.",
    "Preparé preguntas abiertas para escuchar al colaborador.",
    "Definiré acciones, responsables y fechas de seguimiento.",
]
CRITERIOS = {
    "Evidencia": ("dato", "resultado", "meta", "indicador", "entrega", "%"),
    "Escucha respetuosa": ("entiendo", "gracias", "comprendo", "perspectiva", "escuchar"),
    "Solución": ("mejorar", "apoyo", "acción", "plan", "solución", "acordar", "seguimiento"),
}
if "puesto" not in st.session_state:
    st.session_state.puesto = ""
if "paso" not in st.session_state:
    st.session_state.paso = PASOS[0]

def avanzar(siguiente):
    st.session_state.paso = siguiente
    st.rerun()

with st.sidebar:
    st.header("Capacitación de líderes")
    actual = st.radio("Contenido", PASOS, key="paso")
    st.caption(f"Puesto: {st.session_state.puesto or 'No especificado'}")

st.title("Asistente de capacitación para líderes")
if actual == "Inicio":
    st.write("Bienvenido al asistente de capacitación para líderes y mandos medios.")
    st.markdown("""En esta capacitación aprenderás a:
- Definir el puesto que vas a evaluar.
- Comprender los KPIs y su tablero de seguimiento.
- Reunir evidencia mediante EPM.
- Planear una entrevista de retroalimentación.
- Dar retroalimentación clara, respetuosa y útil.""")
    st.info("La meta es evaluar de manera objetiva y enfocada en el desarrollo del colaborador.")
    if st.button("Comenzar", type="primary"):
        avanzar(PASOS[1])
elif actual == "Definir puesto":
    st.subheader("1. Definición del puesto")
    with st.form("puesto_form"):
        puesto = st.text_input("¿Qué puesto o área deseas evaluar?", st.session_state.puesto)
        claro = st.radio("¿La descripción del puesto está clara?", ["Sí", "No"], horizontal=True)
        enviar = st.form_submit_button("Guardar", type="primary")
    if enviar:
        st.session_state.puesto = puesto.strip() or "Puesto no especificado"
        st.success("Puesto guardado: " + st.session_state.puesto)
        if claro == "No":
            st.warning("Consulta a Recursos Humanos o al colaborador para confirmar responsabilidades.")
    st.markdown("""Identifica lo siguiente:
1. Objetivo principal.
2. Responsabilidades.
3. Resultados esperados.
4. Competencias.
5. Alineación con el objetivo del área.

**Ejemplo:** un vendedor puede evaluarse por ventas, atención al cliente y seguimiento de pedidos.""")
    if st.button("Continuar"):
        avanzar(PASOS[2])
elif actual == "KPIs y EPM":
    st.subheader("2. KPIs, tablero y EPM")
    st.write("Puesto:", st.session_state.puesto or "No especificado")
    st.markdown("""Los **KPIs** son indicadores clave para medir el cumplimiento de resultados.

**Ejemplos de indicadores:**
1. Cumplimiento de objetivos = resultado / meta × 100.
2. Calidad = trabajos aceptados / trabajos revisados × 100.
3. Entregas a tiempo = entregas puntuales / entregas totales × 100.

**Un tablero debe mostrar:** indicador, meta, resultado real, diferencia, tendencia y acción de mejora.

En este tutorial, **EPM** se refiere a la evaluación del desempeño mediante evidencia. Confirma con el profesor o empresa su metodología oficial.

**Para reunir evidencia:** usa reportes verificables, observaciones documentadas, metas acordadas, contexto y oportunidades de mejora.""")
    st.info("Ejemplo hipotético: entregas a tiempo, meta 95%, resultado 88%. Diferencia: 7 puntos porcentuales.")
    with st.form("kpis"):
        dato = st.text_area("Datos de tus KPIs (opcional): indicador, meta, resultado y periodo")
        guardar = st.form_submit_button("Registrar datos")
    if guardar:
        if dato.strip():
            st.session_state.kpis = dato.strip()
            st.success("Información registrada únicamente durante esta sesión.")
        else:
            st.info("Puedes continuar con los ejemplos.")
    if st.button("Continuar"):
        avanzar(PASOS[3])
elif actual == "Planear entrevista":
    st.subheader("3. Planeación de una entrevista")
    pasos = [
        ("Define el objetivo", "Qué resultados revisarás y qué quieres lograr."),
        ("Reúne evidencia", "Prepara KPIs, ejemplos y registros."),
        ("Identifica fortalezas y mejoras", "Evita generalizaciones."),
        ("Agenda la reunión", "Busca un espacio privado y tiempo suficiente."),
        ("Prepara preguntas abiertas", "Escucha la perspectiva del colaborador."),
        ("Organiza la conversación", "Reconoce logros y revisa resultados."),
        ("Cierra con acuerdos", "Asigna acciones, plazos y seguimiento."),
    ]
    for i, (nombre, detalle) in enumerate(pasos, 1):
        with st.expander(f"{i}. {nombre}"):
            st.write(detalle)
    st.markdown("""**Preguntas sugeridas:**
- ¿Cómo consideras tu desempeño este periodo?
- ¿Qué resultados te parecen más importantes?
- ¿Qué obstáculos encontraste?
- ¿Qué apoyo necesitas?
- ¿Qué objetivo buscas alcanzar en el siguiente periodo?""")
    if st.button("Continuar"):
        avanzar(PASOS[4])
elif actual == "Consejos":
    st.subheader("4. Consejos para retroalimentar")
    consejos = [
        "Habla de hechos observables, no de características personales.",
        "Reconoce logros con ejemplos específicos.",
        "Explica las áreas de mejora con respeto.",
        "Escucha sin interrumpir.",
        "Evita comparaciones con otros compañeros.",
        "Aborda los problemas oportunamente.",
        "Enfócate en soluciones y desarrollo.",
        "Acuerda acciones específicas y realistas.",
        "Mantén la confidencialidad.",
        "Da seguimiento a los compromisos.",
    ]
    for i, consejo in enumerate(consejos, 1):
        st.write(f"{i}. {consejo}")
    st.error('Menos efectivo: "Siempre entregas tarde y eres desorganizado."')
    st.success('Mejor: "Tres entregas se hicieron después de la fecha acordada. ¿Qué obstáculos hubo y cómo podemos mejorar los tiempos?"')
    if st.button("Practicar"):
        avanzar(PASOS[5])
elif actual == "Simulación":
    st.subheader("5. Simulación práctica")
    st.info("Caso: un colaborador no alcanzó su meta mensual y comenta que tuvo problemas con una herramienta de trabajo.")
    with st.form("simulacion"):
        respuesta = st.text_area("¿Cómo iniciarías la conversación de retroalimentación?")
        evaluar = st.form_submit_button("Evaluar", type="primary")
    if evaluar:
        if not respuesta.strip():
            st.warning("Escribe una respuesta para recibir retroalimentación.")
        else:
            texto = respuesta.lower()
            encontrados = {nombre: any(p in texto for p in palabras) for nombre, palabras in CRITERIOS.items()}
            st.metric("Criterios detectados", f"{sum(encontrados.values())} / 3")
            for nombre, cumple in encontrados.items():
                st.write(("✅" if cumple else "⬜") + " " + nombre)
            if all(encontrados.values()):
                st.success("Incluiste evidencia, escucha y soluciones. Recuerda acordar un plazo.")
            else:
                st.info("Agrega los elementos pendientes: evidencia concreta, escucha respetuosa y una acción con seguimiento.")
            st.caption("Evaluación básica por palabras clave; no utiliza IA generativa.")
    st.write('**Ejemplo:** "La meta del mes era alcanzar el 100% y el resultado fue menor. ¿Qué dificultades tuviste y qué apoyo necesitas? Acordemos una acción y fecha de seguimiento."')
    if st.button("Continuar"):
        avanzar(PASOS[6])
else:
    st.subheader("6. Lista de verificación final")
    completados = sum(st.checkbox(elemento, key=f"check_{i}") for i, elemento in enumerate(CHECKS))
    st.progress(completados / len(CHECKS))
    st.metric("Lista completada", f"{completados} de {len(CHECKS)}")
    if completados == len(CHECKS):
        st.success("¡Estás preparado para realizar la entrevista!")
    else:
        st.info("Revisa los puntos pendientes.")
    if st.button("Volver al inicio"):
        avanzar(PASOS[0])

st.divider()
st.caption("Demostración educativa. No ingreses información confidencial de colaboradores.")
