def separar(lista_numeros):
    lista_numeros.sort()
    lista_pares = []
    lista_impares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)
    return lista_pares, lista_impares

pares, impares = separar([6,5,2,1,7])

print(f'Pares: {pares}')
print(f'Impares: {impares}')