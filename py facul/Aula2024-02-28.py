with open('./meuTexto.txt', 'r+') as file:
    texto = file.readlines()
    for line in texto:
        print(line)
