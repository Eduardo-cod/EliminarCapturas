# Eliminar Capturas

Una herramienta sencilla y eficiente desarrollada en Python para gestionar la limpieza automatizada de directorios de capturas de pantalla (`Screenshots`) en sistemas Linux y entornos de escritorio comunes. El script cuenta con validaciones de seguridad para evitar la eliminación accidental de archivos.

## 🚀 Características

- 🔍 **Validación de Rutas:** Verifica automáticamente si el directorio de capturas existe antes de realizar cualquier acción.
- 🌐 **Soporte Multi-idioma (Sistemas OS):** Incluye opciones configurables por el usuario para adaptarse a la estructura de carpetas en sistemas en español o inglés.
- ⚠️ **Confirmación de Seguridad:** Implementa un paso de interacción humana que solicita confirmación expresa (`s/n`) antes de proceder con el borrado.
- 🛡️ **Cancelación Segura:** Permite abortar la operación de forma inmediata sin alterar ningún archivo si el usuario no confirma la acción.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.10+
- **Librerías Core:** `pathlib` (módulo nativo para la manipulación intuitiva de rutas de archivos).

## 📦 Instalación y Configuración

1. **Clona este repositorio o descarga el script en tu máquina local:**
```bash
   git clone [https://github.com/Eduardo-cod/EliminarCapturas.git](https://github.com/Eduardo-cod/EliminarCapturas.git)
   cd EliminarCapturas
