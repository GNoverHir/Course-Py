# Exemplo quebrado
# def delete(bd):
#     key = input("\nQual campo você deseja buscar para a apagar: ")
#     value = input("Digite o valor para buscar: ")

#     for user in bd:
#         if user[key] == value:
#             del user


def create():
    bd = []  # bd = list()

    while True:

        user = {
            "nome": input("Digite o nome do usuário: "),
            # "cpf": input("Digite o cpf do usuário: "),
            # "email": input("Digite o email do usuário: "),
            "rg": input("Digite o rg do usuário: "),
        }

        bd.append(user)

        print("\n Usuário adicionado com sucesso!")
        if input("Deseja adicionar mais?[s/n] ") == "n":
            break
        print()

    return bd


def read(bd):
    key = input("\nQual campo você deseja buscar: ")
    value = input("Digite o valor para buscar: ")

    results = []
    for user in bd:
        if user[key] == value:
            results.append(user)

    return results


def update(bd):
    # Busco os registro para alterar
    results = read(bd)

    # leio qual o campo será alterado
    key = input("\nQual campo você deseja alterar: ")
    value = input("Digite o novo valor: ")

    for record in results:
        if record[key] == value:
            
        


BD = create()

# update(BD)
# # delete(BD)
# print(BD)


# CRUD: Create Read Update    Delete
#       Criar  Ler  Atualizar Apagar


# Abrindo um arquivo em python
# open("./2024-16-02.py")
