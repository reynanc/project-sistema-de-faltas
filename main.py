# ===========================
# Projeto 5 – Sistema de Controle de Faltas
# ===========================

# ===========================
# Reynan
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
        # Verificar se o aluno está aprovado ou reprovado por falta
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
        return f"{self.nome} - Faltas: {self.faltas}/{self.total_aulas} - Presença: {self.calcular_percentual_presenca():.1f} % - {self.verificar_status()}"



# Lista para armazenar todos os alunos
alunos = []

# ===========================
# Arthur
# ===========================

def buscar_aluno_por_nome(nome: str):
    nome_clean = nome.strip().lower()
    for aluno in alunos:
        if aluno.nome.lower() == nome_clean:
            return aluno
    return None

def registrar_falta(nome_aluno: str, qtd: int = 1) -> bool:
    if not alunos:
        print("Erro: nenhum aluno cadastrado.")
        return False
    if not nome_aluno.strip():
        print("Erro: nome do aluno não pode ser vazio.")
        return False
    if qtd < 1:
        print("Erro: quantidade de faltas deve ser pelo menos 1.")
        return False

    aluno = buscar_aluno_por_nome(nome_aluno)
    if not aluno:
        print(f"Erro: aluno '{nome_aluno}' não encontrado.")
        return False

    aluno.adicionar_falta(qtd)
    print(f"Registradas {qtd} falta(s) para {aluno.nome}.")
    return True

def listar_alunos_por_status():
    if not alunos:
        print(" Nenhum aluno cadastrado.")
        return
    print("\n=== FILTRAR ALUNOS POR STATUS ===")
    print("1. Mostrar apenas aprovados")
    print("2. Mostrar apenas reprovados por falta")
    print("3. Mostrar todos")
    escolha = input("Escolha uma opção: ")
    resultado = {"APROVADO": [], "REPROVADO POR FALTA": []}
    for a in alunos:
        status = a.verificar_status()
        if status == "APROVADO":
            resultado["APROVADO"].append(a)
        else:
            resultado["REPROVADO POR FALTA"].append(a)
    if escolha == "1":
        print("\n--- Alunos Aprovados ---")
        for a in resultado["APROVADO"]:
            print(a)
    elif escolha == "2":
        print("\n--- Alunos Reprovados por Falta ---")
        for a in resultado["REPROVADO POR FALTA"]:
            print(a)
    elif escolha == "3":
        print("\n--- Todos os Alunos ---")
        for a in alunos:
            print(a)
    else:
        print(" Opção inválida.")

def estatisticas_avancadas():
    if not alunos:
        print(" Nenhum aluno cadastrado.")
        return
    total = len(alunos)
    total_faltas = sum(a.faltas for a in alunos)
    media_faltas = total_faltas / total if total > 0 else 0
    mais_faltas = max(alunos, key=lambda a: a.faltas)
    menos_faltas = min(alunos, key=lambda a: a.faltas)
    aprovados = len([a for a in alunos if a.verificar_status() == "APROVADO"])
    percentual_aprovacao = (aprovados / total) * 100 if total > 0 else 0

    print("\n=== ESTATÍSTICAS AVANÇADAS ===")
    print(f"Média de faltas por aluno: {media_faltas:.2f}")
    print(f"Aluno com mais faltas: {mais_faltas.nome} ({mais_faltas.faltas})")
    print(f"Aluno com menos faltas: {menos_faltas.nome} ({menos_faltas.faltas})")
    print(f"Percentual de aprovação da turma: {percentual_aprovacao:.1f}%")
    print("=" * 40)

# ===========================
# - Luana
# ===========================

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ").strip()
    if not nome or nome.isdigit():
        print(" Nome inválido. Não pode ser vazio ou apenas números.")
        return
    if any(char.isdigit() for char in nome):
        print(" Nome inválido. Não pode conter números.")
        return
    try:
        total_aulas = int(input("Digite o total de aulas da disciplina: "))
        if total_aulas <= 0:
            print(" O total de aulas deve ser maior que zero.")
            return
    except ValueError:
        print(" Entrada inválida. Digite um número inteiro.")
        return

    if buscar_aluno_por_nome(nome):
        print(" Aluno já cadastrado.")
        return

    novo = Aluno(nome, total_aulas)
    alunos.append(novo)
    print(f" Aluno {nome} cadastrado com sucesso!")


def exibir_relatorio_completo():
    if not alunos:
        print(" Nenhum aluno cadastrado.")
        return
    print("\n=== RELATÓRIO COMPLETO ===")
    print(f"{'Nome':<15}{'Faltas':<10}{'Total':<10}{'Presença%':<12}{'Status'}")
    print("-" * 60)
    for aluno in alunos:
        print(f"{aluno.nome:<15}{aluno.faltas:<10}{aluno.total_aulas:<10}{aluno.calcular_percentual_presenca():<12.1f}{aluno.verificar_status()}")
    print("=" * 60)


def exibir_estatisticas():
    if not alunos:
        print(" Nenhum aluno cadastrado.")
        return
    total = len(alunos)
    aprovados = len([a for a in alunos if a.verificar_status() == "APROVADO"])
    reprovados = total - aprovados
    print("\n=== ESTATÍSTICAS ===")
    print(f"Total de alunos: {total}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados por falta: {reprovados}")
    print("=" * 30)


def buscar_aluno():
    nome = input("Digite o nome do aluno que deseja buscar: ")
    aluno = buscar_aluno_por_nome(nome)
    if aluno:
        print(aluno)
    else:
        print(f" Aluno '{nome}' não encontrado.")


# ===========================
# Menu principal
# ===========================

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Cadastrar novo aluno")
        print("2. Registrar falta")
        print("3. Listar todos os alunos")
        print("4. Buscar aluno específico")
        print("5. Estatísticas")
        print("6. Filtrar alunos por status")
        print("7. Estatísticas avançadas")
        print("8. Sair do sistema")
        print("==========================")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                cadastrar_aluno()
            elif opcao == "2":
                if not alunos:
                    print("Erro: nenhum aluno cadastrado.")
                    continue
                nome = input("Digite o nome do aluno: ")
                try:
                    qtd = int(input("Digite a quantidade de faltas: "))
                except ValueError:
                    print(" Entrada inválida. Digite um número inteiro.")
                    continue
                registrar_falta(nome, qtd)
            elif opcao == "3":
                if not alunos:
                    print(" Nenhum aluno cadastrado.")
                else:
                    for aluno in alunos:
                        print(aluno)
            elif opcao == "4":
                buscar_aluno()
            elif opcao == "5":
                exibir_estatisticas()
            elif opcao == "6":
                listar_alunos_por_status()
            elif opcao == "7":
                estatisticas_avancadas()
            elif opcao == "8":
                print(" Saindo do sistema... Até logo!")
                break
            else:
                print(" Opção inválida. Tente novamente.")
        except Exception as e:
            print(f" Ocorreu um erro: {e}")


# ===========================
# Execução principal
# ===========================
if __name__ == "__main__":
    menu()
