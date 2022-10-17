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
num= 0
'''
1-Insertar contacto
2-Borrar contacto
3-Buscar contacto
4-Ver todos los contactos
5-Salir

    if (num==1):
        print("Insertar contacto")
        telefono= 0
        nombre= 0
        nombre= input("Dime el nombre del contacto")
        telefono= input("Dime el teléfono del contacto")
'''

while (num!=5):
    print("1-Insertar contacto")
    print("2-Borrar contacto")
    print("3-Buscar contacto")
    print("4-Ver todos los contactos")
    print("5-Salir")
    num= (int)(print("Seleccione un número: \n")) 

    try:
        num=(int)(input("Dime un número: \n"))
    except:
        print("Dime un número del 1 al 5")