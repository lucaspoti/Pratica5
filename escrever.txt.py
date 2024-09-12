file_path = 'texto.txt'

with open(file_path, 'w') as file:
    texto = list()
    
    texto.append("Pegar um sol.")
    texto.append("Viajar para o Rio de Janeiro.")
    texto.append("Ir para a praia.")
    
    for frase in texto:
        file.write(frase + '\n')
