# Desafio.

nome = 'Devison'
idade = 32
peso = 87
altura = 1.65
ano_atual = 2020
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} e pesa {peso}kg')
print(f'O IMC de {nome} e: {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')
