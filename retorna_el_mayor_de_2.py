"""
1- Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def custom_mayor(n1:int, n2:int):
    """Funcion que retorna el mayor de dos numeros.

    Args:
        n1 (int): Primero numero a comparar.
        n2 (int): Segundo numero a comparar.
    """
    resultado = n1 if n1 > n2 else n2
    return resultado