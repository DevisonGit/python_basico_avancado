"""
Operadores Logicos
and -> e -> todas expressoes precisam ser verdadeiras
or -> ou -> ao menos uma expressao precisa ser verdadeira
not -> nao -> inverte o valor da expressao
in -> contem dentro -> pegunta se o valor existe dentro
not in -> nao contem dentro -> pergunta se o valor nao existe
"""


print('Tabela Verdade\n')
print('And')
print('True and True: ', True and True)
print('True and False:', True and False)
print('False and True:', False and True)
print('False and False:', False and False)
print()
print('Or')
print('True or True: ', True or True)
print('True or False:', True or False)
print('False or True:', False or True)
print('False or False:', False or False)
print()
print('Not')
print('not True', not True)
print('not False', not False)
print()
nome = 'Devison'
if 'D' in nome:
    print(f'Contem D no {nome}')
print()
if 'E' not in nome:
    print(f'Nao contem E no {nome}')
