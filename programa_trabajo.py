#hacer un programa que lea nombre edad y sexo de 10 personas, el programa mostrara
#cuantos hombres mayores de edad,menores, y mujeres mayores y menores hay.
#b=int(input("ingrese su edad"))
#c=input("ingrese su sexo, M o F")


cMM= 0
cMF= 0
cmF= 0
cmm= 0
for i in range(10):
 a=input("ingrese su nombre: ")
 b=int(input("ingrese su edad: "))
 c=input ("ingrese su sexo, M o F :" )
 if b >= 18 and c=='M':
    cMM+=1
 if b<18 and c=='M':
    cmm+=1
 if b >= 18 and c=='F':
    cMF+=1
 if b<18 and c=='F':
    cmF+=1

print("La cantidad de hombres mayores es de :",cMM," ","Y la cantidad de hombres menores es de :",cmm)
print("La cantidad de Mujeres mayores es de :",cMF," ","Y la cantidad de mujeres menores es de :",cmF)    
