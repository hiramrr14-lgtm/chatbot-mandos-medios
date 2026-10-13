# Chatbot de capacitación para mandos medios

Asistente educativo para preparar evaluaciones del desempeño de colaboradores. Explica cómo definir un puesto, revisar KPIs, reunir evidencia mediante EPM, planear una entrevista y practicar retroalimentación.

## Contenido

- `chatbot_capacitacion_mandos_medios.py`: programa **original de consola** (sin librerías externas).
- `app.py`: adaptación con interfaz web interactiva, realizada con Streamlit.
- `requirements.txt`: dependencia para desplegar la versión web.

> **Nota:** Este chatbot es un tutorial guiado y una simulación basada en palabras clave; no utiliza un modelo de IA generativa. EPM es usado como evaluación del desempeño mediante evidencia, siguiendo el texto del material original.

## Ejecutar el programa original

Con Python 3 instalado:

```bash
python chatbot_capacitacion_mandos_medios.py
```

La aplicación pedirá respuestas mediante la terminal.

## Ejecutar la versión web en tu computadora

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Abre en tu navegador la dirección local que indique Streamlit (normalmente `http://localhost:8501`).

## Código en GitHub

Este repositorio contiene el código original y la versión web. Para modificarlo, crea un commit con los cambios.

## Publicar la web con Streamlit Community Cloud

1. Ve a https://share.streamlit.io e inicia sesión con GitHub.
2. Selecciona **Create app** y el repositorio donde subiste el código.
3. Selecciona la rama `main` y configura **Main file path** como `app.py`.
4. Haz clic en **Deploy**.
5. Cuando finalice, tendrás un enlace `https://...streamlit.app` para abrirlo desde el navegador.

Consulta la documentación oficial: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Probar la versión de consola sin instalar nada

En GitHub, abre el repositorio y haz clic en **Code > Codespaces > Create codespace on main**. Abre una terminal en ese Codespace y ejecuta:

```bash
python chatbot_capacitacion_mandos_medios.py
```

El Codespace tiene sus propios límites de consumo.

## Privacidad

La versión web guarda temporalmente información en la sesión del navegador; no está diseñada para almacenar datos confidenciales de empleados ni para usarse como un sistema de RH en producción.
