"""
Tipos de dados
str -> String -> textos 'Assim' ou "Assim"
int -> Inteiro -> 123 1 100 1569874 -200 -12
float -> Real/Ponto Flutuante -> 1.0 5623.0 -56.6 -12.36
bool -> Booleano/Logico -> True/False 10==10
"""

print('devison', type('Devison'))  # Funcao type retorna o tipo do parametro passado.
print(10, type(10))
print(10.0, type(10.0))
print(True, type(True))
print()
"""
Casting 
str()
int()
float()
bool()
"""

print(type(int('12')))
print(type(bool('')))
print()
# Desafio da Aula

# Nome: string
print('Devison', type('Devison'))
# Idade: int
print(32, type(32))
# Altura: float
print(1.65, type(1.65))
# E maior de idade: boolean
print(32 > 18, type(32 > 18))
