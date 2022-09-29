"""
Crear un programa que, ingresada una palabra, muestre como salida:
1. El número de apariciones de cada letra en la palabra.
2. Ordene alfabéticamente todas las letras de la palabra.
Ejemplo: Amarillo → [a -> 2, m -> 1, r -> 1, i -> 1, l -> 2, o -> 1] [aaillmor]
"""
from typing import Counter
"""def contador(word):
    #funcion que cuenta las apariciones de cada letra y las pone en un diccionario
    return {letter : word.count(letter) for letter in word}"""

print("ingrese una palabra")
palabra = input().lower()
print (Counter(palabra))
#imprime en orden alfabetico todas las letras de la palabra
print (sorted(palabra))