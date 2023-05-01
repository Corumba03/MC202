import re

dim = [int(x) for x in input().split()]  # Dimensões da matriz
num_elem = int(input())  # Número de elementos não-nulos
size = dim[0] + dim[1]  # Número máximo de elementos não-nulos
coordv = []             # Vetor de coordenadas


for elem in range(size):
    if elem < num_elem:
        tripla = [int(s) for s in re.findall(r'\d+', input())]
    else:
        tripla = [0, 0, 0]
    coordv.append(tripla)


def printv():
    global coordv, num_elem
    print("VC: ", end="")
    for i in range(num_elem):

        print("({},{},{})".format(coordv[i][0], coordv[i][1], coordv[i][2]), end=" ")
    print("")


def rec(i, j):
    global coordv, num_elem
    for elem in range(num_elem):
        if i == coordv[elem][0] and j == coordv[elem][1]:
            print(f'M[{coordv[elem][0]}][{coordv[elem][1]}] == {coordv[elem][2]}')
            return
    print(f'M[{i}][{j}] == 0')


def find(i, j):
    global coordv, num_elem
    for elem in range(num_elem):
        if i == coordv[elem][0] and j == coordv[elem][1]:
            return elem
        if i < coordv[elem][0]:
            return -1
    return -1


def alter(i, j, val):
    global coordv, num_elem, size, dim
    tripla = [i, j, val]
    if i > dim[0] or j > dim[1]:
        return
    if val == 0:
        item = find(i, j)
        if item > -1:
            coordv.pop(item)
            num_elem -= 1
            return
        else:
            return
    elif num_elem == size:  # Se estiver cheio já sai da função
        print("O VC esta' cheio.")
        return
    elif i < coordv[0][0] or (i == coordv[0][0] and j < coordv[0][1]):  # Se for menor que o primeiro item
        coordv.insert(0, tripla)
        num_elem += 1
        return
    elif i > coordv[num_elem-1][0] or (i == coordv[num_elem-1][0] and j > coordv[num_elem-1][1]):  # Se for maior que o último
        coordv.insert(num_elem, tripla)
        num_elem += 1
        return
    else:
        for elem in range(num_elem):
            if i == coordv[elem][0]:  # Se a linha existir
                if (j == coordv[elem][1]):
                    coordv[elem][2] = val
                    return
                elif j < coordv[elem][1]:  # E se o novo elemento for menor que algum elemento da linha
                    coordv.insert(elem, tripla)
                    num_elem += 1
                    return
                elif i < coordv[elem+1][0] or elem+1 == num_elem:  # Ou se o novo elemento for maior que o maior elemento da linha
                    coordv.insert(elem+1, tripla)
                    num_elem += 1
                    return
            elif (i > coordv[elem][0] and i < coordv[elem+1][0]):
                coordv.insert(elem+1, tripla)
                num_elem += 1
                return


oper = 'x'
while oper != 't':
    entrada = input().split()
    oper = entrada[0]
    if oper == 'a':
        entrada = entrada[1] + entrada[2]
        entrada = [int(s) for s in re.findall(r'-?\d+', entrada)]
        i, j, val = (entrada[0], entrada[1], entrada[2])
        alter(i, j, val)
    elif oper == 'r':
        entrada = [int(s) for s in re.findall(r'-?\d+', entrada[1])]
        i, j = (entrada[0], entrada[1])
        rec(i, j)
    elif oper == 'p':
        if num_elem == 0:
            print("O VC esta' vazio.")
        else:
            printv()
