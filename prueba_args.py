import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Prueba de argparse")
parser.add_argument("carpeta")
args = parser.parse_args()
ruta = Path(args.carpeta)
print(type(ruta))

print(args.carpeta)