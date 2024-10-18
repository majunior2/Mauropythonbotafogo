"""
Elabore um fluxograma que calcule quantas notas de 50, 10 e 1 são necessárias para se pagar uma conta cujo valor é fornecido.
"""

def calcular_notas(valorconta):
    notas50 = 0
    notas10 = 0
    notas1 = 0
    
    while valorconta >= 50:
        notas50 += 1
        valorconta -= 50
    
    
    while valorconta >= 10:
        notas10 += 1
        valorconta -= 10
    
   
    while valorconta >= 1:
        notas1 += 1
        valorconta -= 1
    
    
    return notas50, notas10, notas1


valor = int(input("Informe o valor da conta: "))
notas_50, notas_10, notas_1 = calcular_notas(valor)

print(f"Notas de 50: {notas_50}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 1: {notas_1}")