from pathlib import Path
import shutil

categorias = {
    "Imagenes": [".jpg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archivos": [".pdf", ".txt", ".rtf"],
    "Roms": [".iso", ".ciso", ".nes"],
    "Otros": []
}

def obtener_categoria(archivo):
    extension = archivo.suffix.lower()
    for llave, valor in categorias.items():
        if extension in valor:
            return llave
    return "Otros"


def crear_carpetas(ruta):
    for llave, valor in categorias.items():
        nombre_carpetas = llave
        Path(ruta / nombre_carpetas).mkdir(exist_ok=True)


def ordenar(ruta):
    crear_carpetas(ruta)
    for elemento in ruta.iterdir():
        if elemento.is_file():
            categoria = obtener_categoria(elemento)
            destino = ruta / categoria / elemento.name
            shutil.move(elemento, destino)


ordenar(Path("prueba"))


