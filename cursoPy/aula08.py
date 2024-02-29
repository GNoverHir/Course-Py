# # from math import sqrt -> So vai puxar a função SQRT da biblioteca MATH 
# import math # -> puxa tudo da biblioteca
# num = int(input('Digite um numero: '))
# raiz = math.sqrt(num) # math.sqrt faz raiz
# print('A raiz de {} é igual a {}'.format(num, raiz))
# print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # math.ceil arredonda o numero para o maior
# print('A raiz de {} é igual a {:.2f}'.format(num, math.floor(raiz))) # math.floor arrendonda o numero para o menor
# na parte '{:.2f}' isso quer dizer q vai mostrar o numero com apenas 2 casas decimais, então por ex, 3.4566 vai ficar apenas 3.45

# import random
# num = random.randint(1, 10) # printa um numero inteiro(randomint) entre (1 e 10)
# # num = random.random() # vai printar um numero aleatorio entre 0 e 1
# print(num)


import emoji
print(emoji.emojize("Olá, mundo :sunglasses:", use_aliases=True))