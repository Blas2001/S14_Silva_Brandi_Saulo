"""
Date:     2022-01-07
Authors:  Saulo Blas Silva Brandi
File:     T1E3_birthday.py
Brief:    Este programa solicita año, mes y día de cumpleaños 
          e implime el string 'Year:xxxx - Month:xx - Day: xx'
          con sus respectivos resultados
Score:    80
Version:  1.1.1
Fixes:    - Falta la condición de __main__
          
          - PEP8 recomienda no dejar espacio en blanco después de 
                abrir '(' o antes de cerrar paretesis ')'
             
          - PEP8 recomienda añadir un espacio en blanco después del
                carácter de coma ','    
"""

Year = int(input("Año de nacimiento : "))
Month = int(input("Mes de nacimiento en nùmero : "))
Day = int(input("Dìa de nacimiento : "))

print("Year: ", Year," - Month: ",Month, " - Day: ", Day )
