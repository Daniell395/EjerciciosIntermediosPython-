import os

ruta_dir= os.path.dirname(__file__)
rutaR = os.path.join(ruta_dir,"./archivos/data.txt")

def read():
    words = []
    with open(rutaR, "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0:
                words.append(line.strip())
    if len(words)> 0:
        print(words)
    else:
        print("Archivo vacio")

def run():
    try:
        print(0)
    except print(0):
        pass


if __name__ == '__main__':
  run()