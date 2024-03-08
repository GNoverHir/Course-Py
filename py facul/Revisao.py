# def create():
#     bd = []

#     while True:
#         user = {
#             "nome": input('Digite o nome do usuario: '),
#             'rg': input('Digite o rg: ')
#         }

#         bd.append(user)

#         print('\n Cadastro concluido! ')
#         if input('\nDeseja adicionar mais? S/N ').upper() == 'N':
#             break
#         print()

#         return bd
    

# def read(bd):

#     results= []
#     key = input('\nDigite o campo q deseja buscar: ')  
#     value = input('\nDigite o valor que deseja achar: ')

#     for user in bd:
#         if user[key] == value:
#             results.append(user)  
#     return results

# def update(bd):
#     results = read(bd)

#     for user in bd:

# import pprint

# conta_palavras = {}
# conta_letras = {}

# with open('') as f:
#     for linha in f:
#         palavras = linha.split()
#         for palavra in palavras:
#             conta_palavras[palavra] = conta_palavras.get(palavra, 0) + 1
#             for letra in palavra:
#                 conta_letras[letra] = conta_letras.get(letra, 0) + 1

# pprint(conta_letras)
# pprint(conta_palavras)


