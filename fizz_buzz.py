numeros = list(range(1, 101))

for numero in numeros:
    if numero % 3 == 0 and numero % 5 == 0:
        print(f'El numero es: {numero} y es fizzbuzz')
    elif numero % 5 == 0:
        print(f'El numero es: {numero} y es buzz')
    elif numero % 3 == 0:
        print(f'El numero es: {numero} y es fizz')