#Arreglos se llaman List en python

animales = ["perro", "gato"]
print(animales)

############################################################## APPEND
animales.append("vaca")
animales.append("loro")
animales.append("leon")
print(animales)

############################################################## INDEX
print(animales.index("gato")) #imprime donde está "gato"

############################################################## INSERT
animales.insert(1,"tigre") #inserta tigre en posición de gato desplaza toda la lista
print(animales)

############################################################## SLICE
print(animales[0:3]) #apunta a los terminos 0,1,2
print(animales[1:]) #imprime los terminos de 1 hasta el final
print(animales[:3]) #imprim los terminos desde el inicio hasta el 2

############################################################## SORT
numeros = [3,2,5,1,9,8]
print(numeros)
numeros.sort()  #ordena numeros
print(numeros)
