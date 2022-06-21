def recortar(numero, limite_inf, limite_sup):
    if numero < limite_inf:
        return limite_inf
    elif numero > limite_sup:
        return limite_sup
    else:
        return numero

print(recortar(15,0,10))