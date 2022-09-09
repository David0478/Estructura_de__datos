from curses.ascii import isdigit


arr=[0,0]
po=0

def validarNumeros(a):
     c = 0
     x = 0
     for i in a:
         if isdigit(a[x]) and int(a)<50:
          c+=1  
     
         x += 1
     if c == len(a):
         return True
     else:
         return False
         c= c-1

res = "s"
np=0
ni=0
while res == "S" or res == "s" and po<len(arr):
        a = input("Ingrese un valor: ")
        if validarNumeros(a):
            a=str(a)
            arr[po]=int(a)
            po +=1    
        else:
           print("Error solo se permiten numeros, o numeros mayores de 50")
        if po<len(arr):
             res = input("Deseas otro valor s/n \n")

        
        
        
        
for x in arr:
     if x != 0 and x<50:
        print(x," ")
        if x%2==0:
          np+=1

        if x%2!=0:
         ni+=1


     
print("numeros impares : ",ni)
print("numeros pares: ",np)
