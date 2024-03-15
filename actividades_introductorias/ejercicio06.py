"""ejericio 6"""

lista = [1, 2, 3, 4, 9, 8, 7, 6, 5]
lista_impares = []
lista_pares = []
for numero in lista:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print('Imprimiendo lista de pares')
for par in lista_pares:
    print(par)
print('Imprimiendo lista de impares')
for impar in lista_impares:
    print(impar)
