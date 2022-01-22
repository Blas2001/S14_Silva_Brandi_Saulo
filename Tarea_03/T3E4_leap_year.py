#Saulo Blas Silva Brandi
#_*_coding: utf8 _*_
def verificador(año, meses, dias):
    #fechas futuras y meses que no existen
    if año > 2021 or meses > 12:
        return False
    
    Porcentaje1 = año % 4
    Porcentaje2 = año % 100
    Porcentaje3 = año % 400

    if meses == 2 and dias <= 29:
        if Porcentaje1 != 0:
            return False
        if Porcentaje1 == 0 and Porcentaje2 != 0:
            return True
        if Porcentaje1 == 0 and Porcentaje2 == 0 and Porcentaje3 != 0:
            return False
        if Porcentaje1 == 0 and Porcentaje2 == 0 and Porcentaje3 == 0:
            return True
   
    if meses == 4 or 6 or 9 or 11:
        if dias > 30:
            return False
        else:
            return True
    

    if meses == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if dias > 31:
            return False
        else:
            return True

if __name__ == '__main__':
    Dia = int(input("Ingrese el dia: "))
    Mes = int(input("Ingrese el mes: "))
    Año = int(input("Ingrese el año: "))

    print("\n", verificador(Año, Mes, Dia))