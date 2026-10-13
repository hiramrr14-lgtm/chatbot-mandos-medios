"""Pruebas funcionales de la interfaz Streamlit y del tutorial de consola."""
import subprocess
import sys
from pathlib import Path

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parent

def abrir():
    app = AppTest.from_file(str(ROOT / "chatbot_capacitacion_mandos_medios.py"), default_timeout=15)
    app.run()
    assert not app.exception, [str(error.message) for error in app.exception]
    return app

def pulsar(app, texto):
    encontrado = [b for b in app.button if b.label == texto]
    assert encontrado, f"No aparece botón: {texto}"
    encontrado[0].click().run()
    assert not app.exception, [str(error.message) for error in app.exception]
    return app

def prueba_consola():
    proceso = subprocess.run(
        [sys.executable, str(ROOT / "chatbot_capacitacion_mandos_medios.py")],
        input="\n7\n",
        capture_output=True, text=True, timeout=15,
    )
    assert proceso.returncode == 0, proceso.stderr
    assert "ASISTENTE DE CAPACITACIÓN PARA LÍDERES" in proceso.stdout
    assert "MENÚ PRINCIPAL" in proceso.stdout.upper()

def test_pantalla_inicial_y_tutorial_completo():
    app = abrir()
    assert any("Asistente de capacitación" in t.value for t in app.title)
    pulsar(app, "Comenzar")
    assert any("Definición del puesto" in x.value for x in app.subheader)

    app.text_input[0].set_value("Vendedor")
    pulsar(app, "Guardar")
    assert app.session_state.puesto == "Vendedor"
    pulsar(app, "Continuar")
    assert any("KPIs" in x.value for x in app.subheader)

    app.text_area[0].set_value("Entregas a tiempo, 95%, 88%, octubre")
    pulsar(app, "Registrar datos")
    assert "95%" in app.session_state.kpis
    pulsar(app, "Continuar")

    assert any("entrevista" in x.value.lower() for x in app.subheader)
    pulsar(app, "Continuar")
    assert any("Consejos" in x.value for x in app.subheader)
    pulsar(app, "Practicar")
    assert any("Simulación" in x.value for x in app.subheader)

    app.text_area[0].set_value(
        "La meta era 95%. Gracias por compartirlo. Podemos acordar un plan para mejorar."
    )
    pulsar(app, "Evaluar")
    assert any("3 / 3" in str(x.value) for x in app.metric)
    pulsar(app, "Continuar")

    assert len(app.checkbox) == 7
    for x in app.checkbox:
        x.set_value(True)
    app.run()
    assert any("7 de 7" in str(x.value) for x in app.metric)
    assert not app.exception
    pulsar(app, "Volver al inicio")
    assert any("Asistente de capacitación" in t.value for t in app.title)

def test_simulacion_sin_respuesta_y_navegacion():
    app = abrir()
    app.sidebar.radio[0].set_value("Simulación").run()
    assert not app.exception
    pulsar(app, "Evaluar")
    assert app.warning
    app.sidebar.radio[0].set_value("Lista final").run()
    assert len(app.checkbox) == 7
    assert not app.exception

def test_consola():
    prueba_consola()
