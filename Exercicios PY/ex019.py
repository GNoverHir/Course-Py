import random

n1 = str(input("Digite o nome do aluno1: "))
n2 = str(input("Digite o nome do aluno2: "))
n3 = str(input("Digite o nome do aluno3: "))
n4 = str(input("Digite o nome do aluno4: "))

lista=[n1, n2, n3, n4]

aluno = random.choice(lista)

print('O aluno escolhido foi: {}!'.format(aluno))