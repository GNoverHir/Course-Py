nome = str(input("Digite um nome: ")).split()

print("O primeiro nome é: {}\nO ultimo nome é: {}".format(nome[0], nome[len(nome) - 1]))
# No final ali, eu basicamente contei quantos caracteres tinham na lista, no caso, como dei split, (PROXIMA LINHA) 
# cada caracter vai ser tudo q esta entre espaços, então ao inves de : (PROXIMA LINHA)
# [ 0=C, 1=u, 2=r ] e assim vai. Ficou assim: [ 0=Curso, 1=em, 2=Video]
# Dado isso usei len(nome) para ele contar quantos caracteres (QUE LEMBRANDO, agora é [ 0=Curso, .... ]) tem ao todo. o LEN conta quantos caracteres tem (PROXIMA LINHA)
# Então ele nao começa pelo 0 (lembrando q o 0 é o jeito q o py começa a contagem de POSIÇÕES numa lista, dicionario e etc) e sim pelo 1. (PROXIMA LINHA)
# Como eu quero a posição, e o len vai estar 1 casa na frente ja q ele começa pelo 1 e o jeito q o py conta as posições numa lista começa por 0, precisei do - 1 (PROXIMA LINHA)
# Pq ai com isso ele iria se igualar com a forma do py de nomiar a posição dentro de uma lista :D
# VAMBORA


