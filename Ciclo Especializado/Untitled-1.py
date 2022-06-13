# String - Cadena de Texto
from ctypes.wintypes import INT
from tokenize import Name


name = input("Indica tu nombre:")
print(f"Hola,{name}")

# Int - Enteros - Números sin punto decimal
Edad = input("Cual es tu edad?")
Edad = int(Edad)
# Float - Flotante - Números con punto decimal
pi = 3.1416

# Costeo -Transformar un tipo de variable a otro
Edad = float(Edad)

#Type() - Sirve para conocer el tipo de variable que es
print(type(Name), type(Edad))

#Bool - Booleano - Si o No
Verdad= False

#Condicional
##Preguntamos la Edad
##And Todos lo valores son verdaderos
##Or Al menos un valor es verdadero
if Edad >= 18 and Edad <= 30: ##Si el valor es mayor de 18 puedes pasar
    print("U can go in")
    ##Si no el if pasara a esta linea 
elif Edad > 31:
    print("WTF?")
else: print("U have to stay out")

##Markdown - Documentacion