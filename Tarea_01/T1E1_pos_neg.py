"""
Date:       2022-01-07
Authors:    Saulo Blas Silva Brandi
File:       T1E1_pos_neg.py
Brief:      Ingresar un número y validar
            si es un número positivo, negativo o cero.
Score:      80
Version:    1.1.1
Fixes:      - Falta la condición de __main__

            - PEP8 recomienda que la sangría sea un múltiplo de 4 
                espacio (o una tabulación como les sugerí)

            - PEP8 recomienda no dejar espacio en blanco entre la 
                condición de if y el carácter de dos puntos ':'
                
            - PEP8 recomienda no dejar espacio en blanco después de 
                abrir '(' o antes de cerrar paretesis ')'
"""

# SE RECOMIENDA CASTEAR A FLOAT PARA HACER MÁS VERSATIL EL PROGRAMA
Num = int(input("Escribe un nùmero : " )) 
if Num > 0:
     print("El nùmero es positivo")
elif Num == 0:
    print("El nùmero es cero")
else :
    print("El nùmero es negativo")
