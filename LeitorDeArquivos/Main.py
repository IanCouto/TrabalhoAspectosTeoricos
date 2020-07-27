#!/usr/bin/python

file = open('../input/input.txt', 'r')
lista_spaco = [i for j in file.read().split() for i in (j, ' ')][:-1]
print(lista_spaco)
comentario = False
cont = 0
saida = []
for str in lista_spaco:

    if comentario == False:
        print(cont)
        if '/*' in str:
              comentario = True
              saida.append("COMMENT")
        elif str in " ":
            saida.append("SPACE")
        elif str.isdigit():
            saida.append("INT")
        elif str in '=':
            saida.append("EQUALS")

    elif "*/" in str:
        comentario = False

    cont += 1

print(saida)
file.close()
