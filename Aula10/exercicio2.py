"""
elabore um fluxograma que calcule e exiba a média de 500 números fornecidos pelo usuário
"""
def calcular_media():
    soma = 0  # Inicializa a soma
    contador = 0  # Inicializa o contador

    # Loop para coletar 500 números
    while contador < 500:
        numero = float(input(f"Informe o {contador + 1}º número: "))  # Lê o número
        soma += numero  # Adiciona o número à soma
        contador += 1  # Incrementa o contador

    # Calcula a média
    media = soma / 500

    # Exibe a média
    print(f"A média dos 500 números fornecidos é: {media}")

# Chama a função para executar o programa
calcular_media()
