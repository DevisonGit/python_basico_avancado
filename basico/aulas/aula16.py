"""
Formatando valores
:.(numero)f - Define quantidade casa no float
:(caracter)(< > ^)(quantidade)
> esquerda
< direita
^ centro
"""

numero = 2.0
print(f'Original {numero} Formatado {numero:.2f}')

nome = 'Davi'
print(f'{nome:*>10}')
print(f'{nome:*<10}')
print(f'{nome:*^10}')
