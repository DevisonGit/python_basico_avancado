"""
Variaveis, para nomear se deve iniciar com letras, pode conter numeros, separar com _, letras minusculas
"""

nome = 'Devison'
idade = 32
altura = 1.65
e_maior = idade > 18
peso = 60.0

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('E Maior: ', e_maior)
print()

# Desafio da aula
imc = peso / (altura * altura)
print(nome, ' tem ', idade, ' de idade e seu IMC e ', imc)
