#Saulo Blas Silva Brandi
#_*_coding: utf8 _*_
from random import choice

def seleccion_usuario():
    try:
        list1 = ["piedra", "papel", "tijera"]
        su = int(input("Elija: \n 0 para piedra \n 1 para papel \n 2 para tijera:\n"))
        su = list1[su]
        return su
        
    except:
        print("ingresa un número entre 0, 1 y 2")
    

def seleccion_pc():= ["piedra", "papel", "tijera"]
    sp = choice(list1)
    return sp

def partida(sel1, sel2):
    if sel1 == sel2:
        result = "Empate"
        return result
    if sel1 == "piedra" and sel2 == "papel":
        result = "Pierdes"
        return result
    elif sel1 == "piedra" and sel2 == "tijera":
        result = "Ganas"
        return result
    if sel1 == "papel" and sel2 == "tijera":
        result = "Pierdes"
        return result
    elif sel1 == "papel" and sel2 == "piedra":
        result = "Ganas"
        return result
    if sel1 == "tijera" and sel2 == "piedra":
        result = "Pierdes"
        return result
    elif sel1 == "tijera" and sel2 == "papel":
        result = "Ganas"
        return result