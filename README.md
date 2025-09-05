## 👥 Divisão de Tarefas

### 👤 Reynan — Dados & Cadastro 
Responsabilidades:
- Criar classe `Aluno` (nome, total de aulas, faltas = 0)
- Implementar repositório para gerenciar alunos:
  - `adicionar_aluno(aluno)`
  - `obter_aluno_por_nome(nome)`
  - `listar_alunos()`
- Garantir que nomes não se repitam (case-insensitive)

---

### 👤 Arthur — Frequência & Busca
Responsabilidades:
- Função `registrar_falta(nome_aluno, qtd=1)`
- Calcular `percentual_presenca(aluno)`
- Determinar `status_por_frequencia(aluno, limite=75.0)`  
  → retorna **APROVADO** ou **REPROVADO**
- Aplicar regra de reprovação automática para presença < 75%

---

### 👤 Luana — Interface & Relatórios
Responsabilidades:
- Criar menus de texto:
  - Cadastrar aluno
  - Registrar falta
  - Listar alunos
  - Buscar aluno
  - Sair
- Conectar funções dos outros módulos
- Formatar a saída em tabela simples

---
