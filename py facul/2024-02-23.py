from pprint import pprint

# arquivo = open("./exemplo.txt")

# # lê todo o conteúdo do arquivo
# # texto = arquivo.read()

# # lê todo o conteúdo do arquivo, quebrando em linhas
# # texto = arquivo.readlines()

# # lê o arquivo linha a linha
# # for line in arquivo:
# #     print(line)


# with open("./exemplo.txt") as file:
#     for line in file:
#         print(line)


# with open("arquivo-escrita.txt", "w") as f:
# # lança uma exceção qualquer para interromper o fluxo do código
# # exemplo de que quando a operação é interrompida no modo "w", perdemos o conteúdo do arquivo
# raise ValueError

# # escreve no arquivo aberto
# f.write("Oi :+)")

# 'r'
# 'w'
# 'x' Abre um novo arquivo caso n exista
# 'a' append vai para a ultima linha/ultimo caracter e começa escrever a partir dali
# '+' 

# with open("exemplo.txt", "r+") as f:
#     texto = f.read()
#     f.write("\nNOVA LINHA")


arquivo = open("./exemplo.txt")
texto = arquivo.readlines()

conta_letras = {}
conta_palavras = {}
for linha in texto:
    palavras = linha.split()
    for palavra in palavras:
        conta_palavras[palavra] = conta_palavras.get(palavra, 0) + 1
        for letra in palavra:
            conta_letras[letra] = conta_letras.get(letra, 0) + 1
    # conta_letras[letra] = conta_letras.get(letra, 0) + 1


# from pprint import pprint

pprint(conta_letras)
pprint(conta_palavras)

# DESAFIO: Encontrar a palavra e a letra mais frequentes e salvá-los em um arquivo

max_palavra = [None, 0]
for palavra, count in conta_palavras.items():
    if max_palavra[1] < count:
        max_palavra = [palavra, count]

max_char = [None, 0]
for palavra, count in conta_letras.items():
    if max_char[1] < count:
        max_char = [palavra, count]

with open("result.txt", "w") as f:
    f.write(f"Palavra mais frequente: {max_palavra[0]}\n")
    f.write(f"Frequência: {max_palavra[1]}\n")
    f.write("\n" + "=" * 50 + "\n")
    f.write(f"Letra mais frequente: {max_char[0]}\n")
    f.write(f"Frequência: {max_char[1]}\n")

import emoji
