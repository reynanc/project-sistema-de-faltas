## 👥 Divisão de Tarefas

### 👤 Reynan  
Responsabilidades **IMPLEMENTADAS**:
- ✅ Criou classe `Aluno` com atributos (nome, total_aulas, faltas)
- ✅ Implementou método `calcular_percentual_presenca()`
- ✅ Implementou método `verificar_status()` com regra de 75%
- ✅ Implementou método `adicionar_falta(quantidade)` com validação
- ✅ Implementou método `__str__()` para formatação de saída
- ✅ Criou lista global `alunos` para armazenamento

**Funcionalidades da Classe Aluno:**
- Construtor com parâmetros nome, total_aulas e faltas (padrão 0)
- Cálculo automático do percentual de presença
- Verificação de status (APROVADO/REPROVADO POR FALTA)
- Adição de faltas com limite máximo = total de aulas
- Representação string formatada com todas as informações

---

### 👤 Arthur 
Responsabilidades **PENDENTES**:
- ⏳ Função `registrar_falta(nome_aluno, qtd=1)` para buscar aluno e adicionar faltas
- ⏳ Função `buscar_aluno_por_nome(nome)` para localizar aluno específico
- ⏳ Função `listar_alunos_por_status()` para filtrar aprovados/reprovados
- ⏳ Validações de entrada (nome existe, quantidade válida)
- ⏳ Tratamento de erros para casos não encontrados

**Funcionalidades a Implementar:**
- Sistema de busca case-insensitive
- Registro de faltas com validação
- Relatórios de frequência por status
- Estatísticas gerais da turma

---

### 👤 Luana
Responsabilidades **PENDENTES**:
- ⏳ Menu principal interativo com opções:
  - Cadastrar novo aluno
  - Registrar falta
  - Listar todos os alunos
  - Buscar aluno específico
  - Relatórios e estatísticas
  - Sair do sistema
- ⏳ Função `cadastrar_aluno()` para entrada de dados
- ⏳ Função `exibir_relatorio_completo()` com formatação em tabela
- ⏳ Função `exibir_estatisticas()` (total, aprovados, reprovados)
- ⏳ Validações de interface (entradas vazias, números inválidos)
- ⏳ Loop principal do programa com tratamento de exceções

**Funcionalidades a Implementar:**
- Interface de linha de comando amigável
- Formatação de saída em tabelas
- Validação de entradas do usuário
- Sistema de navegação por menus
- Relatórios estatísticos formatados

---

## 📊 Status Atual do Projeto

### ✅ **CONCLUÍDO (Reynan)**
- Estrutura base da classe Aluno
- Lógica de cálculo de presença e status
- Sistema de adição de faltas
- Testes básicos funcionando

### ⏳ **EM DESENVOLVIMENTO**
- **Arthur**: Funções de busca e registro de faltas
- **Luana**: Interface do usuário e relatórios

### 🎯 **PRÓXIMOS PASSOS**
1. **Arthur** implementar funções de busca e registro
2. **Luana** criar interface e sistema de menus
3. Integrar todos os módulos
4. Testes finais e validações

---

## 🚀 Como Executar

**Estado Atual:**
```bash
python main.py
```
*Executa apenas os testes da classe Aluno*

**Após Conclusão:**
- Menu interativo completo
- Todas as funcionalidades integradas
- Sistema pronto para uso

---

## 📋 Requisitos Atendidos

- ✅ Cadastro de alunos (nome e total de aulas)
- ✅ Cálculo de percentual de presença  
- ✅ Regra de reprovação automática (< 75%)
- ✅ Estrutura para registro de faltas
- ⏳ Interface de usuário (em desenvolvimento)
- ⏳ Sistema de busca (em desenvolvimento)
- ⏳ Relatórios completos (em desenvolvimento)
