def main():
    #escribe tu código abajo de esta línea
    iw=float(input("Dame el peso inicial: "))
    fw=float(input("Dame el peso final: "))
    mn=int(input("Dame la cantidad de meses: "))
    
    l=(iw-fw)/mn
    print("Lo que debes bajar por mes es:",l)

if __name__ == '__main__':
    main()
