def main():
    #escribe tu código abajo de esta línea
    
    #this program can solve basic mathematic problems

    num1=int(input("Dame un número: ")) #Reads the first number
    num2=int(input("Dame un número: ")) #Reads the second number

    #Solves the calculations
    suma= num1+num2
    sub= num1-num2
    mult= num1*num2

    #Shows the answers
    print("Suma:", suma)
    print("Resta:", sub)
    print("Multiplicación:", mult)


if __name__ == '__main__':
    main()
