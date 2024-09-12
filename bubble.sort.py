import random

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
array_numeros = [random.randint(0, 100) for _ in range(15)]
print("Array de números original:")
print(array_numeros)
bubbleSort(array_numeros)
print("\nArray de números ordenado com Bubble Sort:")
print(array_numeros)
