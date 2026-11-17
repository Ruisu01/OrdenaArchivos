# Ordenador de archivos

Ordenador es un script en Python que ordena los archivos de una carpeta en subcarpetas según su tipo (imágenes, videos, documentos, etc.).

## Qué hace

- Clasifica cada archivo por su extensión (`.JPG` y `.jpg` van al mismo lugar).
- Si ya existe un archivo con el mismo nombre, renombra el nuevo (`foto_1.jpg`).
- Tiene un modo de simulación (`--simular`) que muestra qué se movería antes de la ejecución final.

## Requisitos

- Python 3.9 o superior
- Probado en CachyOS (basado en Arch Linux). No probado en otros sistemas.

## Uso

```bash
python ordenar.py <carpeta> --simular   # muestra qué haría, sin mover nada (recomendado antes de ejecutar)
python ordenar.py <carpeta>             # ordena de verdad
python ordenar.py --help
```

> **Atención:** el programa no tiene opción de deshacer. Siempre realizar una simulación antes.