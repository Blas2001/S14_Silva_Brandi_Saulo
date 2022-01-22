#Saulo Blas Silva Brandi
def suma():
    Suma = Num1 + Num2
    return Suma
def resta():
    Resta = Num1 - Num2
    return Resta
def multiplicacion():
    Multiplicacion = Num1 * Num2
    return Multiplicacion
def divicion():
    Divicion = Num1 / Num2
    return Divicion
if __name__=='__main__':
    Num1 = 4
    Num2 = 6
    print(Num1 , " + ", Num2 ," = ",suma(),"\n")
    print(Num1 , " - ", Num2 ," = ",resta(),"\n")
    print(Num1 , " * ", Num2 ," = ",multiplicacion(),"\n")
    print(Num1 , " / ", Num2 ," = ",divicion(),"\n")