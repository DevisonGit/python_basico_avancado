"""
Listas em python pode armazenar diverso valores
append, pop, max, mix
"""

lista_numeros = [1, 2, 3, 4, 5, 6]
print(f'lista de numero: {lista_numeros}')
lista_numeros.append(7)
print(f'adicionado mais um numero: {lista_numeros}')
print(f'Menor da lista: {min(lista_numeros)}')
print(f'Maior da lista: {max(lista_numeros)}')
print(f'Removendo: {lista_numeros.pop(5)}')
print(f'lista de numero: {lista_numeros}')
lista_numeros.insert(0,'inicio')
print(f'lista de numero: {lista_numeros}')
del(lista_numeros[0])
print(f'lista de numero: {lista_numeros}')

lista_letras_1 = ['a', 'b', 'c']
lista_letras_2 = ['d', 'e', 'f']
print(f'{max(lista_letras_1)}')
lista_letras_3 = lista_letras_1 + lista_letras_2
print(f'lista de letras unidas +: {lista_letras_3}')
lista_letras_1.extend(lista_letras_2)
print(f'lista de letras unidas extend: {lista_letras_1}')
