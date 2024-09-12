import random

array = [random.randint(1, 100) for _ in range(15)]

print("Array original:")
print(array)

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print("Array ordenado:")
print(array)
