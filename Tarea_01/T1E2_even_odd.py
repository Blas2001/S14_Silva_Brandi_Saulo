"""
Date:       2022-01-07
Authors:    Saulo Blas Silva Brandi
File:       T1E2_even_odd.py
Brief:      Ingresar un número y validar si es par o impar.
Score:      90
Versión:    1.1.1
Fixes:      - Falta la condición de __main__
            
            - PEP8 recomienda añadir espacios en blanco alrededor de
                los operadores
"""

# SERIA BUENO AGREGAR UNA INDICACIÓN CUANDO EL RESULTADO ES CERO
Num = int(input("Escribe un nùmero : "))
if Num %2 == 0:
    print("Numero par")
else:
    print("Numero impar")
