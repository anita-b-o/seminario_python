"""ejercicio 7""" 

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

filtro = [str(numero) for numero in numeros if numero % 3 != 0]
cadena = '-'.join(filtro)
print(cadena)
