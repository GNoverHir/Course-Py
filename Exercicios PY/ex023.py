n = str(input('Digite um numero de 0 a 9999: '))

milhar = n[0]
centena = n[1]
dezena = n[2]
unidade = n[3]

print("="*70)
print("""
      Numero digitado: {}\n
      unidade: {}\n
      dezena: {}\n
      centena: {}\n
      milhar: {}\n""".format(n, unidade, dezena, centena, milhar))