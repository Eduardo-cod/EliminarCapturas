from pathlib import Path

class EliminarCapturas:

    def eliminar_capturas():
        # 1. Definir la ruta de la carpeta.
        # Elige la que corresponda a tu sistema (comenta/descomenta según sea el caso)

        # Opción A: Sistema en español (ej. GNOME/Ubuntu)
        ruta_capturas = Path.home() / "Pictures" / "Screenshots"

        # Opción B: Sistema en inglés
        # ruta_capturas = Path.home() / "Pictures" / "Screenshots"

        # Verificar si la carpeta realmente existe
        if not ruta_capturas.exists():
            print(f"❌ La carpeta no existe en la ruta: {ruta_capturas}")
            print("Por favor, edita el script con la ruta correcta de tu sistema.")
            return

        # 2. Advertencia y confirmación de seguridad
        print(f"⚠️ ¡Atención! Se eliminarán TODOS los archivos en: {ruta_capturas}")
        confirmacion = input("¿Estás seguro de que deseas continuar? (s/n): ").strip().lower()

        if confirmacion != 's':
            print("❌ Operación cancelada por el usuario.")
            return

        # 3. Proceso de eliminación
        contador_eliminados = 0

        for elemento in ruta_capturas.iterdir():
            # Nos aseguramos de borrar solo archivos (no carpetas)
            if elemento.is_file():
                try:
                    elemento.unlink()  # Borra el archivo de forma permanente
                    print(f"Eliminado: {elemento.name}")
                    contador_eliminados += 1
                except Exception as e:
                    print(f"No se pudo eliminar {elemento.name}. Error: {e}")

        print(f"\n✨ ¡Listo! Se eliminaron {contador_eliminados} archivos.")

def main():
    EliminarCapturas.eliminar_capturas()

if __name__ == "__main__":
    main()
