"""
Split -> Separa uma string e forma uma lista
Join -> Juntar uma lista em uma string
Enumerate -> enumera os indice em uma lista
"""

string = 'O Brasil e penta'
string_split = string.split(' ')
print(string_split)
string_join = ' '.join(string_split)
print(string_join)
for indice, valor in enumerate(string_split):
    print(indice, valor)
