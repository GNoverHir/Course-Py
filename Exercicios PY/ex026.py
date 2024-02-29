# MESMO CODIGO Q O DEBAIXO, MAS COM 4 LINHAS :D
# frase = str(input("Digite uma frase: ")).upper().strip()
# print('A letra A aparece {} vezes na frase!'.format(frase.count('A')))
# print('A primeira letra A apareceu na posição {}!'.format(frase.find('A') + 1))
# print('A ultima letra A apareceu na posição {}!'.format(frase.rfind('A') + 1))


#############################################################################

# MESMO CODIGO Q O DECIMA, MAS COM UMA CACETADA DE LINHA KKKKKKKK
frase = str(input("Digite uma frase: "))
fraseCorrigida = frase.strip()

contagemA = fraseCorrigida.upper().count('A')
primeiroA = fraseCorrigida.upper().find('A')+ 1 # Coloquei o +1 pq sem ele vai mostrar q esta na posição 0, que é o comum programador de entender, mas não de usuario
ultimoA = fraseCorrigida.upper().rfind('A') + 1 # Mesma coisa, iria apararecer por exemplo 26, sendo q contando estaria na posição 27. Ai poe +1 p ficar certinho

print('''\n
      Na frase tem: {} letras (a)\n
      A primeira vez q apareceu foi na posição: {}\n
      A ultima vez q apareceu foi na posição: {}'''.format(contagemA, primeiroA, ultimoA))