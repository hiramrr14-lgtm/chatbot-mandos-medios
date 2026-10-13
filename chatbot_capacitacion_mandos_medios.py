# CHATBOT DE CAPACITACIÓN PARA MANDOS MEDIOS
# Ejecutable en Thonny con Python 3. No requiere instalar librerías.

def pausa():
    input("\nPresiona ENTER para continuar...")


def titulo(texto):
    print("\n" + "=" * 65)
    print(texto.upper())
    print("=" * 65)


def bienvenida():
    titulo("Asistente de capacitación para líderes")
    print("¡Bienvenido al asistente de capacitación para líderes y mandos medios!")
    print("\nTe ayudaré a prepararte para evaluar el desempeño de tus colaboradores.")
    print("En esta capacitación aprenderás a:")
    print("- Definir el puesto que vas a evaluar.")
    print("- Comprender los KPIs y su tablero de seguimiento.")
    print("- Entender cómo reunir evidencia mediante EPM.")
    print("- Planear una entrevista de retroalimentación.")
    print("- Dar retroalimentación clara, respetuosa y útil.")
    print("\nLa meta es realizar una evaluación objetiva, basada en evidencia")
    print("y enfocada en el desarrollo del colaborador.")
    pausa()


def definir_puesto():
    titulo("1. Definición del puesto")
    puesto = input("¿Qué puesto o área deseas evaluar? ").strip()

    if not puesto:
        puesto = "Puesto no especificado"

    print("\nPuesto seleccionado:", puesto)
    print("\nPara evaluar correctamente este puesto, identifica:")
    print("1. Objetivo principal: ¿para qué existe el puesto?")
    print("2. Responsabilidades: ¿qué actividades debe realizar?")
    print("3. Resultados esperados: ¿qué debe lograr?")
    print("4. Competencias: ¿qué conocimientos y habilidades necesita?")
    print("5. Alineación: ¿cómo contribuye al objetivo del área?")
    print("\nEjemplo:")
    print("Si el puesto es vendedor, se pueden evaluar las ventas,")
    print("la atención al cliente y el seguimiento a los pedidos.")
    print("\nRecuerda: confirma las responsabilidades reales con la descripción")
    print("del puesto y con las políticas de tu organización.")
    confirmacion = input("\n¿La descripción del puesto está clara? (sí/no): ").strip().lower()
    if confirmacion in ("no", "n"):
        print("Antes de evaluar, consulta al colaborador o a Recursos Humanos")
        print("para confirmar sus responsabilidades y objetivos.")
    return puesto


def explicar_kpis_epm(puesto):
    titulo("2. KPIs, tablero y EPM")
    print("Los KPIs son indicadores clave de desempeño. Sirven para medir")
    print("si una persona está alcanzando los resultados esperados.")
    print("\nPuesto de referencia:", puesto)
    print("\nEjemplos de KPIs (debes adaptarlos al puesto real):")
    print("1. Cumplimiento de objetivos = resultado obtenido / meta × 100")
    print("2. Calidad = trabajos aceptados / trabajos revisados × 100")
    print("3. Entregas a tiempo = entregas puntuales / entregas totales × 100")
    print("\nNo todos los KPIs sirven para todos los puestos. Elige indicadores")
    print("que dependan de las responsabilidades reales del colaborador.")
    print("\n¿Qué debe mostrar el tablero?")
    print("- Nombre del KPI")
    print("- Meta acordada")
    print("- Resultado real")
    print("- Diferencia entre meta y resultado")
    print("- Estado o tendencia")
    print("- Acción de mejora, si se necesita")
    print("\n¿Cómo se relaciona con EPM?")
    print("En este tutorial, EPM se utiliza como evaluación del desempeño")
    print("mediante evidencia. Confirma con tu profesor o empresa qué significa")
    print("exactamente la sigla y cuál es su metodología oficial.")
    print("\nPara reunir evidencia:")
    print("1. Obtén datos de fuentes verificables: reportes, sistemas o registros.")
    print("2. Revisa observaciones documentadas y ejemplos concretos.")
    print("3. Compara los resultados reales con las metas acordadas.")
    print("4. Investiga el contexto antes de atribuir las diferencias al colaborador.")
    print("5. Identifica fortalezas, brechas y acciones de mejora.")
    print("\nImportante: los siguientes valores son solo un ejemplo hipotético.")
    print("KPI: entregas a tiempo | Meta: 95% | Resultado: 88%")
    print("Interpretación: existe una diferencia de 7 puntos porcentuales.")
    print("Antes de concluir por qué ocurrió, hay que revisar las causas.")
    print("\n¿Tienes datos reales de KPIs para analizar?")
    print("1. Sí")
    print("2. No, quiero continuar con el tutorial")
    opcion = input("Elige 1 o 2: ").strip()
    if opcion == "1":
        print("\nEscribe tus datos en este formato: KPI, meta, resultado y periodo.")
        datos = input("Tus datos: ").strip()
        if datos:
            print("\nDatos registrados para esta conversación:", datos)
            print("Revisa que las unidades sean comparables y que la fuente sea confiable.")
        else:
            print("No se ingresaron datos; continuaremos con ejemplos.")
    pausa()


def planear_entrevista():
    titulo("3. Cómo planear una entrevista de retroalimentación")
    pasos = [
        ("Define el objetivo", "Decide qué resultados revisarás y qué quieres lograr."),
        ("Reúne evidencia", "Prepara KPIs, ejemplos concretos y registros relevantes."),
        ("Identifica fortalezas y mejoras", "Evita generalizaciones; utiliza hechos observables."),
        ("Agenda la reunión", "Elige un espacio privado y suficiente tiempo."),
        ("Prepara preguntas abiertas", "Invita al colaborador a explicar su experiencia."),
        ("Organiza la conversación", "Reconoce logros, revisa resultados y escucha su perspectiva."),
        ("Cierra con acuerdos", "Define acciones, responsables, plazos y seguimiento.")
    ]
    for numero, (paso, detalle) in enumerate(pasos, 1):
        print(f"\n{numero}. {paso}: {detalle}")

    print("\nPreguntas que puedes hacer:")
    print("- ¿Cómo consideras que fue tu desempeño durante este periodo?")
    print("- ¿Qué resultados te parecen más importantes?")
    print("- ¿Qué obstáculos encontraste?")
    print("- ¿Qué apoyo necesitas?")
    print("- ¿Qué objetivo te gustaría alcanzar en el siguiente periodo?")
    pausa()


def tips_retroalimentacion():
    titulo("4. Tips para una retroalimentación exitosa")
    tips = [
        "Habla de hechos observables, no de características personales.",
        "Reconoce los logros con ejemplos específicos.",
        "Explica las áreas de mejora con claridad y respeto.",
        "Escucha sin interrumpir.",
        "Evita comparaciones innecesarias con otros compañeros.",
        "Aborda los problemas oportunamente.",
        "Enfócate en soluciones y oportunidades de desarrollo.",
        "Acuerda acciones específicas, medibles y realistas.",
        "Mantén la confidencialidad.",
        "Da seguimiento a los compromisos."
    ]
    for numero, tip in enumerate(tips, 1):
        print(f"{numero}. {tip}")

    print("\nEjemplo de comunicación:")
    print('MENOS EFECTIVO: "Siempre entregas tarde y eres desorganizado."')
    print('MEJOR: "Tres entregas se hicieron después de la fecha acordada.')
    print('¿Qué obstáculos hubo y cómo podemos mejorar los tiempos?"')
    print("\nLa segunda frase es mejor porque describe hechos, evita etiquetar")
    print("a la persona e invita a buscar soluciones.")
    pausa()


def simulacion():
    titulo("5. Simulación práctica")
    print("Situación hipotética:")
    print("Un colaborador no alcanzó su meta mensual y comenta que tuvo")
    print("problemas con una herramienta de trabajo.")
    print("\nEscribe cómo iniciarías la conversación de retroalimentación.")
    respuesta = input("> ").strip()

    if not respuesta:
        print("\nNo escribiste una respuesta. Puedes practicar después.")
        return

    puntos = 0
    criterios = [
        ("evidencia", ("dato", "resultado", "meta", "indicador", "entrega", "%")),
        ("respeto", ("entiendo", "gracias", "comprendo", "perspectiva", "escuchar")),
        ("solución", ("mejorar", "apoyo", "acción", "plan", "solución", "acordar", "seguimiento"))
    ]

    for nombre, palabras in criterios:
        if any(palabra in respuesta.lower() for palabra in palabras):
            puntos += 1

    print("\nRetroalimentación sobre tu respuesta:")
    if puntos == 3:
        print("¡Buen trabajo! Tu respuesta menciona evidencia, escucha respetuosa")
        print("y orientación a soluciones. Asegúrate también de acordar un plazo.")
    else:
        print("Puedes fortalecer tu respuesta incorporando estos elementos:")
        if not any(p in respuesta.lower() for p in criterios[0][1]):
            print("- Evidencia concreta: menciona la meta y el resultado observado.")
        if not any(p in respuesta.lower() for p in criterios[1][1]):
            print("- Escucha respetuosa: pregunta qué ocurrió y escucha su perspectiva.")
        if not any(p in respuesta.lower() for p in criterios[2][1]):
            print("- Solución: acuerda una acción, el apoyo necesario y una fecha de seguimiento.")
    print("\nEjemplo de respuesta mejorada:")
    print('"La meta de este mes era alcanzar el 100% y el resultado fue menor.')
    print('Quisiera entender qué dificultades tuviste con la herramienta y')
    print('qué apoyo necesitas. Acordemos una acción y revisemos el avance')
    print('en una fecha específica."')
    pausa()


def lista_verificacion():
    titulo("Lista de verificación final")
    elementos = [
        "Confirmé las responsabilidades y objetivos del puesto.",
        "Reuní KPIs y verifiqué sus fuentes.",
        "Comparé los resultados con metas acordadas.",
        "Preparé ejemplos de fortalezas y áreas de mejora.",
        "Agendé un espacio privado para la conversación.",
        "Preparé preguntas abiertas para escuchar al colaborador.",
        "Definiré acciones, responsables y fechas de seguimiento."
    ]
    respuestas = []
    for elemento in elementos:
        valor = input(f"¿{elemento} (s/n): ").strip().lower()
        respuestas.append(valor in ("s", "si", "sí"))

    completados = sum(respuestas)
    print(f"\nChecklist completado: {completados} de {len(elementos)} puntos.")
    if completados == len(elementos):
        print("¡Estás preparado para realizar la entrevista!")
    else:
        print("Revisa los puntos pendientes antes de realizar la entrevista.")
    print("\nGracias por utilizar el asistente de capacitación.")


def menu():
    puesto = "No especificado"
    while True:
        titulo("Menú principal")
        print("1. Definir el puesto a evaluar")
        print("2. Aprender sobre KPIs, tablero y EPM")
        print("3. Planear una entrevista de retroalimentación")
        print("4. Consejos para una retroalimentación exitosa")
        print("5. Practicar una entrevista")
        print("6. Lista de verificación final")
        print("7. Salir")
        opcion = input("\nSelecciona una opción (1-7): ").strip()

        if opcion == "1":
            puesto = definir_puesto()
        elif opcion == "2":
            explicar_kpis_epm(puesto)
        elif opcion == "3":
            planear_entrevista()
        elif opcion == "4":
            tips_retroalimentacion()
        elif opcion == "5":
            simulacion()
        elif opcion == "6":
            lista_verificacion()
        elif opcion == "7":
            print("\n¡Gracias! Éxito en tu proceso de evaluación.")
            break
        else:
            print("\nOpción no válida. Elige un número del 1 al 7.")


if __name__ == "__main__":
    # Mantiene el tutorial original en consola y habilita la interfaz web cuando
    # Streamlit Cloud usa este archivo como punto de entrada por accidente.
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
    except ImportError:
        get_script_run_ctx = None

    if get_script_run_ctx is not None and get_script_run_ctx(suppress_warning=True) is not None:
        from pathlib import Path
        import runpy
        import streamlit as st

        runpy.run_path(str(Path(__file__).with_name("app.py")), run_name="__main__")
        st.stop()
    else:
        bienvenida()
        menu()
