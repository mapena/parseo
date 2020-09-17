


def abrirarchivo():
    try:
        print("abrir archvo")
        f = open("c:\\Users\mp\Desktop\dormant.txt", "r")
    except IOError:
        print("No existe archivo")
       # raise si se habilita la sentencia raise el programa cancela
    return


if __name__ == "__main__":
    abrirarchivo()
