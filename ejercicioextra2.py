#hacer un programa que lea una cadena donde la cadena representara la cantidad de numeros
#impares que se deben de leer, si no se introduce numeros impares se pedira el numero, al final mostrara
#suma y promedio de los numeros introducidos


a=input(" ingresa una cadena paps: ")
f=len(a)
ar=[f]
aux=0
c=0

while c<=f:
 for i in range(f):
   b=int(input("Ingresa un numero impar: "))
   if b%2!=0:
      aux=aux+b#aqui estoy sumando los datos consecutivamente
      c+=1

   else:
      print("solo numeros pares bb")
      

      

b=aux/f
print("La suma de los numeros es de : ",aux)
print("El promedio es de: ",b)


