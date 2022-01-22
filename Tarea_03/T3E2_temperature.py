#Saulo Blas Silva Brandi
def celsius():
    Fahrenheit = float(input("Introduce ºF : "))
    Celsius = (Fahrenheit-32)*5/9
    return Celsius

def fahrenheit():
    Celsius = float(input("Introduce ºC : "))
    Fahrenheit = (Celsius*9/5)+32
    return Fahrenheit
if __name__=='__main__':
    print("De ºF a ºC ",celsius())
    print("De ºC a ºF ",fahrenheit())