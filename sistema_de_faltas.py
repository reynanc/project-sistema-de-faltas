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

def listar_alunos_por_status() -> dict:
    aprovados = [a for a in alunos if a.verificar_status() == "APROVADO"]
    reprovados = [a for a in alunos if a.verificar_status() != "APROVADO"]
    return {"APROVADO": aprovados, "REPROVADO POR FALTA": reprovados}

# ===========================
# - Luana
# ===========================