from pprint import pprint


def f():
    bd = []  # bd = list()

    while True:

        user = {
            "nome": input("Digite o nome do usuário: "),
            "cpf": input("Digite o cpf do usuário: "),
            "email": input("Digite o email do usuário: "),
            "rg": input("Digite o rg do usuário: "),
        }

        bd.append(user)

        print("\n Usuário adicionado com sucesso!")
        if input("Deseja adicionar mais?[s/n]") == "n":
            break

    return bd


def busca(bd):
    key = input("Digite o campo desejado: ")
    value = input("Digite o valor para buscar")

    results = []
    for user in bd:
        if user[key] == value:
            results.append(user)
        else:
            print('n achei')

    return results


BD = f()

print(busca(BD))
