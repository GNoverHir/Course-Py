import math

while True: # Coloquei so pra continuar o codigo. Ainda n foi aprendido na aula
    n = float(input("Digite um numero qualquer: "))
    # print('O numero {} tem sua porção inteira de {}'.format(n, math.floor(n))) # -> Minha primeira tentaiva. floor arrendo pro menos
    print('O numero {} tem sua porção inteira de {}'.format(n, math.trunc(n))) # -> Trunc deixa apenas o inteiro do numero