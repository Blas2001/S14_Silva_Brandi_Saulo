"""
Date:       2022-01-07
Authors:    Saulo Blas Silva Brandi
File:       
Brief:      
Score:      80 (65)
Version:    0.1.1
Fixes:      - Falto el encabezado (docstring)
            
            - PEP8 recomienda añadir un espacio en blanco después del
                carácter de almohadilla '#' de los comentarios
            
            - Falta la condición de if __name__ == "__main__":
            
            - PEP8 recomienda añadir un espacio en blanco después del
                carácter de coma ','
"""

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

# ESTAS LINEAS NO FUNCIONARON PORQUE EL METODO SE DEBE EFECTUAR
# Y DESPUES SE DEBE HACER EL PRINT DE LA LISTA (SOLO Numeros)
# REALMENTE LO QUE ESTAS IMPRIMIENDO ES EL RETORNO DEL METODO
# EL CUAL ES "NONE" DE QUE NO HUBO NINGUN PROBLEMA
print(Numeros.sort()) #ordenamos elementos
print(Numeros.sort(reverse=True)) #Elementos en reversa
