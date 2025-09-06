# ===========================
#  Sistema de Controle de Faltas
# ===========================

class Aluno:
    def __init__(self, nome, total_aulas, faltas=0):
        self.nome = nome
        self.total_aulas = total_aulas
        self.faltas = faltas
    
    def calcular_percentual_presenca(self):
        # Calcula o percentual de presença do aluno
        if self.total_aulas == 0:
            return 0
        aulas_presentes = self.total_aulas - self.faltas
        return (aulas_presentes / self.total_aulas) * 100
    
    def verificar_status(self):
        # Verifica se o aluno está aprovado ou reprovado por falta
        percentual = self.calcular_percentual_presenca()
        if percentual >= 75:
            return "APROVADO"
        else:
            return "REPROVADO POR FALTA"
    
    def adicionar_falta(self, quantidade=1):
        # Adiciona faltas ao aluno
        self.faltas += quantidade
        if self.faltas > self.total_aulas:
            self.faltas = self.total_aulas
    
    def __str__(self):
        return f"{self.nome} - Faltas: {self.faltas}/{self.total_aulas} - Presença: {self.calcular_percentual_presenca():.1f}% - {self.verificar_status()}"

# Lista para armazenar todos os alunos
alunos = []

def cadastrar_aluno():
    # Cadastra um novo aluno no sistema
    print("\n=== CADASTRO DE ALUNO ===")
    nome = input("Nome do aluno: ").strip()
    
    # Verificar se aluno já existe
    for aluno in alunos:
        if aluno.nome.lower() == nome.lower():
            print("Erro: Aluno já cadastrado!")
            return
    
    try:
        total_aulas = int(input("Total de aulas da disciplina: "))
        if total_aulas <= 0:
            print("Erro: O número de aulas deve ser positivo!")
            return
        
        novo_aluno = Aluno(nome, total_aulas)
        alunos.append(novo_aluno)
        print(f"Aluno {nome} cadastrado com sucesso!")
    except ValueError:
        print("Erro: Digite um número válido para o total de aulas!")

def registrar_falta():
    # Registra faltas para um aluno específico
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    
    print("\n=== REGISTRAR FALTA ===")
    nome = input("Nome do aluno: ").strip()
    
    aluno_encontrado = None
    for aluno in alunos:
        if aluno.nome.lower() == nome.lower():
            aluno_encontrado = aluno
            break
    
    if not aluno_encontrado:
        print("Aluno não encontrado!")
        return
    
    try:
        quantidade = int(input("Quantidade de faltas a adicionar: "))
        if quantidade <= 0:
            print("Erro: A quantidade deve ser positiva!")
            return
        
        aluno_encontrado.adicionar_falta(quantidade)
        print(f"Falta(s) registrada(s) para {aluno_encontrado.nome}")
        print(f"Status atual: {aluno_encontrado}")
    except ValueError:
        print("Erro: Digite um número válido!")

def buscar_aluno():
    # Busca e exibe informações de um aluno específico
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    
    print("\n=== BUSCAR ALUNO ===")
    nome = input("Nome do aluno: ").strip()
    
    for aluno in alunos:
        if aluno.nome.lower() == nome.lower():
            print(f"\nInformações do aluno:")
            print(f"Nome: {aluno.nome}")
            print(f"Total de aulas: {aluno.total_aulas}")
            print(f"Faltas: {aluno.faltas}")
            print(f"Percentual de presença: {aluno.calcular_percentual_presenca():.1f}%")
            print(f"Status: {aluno.verificar_status()}")
            return
    
    print("Aluno não encontrado!")

def listar_todos_alunos():
    # Lista todos os alunos com suas informações
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    
    print("\n=== LISTA DE TODOS OS ALUNOS ===")
    print("-" * 80)
    
    # Ordenar por nome
    alunos_ordenados = sorted(alunos, key=lambda x: x.nome)
    
    for aluno in alunos_ordenados:
        print(aluno)
    
    print("-" * 80)
    print(f"Total de alunos: {len(alunos)}")
    
    # Estatísticas
    aprovados = sum(1 for aluno in alunos if aluno.verificar_status() == "Aprovado")
    reprovados = len(alunos) - aprovados
    
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados por falta: {reprovados}")

def exibir_menu():
    # Exibe o menu principal do sistema"""
    print("\n" + "="*50)
    print("    SISTEMA DE CONTROLE DE FALTAS")
    print("="*50)
    print("1. Cadastrar aluno")
    print("2. Registrar falta")
    print("3. Listar todos os alunos")
    print("4. Buscar aluno específico")
    print("5. Sair")
    print("-" * 50)

def main():
    # Função principal do sistema
    while True:
        exibir_menu()
        
        try:
            opcao = input("Escolha uma opção (1-5): ").strip()
            
            if opcao == "1":
                cadastrar_aluno()
            elif opcao == "2":
                registrar_falta()
            elif opcao == "3":
                listar_todos_alunos()
            elif opcao == "4":
                buscar_aluno()
            elif opcao == "5":
                print("\nSaindo do sistema...")
                print("Obrigado por usar o Sistema de Controle de Faltas!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 5.")
        
        except KeyboardInterrupt:
            print("\n\nSaindo do sistema...")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

# Executar o programa
if __name__ == "__main__":
    main()