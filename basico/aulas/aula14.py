num_1 = input('Digite um numero :')
num_2 = input('Digite outro numero: ')

# isnumeric isdigits isdecimal

if num_1.isdigit() and num_2.isdigit():
    print(int(num_1) + int(num_2))
else:
    print('Nao pude converter para numeros')
