def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


"""
Explicação: o laço externo, controlado por i, define quantas passagens completas serão feitas pela
lista. O laço interno, controlado por j, percorre pares de elementos vizinhos. Sempre que o elemento
da esquerda for maior que o da direita, os dois trocam de lugar. O limite ( n - 1 - i ) evita comparar
novamente as posições finais, que já ficaram corretas nas passagens anteriores.
"""


# Versão otimizada

def bubble_sort_otimizado(lista):
    n = len(lista)
    passagens = 0
    trocas = 0
    for i in range(n - 1):
        houve_troca = False
        passagens += 1
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocas += 1
                houve_troca = True
        if not houve_troca:
            break
    print("passagens=" + str(passagens))
    print("trocas=" + str(trocas))
    return lista

"""
Explicação: a variável houve_troca começa como False a cada passagem. Se nenhuma troca
acontecer durante o laço interno, isso significa que a lista já está ordenada, e o laço externo é
interrompido com break, economizando passagens desnecessárias. O contador de passagens soma
um a cada repetição do laço externo, e o contador de trocas soma um a cada troca de posições
realizada.
"""
