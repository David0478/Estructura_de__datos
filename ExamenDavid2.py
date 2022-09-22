

r="s"
while r=="s" or r=="S":
 a=int(input("Ingresa un numero: "))
 b=int(input("Ingresa otro numero: "))
 c=int(input("Ingresa otro numero: "))
 ab=(a**2)+(b**2)
 if ab==(c**2):
    print("correcto")
    r=input("Quieres seguir? s/n: ")
 else:
    print("Incorrecto")
    r=input("Quieres seguir? s/n: ")