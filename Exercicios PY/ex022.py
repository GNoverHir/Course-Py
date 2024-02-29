nomeCompleto = str(input('Digite seu nome completo: '))

nomeMaiusculo = nomeCompleto.upper()
nomeMinusculo = nomeCompleto.lower()

nomeSemEspaço = nomeCompleto.replace(' ', '')
qtdLetrasNome = len(nomeSemEspaço)

nomeSeparado = nomeCompleto.split()
qtdPrimeiroNome = (len(nomeSeparado[0]))

print("""
      Nome: {}\n
      Em Maiusculas: {}\n
      Em Minusculas: {}\n
      Quantidade de letras do nome: {}\n
      Quantidade de letras do primeiro nome: {}""".format(nomeCompleto, nomeMaiusculo, nomeMinusculo, qtdLetrasNome, qtdPrimeiroNome))