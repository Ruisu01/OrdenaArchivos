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


print(obtener_categoria(Path("FOTO.JPG")))
print(obtener_categoria(Path("peli.mkv")))
print(obtener_categoria(Path("cosa.xyz")))

