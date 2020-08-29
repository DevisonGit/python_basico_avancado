numero = input("Digite um numero: ")

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O numero {numero} e Par')
    else:
        print(f'O numero {numero} e Impar')
else:
    print('numero invalido')



