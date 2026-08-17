def selection_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
            trocas += 1
    print("comparações=" + str(comparacoes))
    print("trocas=" + str(trocas))
    return lista

"""Explicação: o laço externo, controlado por i, percorre cada posição da parte ainda não ordenada. A
variável indice_menor guarda a posição do menor valor encontrado até o momento nessa parte. O
laço interno, controlado por j, compara cada elemento restante com o menor valor já encontrado,
incrementando o contador de comparações a cada comparação feita. Ao final do laço interno, se o
menor elemento não estiver na posição i, a troca é feita uma única vez, e o contador de trocas é
incrementado."""

"""
>>> selection_sort([5, 4, 3, 2, 1])
... 
comparações=10
trocas=2
[1, 2, 3, 4, 5]
>>> selection_sort([1, 2, 3, 4, 5])
... 
comparações=10
trocas=0
[1, 2, 3, 4, 5]
"""