def main():
    #escribe tu código abajo de esta línea
    n=int(input("Dame el año de nacimiento: "))
    a=int(input("Dame el año actual: "))
    e=a-n
    l=e/5
    print("Los lustros que has vivido son:",l)

if __name__ == '__main__':
    main()
