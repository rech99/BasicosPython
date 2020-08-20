#esto es un comentario
print("Hola Mundo")
print ("Adios Mundo")

#operaicones arimeticas
5+1
print(4+6)
print(5-2)
print(3*4)
print(20/4)
#presedencia de operaciones
print(5+8*(3+2))

#tipos de datos
print(type(2))
print(type(8.62))
print(type("Texto"))
print(type('Texto'))
print(type("5"))

#Variables
mensaje = "Esto es un mensaje"
print (mensaje)
mensaje = "Mensaje modificado"
print (mensaje)
print(type(mensaje))
mensaje = 100
print (mensaje)
print (type(mensaje))

mis3animales ="Perico, gallo, chivo"
print (mis3animales)

tres_animales ="Perico, gallo, chivo"
print (tres_animales)

textoUno = "Mi texto"
textoDos ="Mi segundo texto"

print (textoUno + textoDos)

#str() int() float()
edad = 20
print("La edad del usuario es: " + str(edad))
print("El tipo de dato de edad es:" + str(type(edad)))

import math

grados = 45.0
radianes = grados * math.pi / 180.0
seno = math.sin(radianes)
print("Seno de 45 grados:" + str(seno))

def saludar(nombre):
    print("Holi " + nombre + " Uwu")
    print("¿Como estas? :3")
    print("Te saludo de lejitos, espero estes bien")

def despedir ():
    print("Ya me voy")
    print("Espero estes bien :')")

def concatenar(parte1, parte2):
    return parte1 + parte2

print ("Esto no es parte de la funcion")
saludar("David")
despedir()

frase = concatenar ("Hola", " Adios")
print (frase)