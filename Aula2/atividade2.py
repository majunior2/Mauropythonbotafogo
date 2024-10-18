# Solicita ao usuário que insira o valor do salário atual
salario_atual = float(input("Digite o valor do salário atual: R$ "))

# Solicita ao usuário que insira a porcentagem de aumento
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))

# Calcula o valor do aumento
valor_aumento = salario_atual * (porcentagem_aumento / 100)

# Calcula o novo salário
novo_salario = salario_atual + valor_aumento

# Exibe o valor do aumento e o novo salário
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
