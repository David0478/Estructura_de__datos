from curses.ascii import isdigit


def validarletras(a):
    for i in a:
     if a.isdigit(i):  
        print("Es una letra")
     else:
         print("No es caracte")    #analiza cada digito y si no es alfanumerico retorna a falso

a= input("Escribe un nombre")
validarletras(a)

'''
cadenadetexto="Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no."
print (cadenadetexto.find("quien"))
print (cadenadetexto.rfind("quien"))

print(":".join(["freeCodeCamp", "es", "divertido"]))
print(" y ".join(["A", "B", "C"]))

string = "Esto es bonito. Esto es bueno."
newString = string.replace("es","FUE")
print(newString) '''