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


"""
É APENAS TESTE PARA VER SE ESTÁ FUNCIONANDO CORRETAMENTE:
"""
# Lista para armazenar todos os alunos
alunos = [
    Aluno("Reynan", 20),
    Aluno("Arthur", 20),
    Aluno("Luana", 20),
    Aluno("José", 20),
    Aluno("Felipe", 20),
]
for aluno in alunos:
    print(aluno)
    aluno.adicionar_falta(6)
    print(aluno)
    print("="*50)
    print()

"""
=======================================================
"""  

# ===========================
# Arthur
# ===========================




# ===========================
# - Luana
# ===========================