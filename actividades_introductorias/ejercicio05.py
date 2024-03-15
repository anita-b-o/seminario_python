"""ejercicio 5"""

# No me quedó claro cuando cortar la lectura así que me lo inventé sacrificando al cero

numeros = []
while True:
    try:
        numero = int(input('''Ingrese un numero para agregar a la lista
(finaliza al ingresar 0): '''))
        if numero == 0:
            break
        numeros.append(numero)
    except ValueError:
        print('~~~No se ha ingresado un numero. Intentalo de nuevo')
for numero in numeros:
    if numero < 0:
        break
    print(numero)
