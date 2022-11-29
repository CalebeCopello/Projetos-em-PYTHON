def numeroFaltando(*n):
    lis = sorted(n)
    mn = min(lis)
    mx = max(lis)
    fal = []
    for c in range(1, mx):
        if c not in lis:
            fal.append(c)
    return f'Números de entrada {lis}\nNúmeros que faltam:{fal}'


print(numeroFaltando(9,5,7,1,3,15))
