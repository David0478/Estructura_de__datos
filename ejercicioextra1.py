#hacer un programa que pida un numero comprendido entre 5 y 20, de lo contrario se volvera a pedir.
#el programa mostrara todos los numeros pares que se encuentran entre 0 y el numero que se escribio


pa=0
r="s"
while r=="s" or r=="S":
   
   a=int(input("Ingrese un numero :"))
   if a>=5 and a<=20:
    f=int(a/2)
    for i in range(f):
      pa=pa+2
      print(pa)
    r=input("Quieres seguir?: s/n: ")
    if r=="s" or r=="S":
      pa=0   
   else:
    print("Exsede el limite de 5 a 20")
    r=input("Quieres seguir?: s/n: ")








 