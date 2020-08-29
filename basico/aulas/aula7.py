"""
Formatando string
"""

nome = 'Devison'
idade = 32
altura = 1.65
e_maior = idade > 18
peso = 87

# Desafio da aula
imc = peso / (altura * altura)
print(nome, ' tem', idade, ' de idade e seu IMC e ', imc)
print(f'{nome} tem {idade} de idade e seu IMC e {imc:.2f}')
print('{} tem {} de idade e seu IMC e {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} de idade e seu IMC e {im:.2f}'.format(n=nome, i=idade, im=imc))
