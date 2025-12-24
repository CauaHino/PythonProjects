# 📂 Organizador Automático de Carpetas

Este es un script de Python sencillo pero potente que ayuda a mantener tu carpeta de descargas (o cualquier otra) limpia y organizada. Clasifica los archivos automáticamente en carpetas según su extensión.

## 🚀 ¿Cómo funciona?

El script escanea los archivos de una ruta específica y los mueve a subcarpetas categorizadas:
- **Imágenes:** .jpg, .jpeg, .png, .gif
- **Documentos:** .pdf, .docx, .txt, .xlsx
- **Videos:** .mp4, .mov, .avi
- **Instaladores:** .exe, .dmg, .pkg

## 🛠️ Requisitos

- **Python 3.x** instalado.
- No requiere librerías externas (utiliza `os` y `shutil` que vienen integradas).

## 📋 Uso

1. Clona este repositorio o descarga el archivo `organizador.py`.
2. Abre el archivo y modifica la variable `ruta_origen` con la dirección de la carpeta que deseas organizar:
   ```python
   ruta_origen = '/Tu/Ruta/Aqui'

