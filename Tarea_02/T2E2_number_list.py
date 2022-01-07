"""Crear una lista con n números desde el teclado, después realizar los siguientes
pasos (comentar el número y nombre del paso) e imprimir la lista en cada paso:"""
#Saulo Blas Silva Brandi

#Creamos lista
Numeros = ["1","2","3","4","5"]
print(Numeros) #Imprimo lista
print(type(Numeros)) #Observamos que tipo es "Numeros"
Numeros = list(map(int,Numeros)) #Convertimos str a int
print(Numeros)
print("A continuacion digite el intervalo de la lista que desea ver")
inicio = int(input("Escriba el inicio de la lista : "))
final = int(input("Escriba el final de la lista : "))
print(Numeros[inicio:final])#imprimir elementos elegidos
print(Numeros.sort()) #ordenamos elementos
print(Numeros.sort(reverse=True)) #Elementos en reversa