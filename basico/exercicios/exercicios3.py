"""
Fazer um programa que receba um nome e valide se:
<= 4 printar Seu nome e curto
5 ou 6 printar Seu nome e normal
> 6 printar Seu nome e muito grande
"""

nome = input('Digite se nome: ')
tamanho_nome = len(nome)

if tamanho_nome == 0 :
    print('Digite algo')
else:
    if tamanho_nome <= 4:
        print('Seu nome e curto')
    elif len(nome) <= 6:
        print('Seu nome e normal')
    elif len(nome) > 6:
        print('Seu nome e muito grande')

