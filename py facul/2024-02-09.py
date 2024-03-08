# {chave: valor}
# [
# {
#     "a": None,
#     "b": 1,
#     1: "a",
#     2: (1, 2, 3),
#     (1, "a"): ["a", 1, True],
#     (1, 1): True,
#     ("a", "b"): False,
#     "dicionario de dicionarios": {
#         1: 2,

#     }
# }
# ]

from pprint import pprint

s = "No universo fitness das redes sociais, é comum ver uma cena curiosa. Em jejum e em busca de uma barriga negativa, influenciadoras controlam a respiração contraindo os músculos abdominais, sugando a barriga para dentro do corpo e formando uma espécie de vácuo no centro do tronco. E assim se inicia o dia..."
frequencia = {}
for letra in s:
    frequencia[letra] = 1 + frequencia.get(letra, 0)

# pprint(frequencia)

frequencia_palavras = {}
for palavra in s.split():
    frequencia_palavras[palavra] = 1 + frequencia_palavras.get(palavra, 0)

# pprint(frequencia_palavras)


import pandas as pd

pd.Series(frequencia).plot.bar()
