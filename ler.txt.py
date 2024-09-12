file_path = 'loremipsum.txt'

with open(file_path, 'r') as file:
    content = file.read()

print("Conteúdo completo do arquivo:")
print(content)

with open(file_path, 'r') as file:
    first_line = file.readline()

print("\nPrimeira linha do arquivo:")
print(first_line.strip())

print("\nTrês primeiros caracteres do arquivo:")
print(content[:3])

with open(file_path, 'r') as file:
    content_with = file.read()

print("\nConteúdo lido usando 'with':")
print(content_with)
