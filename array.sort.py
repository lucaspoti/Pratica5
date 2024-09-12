import random

array_inteiros = [random.randint(0, 100) for _ in range(15)]
print("Array de números inteiros original:")
print(array_inteiros)
array_inteiros.sort()
print("\nArray de números inteiros ordenado de forma crescente:")
print(array_inteiros)
array_inteiros.sort(key=None, reverse=True)
print("\nArray de números inteiros ordenado de forma decrescente:")
print(array_inteiros)
array_strings = ["nome", "dataNascimento", "cpf", "rg"]
print("\nArray de strings original:")
print(array_strings)
array_strings.sort()
print("\nArray de strings ordenado de forma crescente:")
print(array_strings)
array_strings.sort(key=None, reverse=True)
print("\nArray de strings ordenado de forma decrescente:")
print(array_strings)
