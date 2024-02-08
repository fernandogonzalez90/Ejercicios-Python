"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""

from retorna_el_mayor_de_2 import custom_mayor

def max_de_tres(n1:int, n2:int, n3:int):
    """Funcion que retorna el mayor de 3 numeros

    Args:
        n1 (int): Primer Numero a comparar
        n2 (int): Segundo Numero a comparar
        n3 (int): Tercer Numero a comparar
    """

    return custom_mayor(custom_mayor(n1,n2), n3)

print(max_de_tres(5,80,10))