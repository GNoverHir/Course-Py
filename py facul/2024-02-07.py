# # Tupla:
# t = (1, 2, 3)
# #    0, 1, 2
# # idx

# # Lista
# l = [1, 2, 3]
# #    0, 1, 2
# # idx

# # operações permitidas, pois estamos acessando e UTILZANDO o conteúdo
# t[1] * 1
# l[1] * 1

# # operação não permitida para TUPLA
# # t[1] = 6


# l = [23, 43, 2, 0, -6, 23432]
# l.sort()  # a lista foi ordenada do menor para o maior
# print(l)  # imprime a lista ordenada de modo crescrente

# l.sort(reverse=True)  # a lista foi ordenada do maior para o menor
# print(l)  # imprime a lista ordenada de modo decrescrente

# A busca em um array/vetor/lista ordenado é muito mais eficiente (rápido)

# # l = ["joão", "mirella", "natan", "clara"]
# l = ["clara", "joão", "mirella", "natan"]

# ["clara", "joão"]["mirella", "natan"]

# ["mirella"]["natan"]

# "mirella"

# for i, name in enumerate(l):
#     if name == "mirella":
#         break

# print("mirealla está na posição", i)


# l.index("mirella")

# l[i]
# 0,     1,   2, 3, ..., n-3, n-2, n-1
# -n, -n-1,         ...,  -3 , -2, -1


## DICIONÁRIO
# chave -> valor
# key   -> value
# forma de escrever um dicionário
# {
#     chave1: valor1,
#     chave2: valor2,
#     chave3: valor3,
#     chave4: valor4,
# }


## Possíveis chaves:

## STRING (texto) como chave

# d = {
#     "clara": XXX,
#     "joão": XXX,
#     "mirella": XXX,
#     "natan": XXX,
# }


# notas = {
#     "clara": 10,
#     "joão": 10,
#     "mirella": 10,
#     "natan": 10,
# }

# notas["joão"]  # acessar o valor a partir de uma chave


# # NÚMERO (int) como chave
# rm_aluno = {
#     123: "joão",
#     124: "clara",
#     125: "mirella",
#     126: "natan",
# }

# rm_aluno[123]  # acessar o valor a partir de uma chave


# # TUPLA como chave
# matricula = {
#     (123, "joão"): "joão",
#     (124, "clara"): "clara",
#     (125, "mirella"): "mirella",
#     (126, "natan"): "natan",
# }

# matricula[(123, "joão")]  # acessar o valor a partir de uma chave


# ## Alterando o valor dada uma chave
# matricula[(123, "joão")] = "joão vitor"

# # # removendo um valor do dicionário
# # del matricula[(123, "joão")]  # APENAS APAGA o registro
# # # OU
# # matricula.pop((123, "joão"))  # APAGA E RETORNA o registro

# # CUIDADO:
# del matricula[(123, "joão")]
# # é diferente de
# del matricula


# # TIPOS DE VALORES
banco_de_dados_fiap = {
    "RM123": {
        "matriculado": True,
        "nome": "beltrano",
        "faltas": 1,
        "assiduidade": 0.9,  # (10 - 1) / 10  # % de presença nas aulas
        "notas": [10, 8.5, 9],
        "chave2": ("rm123", 2023),
        "ano_ingresso": 2023,
        "matricula": "rm123",
    },
    "RM124": {
        "matriculado": False,
        "nome": "fulano",
        "faltas": 10,
        "assiduidade": 0.0,  # % de presença nas aulas
        "notas": None,
        "chave2": ("rm124", 2023),
        "ano_ingresso": 2023,
        "matricula": "rm124",
    },
}

# acessando o dicionário com os registros do aluno RM 124
banco_de_dados_fiap["RM124"]

# acessando o dicionário com os registros do aluno RM 124
# e seu número de faltas
banco_de_dados_fiap["RM124"]["faltas"]


# acessando o dicionário com os registros do aluno RM 123
# e seu número de faltas
banco_de_dados_fiap["RM123"]["faltas"]
#                        ^

# # Listas de dicionários
l = [
    {
        "matriculado": True,
        "nome": "beltrano",
        "faltas": 1,
        "assiduidade": 0.9,  # (10 - 1) / 10  # % de presença nas aulas
        "notas": [10, 8.5, 9],
        "chave2": ("rm123", 2023),
        "ano_ingresso": 2023,
        "matricula": "rm123",
    },
    {
        "matriculado": False,
        "nome": "fulano",
        "faltas": 10,
        "assiduidade": 0.0,  # % de presença nas aulas
        "notas": None,
        "chave2": ("rm124", 2023),
        "ano_ingresso": 2023,
        "matricula": "rm124",
    },
]

# acessando o dicionário com os registros do aluno RM 124
l[1]

# acessando o dicionário com os registros do aluno RM 124
# e seu número de faltas
l[1]["faltas"]


# acessando o dicionário com os registros do aluno RM 123
# e seu número de faltas
l[0]["faltas"]
# ^
