nome = str(input("Digite um nome de pessoa composto: "))

silva = 'silva' in nome.lower()
# ou
# silva = 'SILVA' in nome.upper()

print('O nome tem SILVA?: {}'.format(silva))