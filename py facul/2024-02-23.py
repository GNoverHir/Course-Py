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


# with open("exemplo.txt", "r+") as f:
#     texto = f.read()
#     f.write("\nNOVA LINHA")


arquivo = open("./exemplo.txt")
texto = arquivo.readlines()

conta_letras = {}
conta_palavras = {}
for linha in texto:
    palavras = linha.split()
    for char in palavras:
        conta_palavras[char] = conta_palavras.get(char, 0) + 1
        for letra in char:
            conta_letras[letra] = conta_letras.get(letra, 0) + 1
    # conta_letras[letra] = conta_letras.get(letra, 0) + 1


# from pprint import pprint

# pprint(conta_letras)
# pprint(conta_palavras)

# DESAFIO: Encontrar a palavra e a letra mais frequentes e salvá-los em um arquivo

max_palavra = [None, 0]
for char, count in conta_palavras.items():
    if max_palavra[1] < count:
        max_palavra = [char, count]

max_char = [None, 0]
for char, count in conta_letras.items():
    if max_char[1] < count:
        max_char = [char, count]

with open("result.txt", "w") as f:
    f.write(f"Palavra mais frequente: {max_palavra[0]}\n")
    f.write(f"Frequência: {max_palavra[1]}\n")
    f.write("\n" + "=" * 50 + "\n")
    f.write(f"Letra mais frequente: {max_char[0]}\n")
    f.write(f"Frequência: {max_char[1]}\n")
