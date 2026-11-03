from pathlib import Path

categorias = {
    "Imagenes": [".jpg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archivos": [".pdf", ".txt", ".rtf"],
    "Roms": [".iso", ".ciso", ".nes"]
}

def obtener_categoria(archivo):
    extension = archivo.suffix.lower()
    for llave, valor in categorias.items():
        if extension in valor:
            return llave
    return "Otros"


carpeta = Path("prueba")

for elemento in carpeta.iterdir():
    if elemento.is_file():
        print(elemento.name + " --> " + obtener_categoria(elemento))

