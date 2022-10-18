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
#Función que pinta el menú y devuelve la opción seleccionada del 1 al 5
def pintaMenu():
    num= 0
    while (num< 1 or num >5 ):
        print("**********MENÚ AGENDA*********")
        print("1-Insertar contacto")
        print("2-Borrar contacto")
        print("3-Buscar contacto")
        print("4-Ver todos los contactos")
        print("5-Salir")

        try:
            num=(int)(input("Dime un número: \n"))
        except:
            print("Dime un número del 1 al 5")

    return num  
print("Has seleccionado", pintaMenu())      

num= pintaMenu()