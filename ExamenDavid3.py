
r="s"
while r=="s":
 a=int(input("Ingresa la cantidad de numeros que deseas introducir: "))
 if a>0:
    for i in range(a):
        b=int(input("ingresa un numero mayor a 4: "))
        if b>=4:
          if b%4==0:
            print("YES")
          else:
            print("No")
        else:
            print("Solo numeors mayores a 4")
            print(i)

    r="n"
    print("Gracias por  jugar :D")
 else:
    print("Solo numeros positivos")
    r="s"