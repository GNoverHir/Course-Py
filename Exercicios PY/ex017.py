import math

c1 = float(input('Digite o cateto oposto: '))
c2 = float(input('Digite o cateto adjacente: '))

h = math.sqrt(c1) + math.sqrt(c2)

print('A hipotenusa da soma dos catetos ao quadrado {} e {} é igual a {}'.format(c1, c2, h))

