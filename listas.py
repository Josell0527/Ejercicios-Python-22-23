#Listas de python, almacenan datos del mismo y distinto tipo
#Definición e iniciación
from operator import truediv


vNombres= []
print(type(vNombres))
vNombres.insert(0,"Juanito")
vNombres.insert(1,"Paco")
vNombres.insert(2,"Inés")
vNombres.append("Minerva") #Introduce al final de la lista
vNombres.insert(1,"Julián")

#Eliminar elementos de la lista
#vNombres.clear()
vNombres.remove("Paco")
#vNombres.pop(1) #pop saca un valor pero lo guarda
print(f"EL nombre borrado es: {vNombres.pop(1)}")

#Ordenar una lista
vNombres.sort(reverse=True) #reverse ordena de mayor a menor

#Contar los elementos de una lista
print(f"Inés aparece:", (vNombres.count("Inés"))) 
print("La lista tiene", len(vNombres)) #len lee los elementos en este caso de vNombres



print (vNombres)

#BUCLE WHILE

i=0
bandera= True

while (bandera == True):
    print("NO hagas esto nunca", i)
    i= i+1
    if (i == 30000):
        bandera= False 
print("Terminado")
