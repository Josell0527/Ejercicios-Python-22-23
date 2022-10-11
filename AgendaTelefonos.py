''' 
Opción 1:
LIstas para nombres 
Listas para telefonos

Opción 2:
Listas para nombres y telefonos
Ejemplo [Juan-Teléfono, Pepe-Teléfono]
'''

#Opción 1:

vNombres= []
vTelefonos= []
Nombres= input("Dime un nombre:")
Telefonos= input("Dime el teléfono de dicho nombre:")

vNombres.append(Nombres)
#vNombres.append(input("Dime un nombre:")) OTRA FORMA
vTelefonos.append(Telefonos)

print("El telefono de", (vNombres), "es", (vTelefonos))