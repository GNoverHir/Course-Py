from pprint import pprint

conta_palavras = {}
conta_letras = {}

# Abre o arquivo no modo de leitura ('r')
with open('./meuTexto.txt', 'r') as f:
    # Para cada linha no arquivo
    for linha in f:
        # Determina que 'linha' é igual a 'linha.split()', que realiza a separação por espaços
        palavras_na_linha = linha.split()
        
        # Para cada palavra na linha...
        for palavra in palavras_na_linha:
            # Atualiza o contador de palavras para a palavra atual
            # conta_palavras.get(palavra, 0) retorna o valor atual da palavra ou 0 se a palavra não existir no dicionário
            # Adiciona 1 ao valor existente ou cria uma nova entrada com valor 1
            conta_palavras[palavra] = conta_palavras.get(palavra, 0) + 1
            
            # Para cada letra na palavra...
            for letra in palavra:
                # Atualiza o contador de letras para a letra atual
                # Semelhante ao contador de palavras, mas agora estamos contando letras
                conta_letras[letra] = conta_letras.get(letra, 0) + 1

# Usa pprint para imprimir os resultados
pprint(conta_palavras)
pprint(conta_letras)