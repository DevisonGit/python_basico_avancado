"""
Imprimir uma saudacao ao usuario de acordo com o horario
0-11 bom dia
12-17 boa tarde
18-23 boa noite
"""

horario = input('Digite o horario: ')

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('O horario deve esta entre 0 e 23')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde')
        elif horario <= 23:
            print('Boa noite')
else:
    print('Horario invalido');