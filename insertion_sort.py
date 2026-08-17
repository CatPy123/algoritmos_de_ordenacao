def insertion_sort(lista):
    n = len(lista)
    deslocamentos = 0
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            deslocamentos += 1
            j -= 1
        lista[j + 1] = chave
    print("deslocamentos=" + str(deslocamentos))
    return lista

"""
Explicação: a variável chave guarda o valor que será inserido na posição correta dentro da parte já
ordenada da lista, formada pelos elementos anteriores ao índice i. O laço while desloca para a direita
todos os elementos maiores que a chave, contando cada deslocamento. Quando o laço while termina,
seja porque chegou ao início da lista, seja porque encontrou um valor menor ou igual a chave, ela é
finalmente colocada na posição j + 1.
"""