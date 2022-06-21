def relacion(num_1, num_2):
    if num_1 > num_2:
        return 1
    elif num_1 < num_2:
        return -1
    else:
        return 0

combinaciones = [[5,10], [10,5], [5,5]]

for combinacion in combinaciones:
    print(relacion(combinacion[0], combinacion[1]))