"""
Desenvolver um validador de CPF

"""

cpf = input('Digite seu CPF: ')
soma = 0
cpf_gerado = cpf[:-2]

for indice, i in enumerate(range(10, 1, -1)):
    soma += int(cpf[indice]) * i
total = 11 - (soma % 11)
digito_1 = 0 if total > 9 else total
cpf_gerado += str(digito_1)

soma = 0

for indice, i in enumerate(range(11, 1, -1)):
    soma += int(cpf[indice]) * i
digito_2 = 11 - (soma % 11)
cpf_gerado += str(digito_2)

if cpf_gerado == cpf:
    print('CPF validado')
else:
    print('CPF invalido')
