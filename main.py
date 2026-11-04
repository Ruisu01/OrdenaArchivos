from pathlib import Path
import shutil
from sys import path

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

def edicion_nombre(carpeta, nombre):
    stem = Path(nombre).stem
    suffix = Path(nombre).suffix
    destino = carpeta / nombre
    contador = 1
    while destino.exists():
        destino = carpeta / f"{stem}_{contador}{suffix}"
        contador += 1

    return destino

def ordenar(ruta):
    crear_carpetas(ruta)
    for elemento in ruta.iterdir():
        if elemento.is_file():
            categoria = obtener_categoria(elemento)
            destino = edicion_nombre(ruta / categoria, elemento.name)
            shutil.move(elemento, destino)


ordenar(Path("prueba"))
