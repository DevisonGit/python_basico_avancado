"""
While -> executa algo enquanto a condicao for verdadeira
continue -> pular para o proxima volta do laco
break -> encerra a execucao do laco em que ele estive
else -> executa seu conteudo quando a condicao do while for falsa
"""
print('Demostrando o while')
x = 0
while x < 10:
    print(x, end=' ')
    x += 1

print('\nWhile com continue')
x = 0
while x < 10:
    if x == 5:
        x += 1
        print(' Pulando o Cinco ', end=' ')
        continue
    print(x, end=' ')
    x += 1

print('\nWhile com break')
x = 0
while x < 10:
    if x == 5:
        print('break')
        break
    print(x, end=' ')
    x += 1
print('\nWhile com else')
x = 0
while x < 10:
    print(x, end=' ')
    x += 1
else:
    print(f'condicao falsa x vale {x}')
