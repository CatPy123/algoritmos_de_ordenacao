def ler_lista_do_usuario():
    while True:
        entrada = input("Digite os números separados por espaço: ")
        partes = entrada.split()
        try:
            lista = [int(valor) for valor in partes]
            return lista
        except ValueError:
            print("Entrada inválida. Use apenas inteiros.")

"""
Explicação: a função fica em um laço até que o usuário digite uma entrada válida. O método split( )
separa o texto digitado em pedaços usando o espaço como referência, e a list comprehension tenta
converter cada pedaço em inteiro. Se algum pedaço não puder ser convertido, o Python lança um
ValueError, que é capturado para exibir uma mensagem de erro e pedir a entrada novamente.
"""

def exibir_resultado(nome_algoritmo, lista_ordenada):
    print("Algoritmo utilizado: " + nome_algoritmo)
    print("Lista ordenada: " + str(lista_ordenada))

def gerar_lista_aleatoria(tamanho):
    import random
    lista = [random.randint(0, 9999) for _ in range(tamanho)]
    return lista

def gerar_lista_quase_ordenada(lista):
    quase = sorted(lista)
    if len(quase) > 1:
        meio = len(quase) // 2
        ultimo = len(quase) - 1
        quase[meio], quase[ultimo] = quase[ultimo], quase[meio]
    return quase

"""Explicação: o uso de sorted( ) aqui é permitido porque essa função apenas prepara dados de teste
para a comparação de desempenho, e não é um dos algoritmos que o aluno está implementando
como exercício. Após ordenar a lista, dois elementos são trocados de posição de propósito, simulando
uma lista quase ordenada, mas não totalmente ordenada.
"""
