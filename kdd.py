import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def main():
    file_path = 'texto.txt'
    output_file_path = 'ordenado.txt'
    
    palavras = []


    with open(file_path, 'r') as file:
        for linha in file:
            palavras.extend(linha.split())

    
    def medir_tempo(func, arr):
        start_time = time.time()
        resultado = func(arr.copy())
        end_time = time.time()
        return resultado, end_time - start_time

  
    sorted_bubble, tempo_bubble = medir_tempo(bubble_sort, palavras)
    print("Bubble Sort:")
    print("Tempo de execução: {:.6f} segundos".format(tempo_bubble))
    print("Palavras ordenadas:", sorted_bubble)


    sorted_selection, tempo_selection = medir_tempo(selection_sort, palavras)
    print("\nSelection Sort:")
    print("Tempo de execução: {:.6f} segundos".format(tempo_selection))
    print("Palavras ordenadas:", sorted_selection)

    palavras_nativo = palavras.copy()
    start_time = time.time()
    palavras_nativo.sort()
    end_time = time.time()
    tempo_nativo = end_time - start_time

    print("\nMétodo nativo sort():")
    print("Tempo de execução: {:.6f} segundos".format(tempo_nativo))
    print("Palavras ordenadas:", palavras_nativo)

    with open(output_file_path, 'w') as file:
        file.write('\n'.join(palavras_nativo))

if __name__ == "__main__":
    main()
