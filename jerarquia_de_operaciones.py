# Programa que hace formula general positiva
from re import X


a=float(input("Escribe un numero"))
b=float(input("Escribe un numero"))
c=float(input("Escribe un numero"))

x=b**2
y=float(4*a*c)
if x<y:
    print("La  ecuacion no tiene solucion con numeros reales")

else:
    D=float (-1)*(b)
    A=float(x-y)
    I= A**(1/2)
    V=float (2*a)
    pos= (D+I)/V
    neg= (D-I)/V
    input(D)
    input("x1 es igual a : "+str(pos))
    input("x2 es igual a :"+str(neg))

