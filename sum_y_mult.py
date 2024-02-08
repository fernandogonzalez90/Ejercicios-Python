"""
5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

from functools import reduce

def max_and_sum(lista:list):
    suma = reduce(lambda x, y: x + y, lista)
    multi = reduce(lambda x, y: x * y, lista)
    return f'El resltado de la suma es: {suma} \nEl resultado de la multiplicación es: {multi}'

print(max_and_sum([1,2,3]))
