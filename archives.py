import os

ruta_dir= os.path.dirname(__file__)
rutaR = os.path.join(ruta_dir,"./archivos/name.txt")

def read():
    names = []
    with open(rutaR, "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0:
                names.append(line.strip())
    if len(names)> 0:
        print(names)
    else:
        print("Archivo vacio")

def write():
    names = []
    with open(rutaR, "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

def add_name(name):
    with open(rutaR, "a" , encoding="utf-8") as f:
        f.write(name)
        f.write("\n")

def delete_name(name):
    names = []
    with open(rutaR, "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0 and line.strip()!= name:
                names.append(line.strip())
    with open(rutaR, "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

    
def run():
    sw = True
    while sw:
        try:
            print("""  
----------------------------------------------------------------------
            Seleccione un numero:
            1. Crear un nuevo archivo 
            2. Agregar nombre
            3. Listar nombre
            4. Borrar nombre
            5. Salir del programa
----------------------------------------------------------------------
            """)
            n = int(input("Ingrese una opcion :   "))
            if n == 1:
                write()
            elif n == 2:
                name = input("Ingrese el nombre a agregar: ")
                add_name(name)
            elif n == 3:
                read()
            elif n == 4:
                name = input("Ingrese el nombre a borrar : ")
                delete_name(name)
            elif n ==5:
                sw = False
                print("Programa Terminado!")
        except ValueError :
                print("Error seleccione una opcion correcta")
    # write()

if __name__ == '__main__':
    run()