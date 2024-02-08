"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

"""

def  es_vocal(caracter):
    return True if caracter.lower() in ['a', 'e', 'i', 'o', 'u'] else False

print(es_vocal('O')) 