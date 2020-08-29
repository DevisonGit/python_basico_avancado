"""
For - > percorre valores finitos
enumarate -> enumera os indicies
range -> configura um range para o for range(inicio, fim, passo)
"""

texto = 'Python e show'

for letra in texto:
    print(letra, end=' ')

print()
for i, letra in enumerate(texto):
    print(i, letra)

print()
for i in range(10, 20, 2):
    print(i)
