frase = 'Curso em Video Python'

# print(frase[0]) # vai printar o caracter da posição 0. No caso: 'C'
# print(frase[3:13]) # Vai printar do index 3 até o 12 (o 13 ali n vai ser printado, é dele para trás)
# print(frase[:13]) # Se nao especificar o começo ele vai desde o index 0
# print(frase[1:15:2]) # Ele vai printar do index 1 até o 15 pulando de 2 em 2 casas
# print(frase[1::2]) # Se vc não idetificar o final entre :: ele vai até o fim da lista pulando de 2 em 2
# print(frase[::2]) # Se nao especificar o começo e nem o fim, ele percorre a lista inteira pulando de 2 em 2
# print(frase.count("a")) # Vai printar a contagem de quantos "a" aparecem dentro da frase, que no caso é Curso em Video Python
# OBSERVAÇÃO DE COUNT: 'o' não é a msm coisa que 'O'
# print(frase.upper().count('O')) # O uso do upper vai transformar a frase TODA em maiuscula, e dps o count vai poder contar quantos 'O' existem
# lower PODE SER USADO PARA DEIXAR MINUSCULO!
# print(len(frase)) # Vai contar quantos espaços tem na frase, pro exemplo, (1-C, 2-u, 3-r, 4-s, 5-o, 6-' ', ..... 21-n)
# print(frase.strip()) # Caso frase= '  Curso em Video Python    ' ele iria remover esses espaços desnecessarios no começo e no fim
# print(frase.replace('Python', 'Android')) # Vai trocar a palavra Python da frase por Android
# print('Curso' in frase) # a palvra Curso tem em Frase? Essa resposta vai vir em sim(True) ou nao(False)

# print(frase.find('video')) # Ele vai procurar na frase em que posição está 'video'.
# NO CASO vai printar -1 pq nao existe 'video', mas sim 'Video'. Nesse caso é so deixar a frase em upper, ou lower. Se lower, devemos achar por 'video'. Se upper, devemos procurar por 'VIDEO'
# print(frase.lower().find('video'))


# SPLIT
# print(frase.split()) # Vai dividir as palavras pelos espaços entre ela, então vai individualizar 'Curso', 'em', 'Video' e 'Python'
# Agora a ordem esta [0-'Curso', 1-'em', 2-'Video', 3-'Python']. E dentro de cada uma delas está assim: [ 0-'C', 1-'u', 2-'r', 3-'s', 4-'o'] [ 0-'e', 1-'m'] Saco?
# Então se fizermos assim:
# frase = 'Curso em Video Python'
# dividido = frase.split()
# print(dividido [0] [3]) # aqui ele vai acessar a posição 0 do split(ou seja: 0-'Curso'), e depois vai acessar a posição 3 dentro dele (ou seja: 3-'r') -> print vai ser 'r'














# DICA
# para evitar isso: print("Se você sabe o seu valor, então vá à luta e conquiste o que é seu! Mas você precisa estar disposto a receber os golpes, e não ficar apontando dedos e dizendo que não está onde quer por causa dele, ou dela, ou de qualquer pessoa! Covardes fazem isso é você não é um deles! Você é melhor do que isso!")
# use 3 aspas:
#print("""Se você sabe o seu valor, 
#      então vá à luta e conquiste o que é 
#      seu! Mas você precisa estar disposto 
#      a receber os golpes, e não ficar 
#      apontando dedos e dizendo que não está onde 
#      quer por causa dele, ou dela, ou de qualquer 
#      pessoa! Covardes fazem isso é você não é um 
#      deles! Você é melhor do que isso!""") 