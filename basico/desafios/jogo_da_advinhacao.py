"""
Jogo da Adivinhacao
Acertar a palavra secreta com 3 tentativas
"""

palavra_secreta = 'brasil'
tentativas = 3
palavras_digitadas = []

while True:
    letra_digitada = input('Digite um letra: ')

    if tentativas <= 1:
        print('Game Over')
        break

    if len(letra_digitada) > 1:
        print('Por favor, digite apenas uma letra')
        continue

    palavras_digitadas.append(letra_digitada)
    print(f'Letras ja digitadas: {palavras_digitadas}')

    if letra_digitada in palavra_secreta:
        print('Voce acertou')
    else:
        tentativas -= 1
        print(f'Voce ainda tem {tentativas} tentativas')
    palavra_secreta_tmp = ''
    for i in palavra_secreta:
        if i in palavras_digitadas:
            palavra_secreta_tmp += i
        else:
            palavra_secreta_tmp += '*'
    print(palavra_secreta_tmp)

    if palavra_secreta_tmp == palavra_secreta:
        print('Voce ganhou')
        break
