 # Importação das funções que serão usadas
from bubble_sort import bubble_sort, bubble_sort_otimizado
from utilitarios import ler_lista_do_usuario, exibir_resultado
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from utilitarios import gerar_lista_aleatoria
from utilitarios import gerar_lista_quase_ordenada
import time


# Menu principal
def exibir_menu():
    print("")
    print("1. Bubble Sort (versão básica)")
    print("2. Bubble Sort (versão otimizada)")
    print("3. Selection Sort")
    print("4. Insertion Sort")
    print("5. Comparação rápida (Bubble x Selection)")
    print("6. Comparação de desempenho (os três algoritmos)")
    print("0. Sair")


def executar_comparacao_rapida():
    lista = ler_lista_do_usuario()
    copia_bubble = list(lista)
    copia_selection = list(lista)
    print("Bubble Sort otimizado:")
    resultado_bubble = bubble_sort_otimizado(copia_bubble)
    print("Selection Sort:")
    resultado_selection = selection_sort(copia_selection)
    print("Resultado Bubble Sort otimizado: " + str(resultado_bubble))
    print("Resultado Selection Sort: " + str(resultado_selection))

"""Explicação: a mesma lista digitada pelo usuário é copiada duas vezes, uma para cada algoritmo,
garantindo que os dois recebam exatamente a mesma entrada, sem que a execução de um interfira
na execução do outro. Os contadores de cada algoritmo são impressos automaticamente dentro das
próprias funções de ordenação.
"""

def executar_comparacao_desempenho():
    tamanho = ""
    while type(tamanho) != int:
        try:
            tamanho = int(input("Digite o tamanho da lista para o teste: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    lista_aleatoria = gerar_lista_aleatoria(tamanho)
    lista_quase_ordenada = gerar_lista_quase_ordenada(lista_aleatoria)
    algoritmos = [
        ("Bubble Sort otimizado", bubble_sort_otimizado),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
    ]
    print("")
    print("Resultados com lista aleatória:")
    for nome, funcao in algoritmos:
        copia = list(lista_aleatoria)
        inicio = time.perf_counter()
        funcao(copia)
        fim = time.perf_counter()
        tempo = round(fim - inicio, 4)
        print(nome + " - tempo: " + str(tempo) + " s")
    print("")
    print("Resultados com lista quase ordenada:")
    for nome, funcao in algoritmos:
        copia = list(lista_quase_ordenada)
        inicio = time.perf_counter()
        funcao(copia)
        fim = time.perf_counter()
        tempo = round(fim - inicio, 4)
        print(nome + " - tempo: " + str(tempo) + " s")


"""Explicação: a lista de tuplas algoritmos guarda o nome de exibição e a função correspondente de
cada algoritmo, permitindo executar os três dentro de um mesmo laço for, sem repetir código. Para
cada algoritmo, uma cópia independente da lista é usada, e o tempo de execução é medido com
time.perf_counter( ) antes e depois da chamada da função, calculando a diferença entre os dois
instantes.
"""

def main():
    opcao = -1
    while opcao != 0:
        exibir_menu()
        entrada = input("Escolha uma opção: ")
        
        try:
            opcao = int(entrada)
        except ValueError:
            print("Opção inválida.")
            continue

        if opcao == 1:
            lista = ler_lista_do_usuario()
            resultado = bubble_sort(list(lista))
            exibir_resultado("Bubble Sort básico", resultado)
        elif opcao == 2:
            lista = ler_lista_do_usuario()
            resultado = bubble_sort_otimizado(list(lista))
            exibir_resultado("Bubble Sort otimizado", resultado)
        elif opcao == 3:
            lista = ler_lista_do_usuario()
            resultado = selection_sort(list(lista))
            exibir_resultado("Selection Sort", resultado)
        elif opcao == 4:
            lista = ler_lista_do_usuario()
            resultado = insertion_sort(list(lista))
            exibir_resultado("Insertion Sort", resultado)
        elif opcao == 5:
            executar_comparacao_rapida()
        elif opcao == 6:
            executar_comparacao_desempenho()

        elif opcao == 0:
            print("Encerrando o programa.")
        else:
            print("Opcao invalida. Tente novamente.")

"""
Explicação: o programa fica em um laço enquanto a opção escolhida for diferente de zero. A cada
repetição, o menu é exibido, a opção é lida e convertida para inteiro dentro de um bloco try, e a
estrutura if - elif - else decide qual algoritmo executar. Repare que sempre é passada uma cópia da
lista, com lista(lista), para que a lista original digitada pelo usuário não seja alterada por engano.
"""

if __name__ == "__main__":
    main()

"""
Explicação: essa estrutura garante que o menu só seja executado quando rodarmos o arquivo
main.py diretamente, e não quando outro arquivo apenas importar alguma função dele.
"""
