"""
Operadores relacionais
== igual
> maior que
>= maior igual
< menor que
<= menor igual
!= diferente
"""

valor_1 = 2
valor_2 = 2
print(f'{valor_1} == {valor_2}: {valor_1 == valor_2}')
print(f'{valor_1} > {valor_2}: {valor_1 > valor_2}')
print(f'{valor_1} >= {valor_2}: {valor_1 >= valor_2}')
print(f'{valor_1} < {valor_2}: {valor_1 < valor_2}')
print(f'{valor_1} <= {valor_2}: {valor_1 <= valor_2}')
print(f'{valor_1} != {valor_2}: {valor_1 != valor_2}')
print()

nome = input('Digite o seu nome: ')
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print(f'{nome} e maior de idade')
elif idade > 0:
    print(f'{nome} e menor de idade')
else:
    print("idade invalida")
