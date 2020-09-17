from sys import argv

def abrir_archivo(archid, origen):
    try:
        if archid == "entrada":
            global arch_entrada
            arch_entrada = open(origen, "r")
#           arch_entrada = open("c:\\Users\mp\Desktop\dormant.txt", "r")
        else:
            global arch_salida
            arch_salida = open(origen, "w")
#            arch_salida = open("c:\\Users\mp\Desktop\salida.txt", "w")
    except IOError:
        print("No se pudo abrir el  archivo: " + archid.name)
       # raise si se habilita la sentencia raise el programa cancela
    return

def cerrar_archivo(archid):
    try:
        archid.close()
    except IOError:
        print("Error cerrar archivo:", archid.name)
       # raise si se habilita la sentencia raise el programa cancela
    return

def leer_archivo(archid):
    global contenido
    contenido = archid.readlines()  # se genera una lista
    return


def grabar_archivo(archid, registro):
    try:
        archid.write(registro)
    except IOError:
        print("Error de grabacion archivo salida")
       # raise si se habilita la sentencia raise el programa cancela
    return


def procesar_salida():
    for x in contenido:
        reg = x.split(",")
        salida = reg[2] + "," + reg[3] + "\n"
        grabar_archivo(arch_salida, salida)

    return


if __name__ == "__main__":
    script, fentrada, fsalida = argv
    print("archivo de entrada:", fentrada)
    print("archivo de salida:", fsalida)
    abrir_archivo("entrada", fentrada)
    abrir_archivo("salida", fsalida)
    leer_archivo(arch_entrada)
    procesar_salida()
    cerrar_archivo(arch_entrada)
    cerrar_archivo(arch_salida)
