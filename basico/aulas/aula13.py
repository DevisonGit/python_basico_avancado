usuario = input('Digite seu nome de usuario: ')
qtd_char = len(usuario)

print(f'O Usuario {usuario} tem {qtd_char} caracteres')

if qtd_char < 6:
    print('Usuario tem que ter ao menos 6 caracteres')
else:
    print(f'Usuario {usuario} cadastrado')
