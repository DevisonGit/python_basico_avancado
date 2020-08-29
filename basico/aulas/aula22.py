lista = ['teste', 'a', 1, 2, 3, 4]

n1, n2, *resto = lista
print(n1)
print(n2)
print(resto)

x = 10
y = 'teste'

print(f'x = {x} y = {y}')
x, y = y, x
print(f'x = {x} y = {y}')
