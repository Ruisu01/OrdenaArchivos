import argparse
from pathlib import Path
import shutil

categorias = {
      "Imagenes": [".jpg", ".jpeg", ".png",
    ".gif", ".webp", ".bmp",
    ".tiff", ".svg", ".ico"
  ],

      "Video": [".mp4", ".mkv", ".avi",
    ".mov", ".wmv", ".flv",
    ".webm", ".mpeg", ".3gp"
  ],

    "Documentos": [".pdf", ".doc", ".docx",
        ".odt", ".rtf", ".txt",
        ".epub", ".md"
    ],

    "Audio": [".mp3", ".wav", ".flac",
        ".ogg", ".aac", ".m4a",
        ".wma", ".mid"
    ],

    "Otros": [],

    "Hojas_calculo": [".xls", ".xlsx",
        ".ods", ".csv"
    ],

    "Ejecutables": [".exe", ".msi", ".bat",
    ".cmd", ".sh", ".apk",
    ".appimage"
    ],

    "Codigo_fuente": [".c", ".cpp", ".h",
        ".hpp", ".py", ".java",
        ".js", ".ts", ".html",
        ".css", ".php", ".go",
        ".rs"
    ],

    "Bases_de_datos": [".db", ".sqlite", ".sqlite3",
        ".mdb", ".accdb"
    ],

    "Presentaciones": [".ppt", ".pptx", ".odp"
    ],

    "Comprimidos": [".zip", ".rar", ".7z",
        ".tar", ".gz", ".bz2",
        ".xz"
    ],
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


parser = argparse.ArgumentParser(description="Ordena los archivos de una carpeta por categoría")
parser.add_argument("carpeta")
args = parser.parse_args()

ruta = Path(args.carpeta)
ordenar(ruta)