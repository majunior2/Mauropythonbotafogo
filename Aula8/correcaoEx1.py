alunos = []


num_alunos = int(input("Digite o número de alunos: "))


for i in range(num_alunos):
    nome_aluno = input(f"Digite o nome do aluno {i + 1}: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    media = (nota1 + nota2) / 2 
    
    status = "Aprovado" if media >= 6.5 else "Reprovado"
    
    aluno_info = {
        'nome': nome_aluno,
        'nota1': nota1,
        'nota2': nota2,
        'media': media,
        'status': status
    }
    
    alunos.append(aluno_info)

for aluno in alunos:
    print(f"{aluno['nome']}: Média: {aluno['media']:.2f} - {aluno['status']}")
