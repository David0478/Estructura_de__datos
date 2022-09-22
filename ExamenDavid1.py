
aux=0
r="s"
while r=="s"or r=="S":
 for c in range(12):
   b=float(input("Ingresa el saldo de larry: "))
   if b>0:
      aux=aux+b
   else:
     print("Solo numeros  positivos")
     

 f=aux/12
 print("suma es de: ",aux)
 print("El promedio de los saldos de larry es de : ","$ ",f)
 r=input("Quieres seguir jugando? s/n: ")





   
