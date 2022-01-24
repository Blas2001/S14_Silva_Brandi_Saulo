"""
Date:       2022-01-07
Authors:    Saulo Blas Silva Brandi
File:       
Brief:      
Score:      80 (15)
Version:    1.1.1
Fixes:      - Falto el encabezado (docstring)
            
            - PEP8 recomienda añadir un espacio en blanco después del
                carácter de almohadilla '#' de los comentarios
            
            - Falta la condición de if __name__ == "__main__":
            
            - PEP8 recomienda añadir espacios en blanco alrededor de
                los operadores, excepto en los paramétros
            
            - PEP8 recomienda añadir un espacio en blanco después del
                carácter de coma ','
"""
"""Crear una lista de n elementos de texto (strings) predefinidos, después realizar los
siguientes pasos (comentar el número y nombre del paso) e imprimir la lista en
cada paso: """
#Saulo Blas Silva Brandi
#Creamos lista
Numeros = ["uno","dos","tres","cuatro","cinco"]
Numeros.append("Seis") #Agregamos el str a la lista
print(Numeros)
Numeros.insert(4,"Siete") #Insertamos un str
print(Numeros)
Numeros.pop(1) #Borramos un str
print(Numeros)
Numeros.sort() #Ordenamos de A-Z
print(Numeros)
Numeros.sort(reverse = True) #Ordenamos de Z - A
print(Numeros)
