import math
angulo = float(input("digite o angulo q deseja: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O angulo {} possue: \nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(angulo, seno, cosseno, tangente))
