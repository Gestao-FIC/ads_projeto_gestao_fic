# PRD - Product Requirements Document

## Introdução & objetivo

Este sistema visa otimizar a alocação de docentes e o gerenciamento de turmas dos cursos de formação inicial e continuada (FIC) do SENAI, integrando dados do sistema legado SG7 em um dashboard visual para facilitar o acompanhamento e aprovação de cursos. O principal objetivo é centralizar as informações relacionadas aos cursos e docentes, permitindo uma tomada de decisão eficiente sobre a abertura de turmas com base em critérios de quórum e a gestão do alocamento de docentes aos cursos. A solução também melhora o processo de substituição de docentes em casos de imprevistos, e simplifica o planejamento de infraestrutura e materiais.


## Por que implementar isto?

O sistema surge da necessidade de evitar o gerenciamento manual e fragmentado das turmas e dos docentes, que atualmente envolve múltiplas planilhas e telas. A centralização dessas informações em um único painel visual reduz erros, economiza tempo e facilita o acompanhamento de metas financeiras, quórum de alunos e alocação de docentes. Além disso, o sistema permitirá uma visão clara do status das turmas, seja para cursos em andamento, prorrogados ou concluídos, além de gerar relatórios e ajustes manuais diretamente a partir dos dados.

---

## Público-alvo

Este sistema é direcionado principalmente para gestores do SENAI responsáveis pelo planejamento e execução dos cursos.

| Perfil de usuário | Descrição, necessidades e interesses. |
| --- | --- |
| Coordenador dos cursos FIC | Necessita de uma visão centralizada para aprovar a abertura de turmas, ajustar a alocação de docentes e gerenciar o calendário de cursos.  |


---

## Personas

> **Lucas, Coordenador dos cursos FIC**: Responsável por aprovar a abertura de turmas. Ele valoriza um dashboard claro com indicadores financeiros, quórum de alunos e visão de disponibilidade dos docentes. Lucas precisa de um sistema fácil de usar para evitar a navegação em múltiplas planilhas.
>

---

## Requisitos Funcionais


### **F1. Dashboard visual com indicadores (cursos, matrículas, receita)**
- **Descrição:**  Exibir um dashboard com gráficos de progresso para cursos lecionados, matrículas e receita, comparando os valores atuais com as metas anuais. 
- **Critérios de Aceitação:**
    - Gráficos de progresso para cada métrica (quantidade de cursos, matrículas e receita total gerada).
    - Comparação clara entre valor atual e meta anual.
- **Prioridade:** P1 (Alta)


### **F2. Calendário de aulas dos docentes**
- **Descrição:**  Visualizar o calendário de aulas de um docente específico, com opção de edição do calendário.
- **Critérios de Aceitação:**
    - Filtro para visualização individual do calendário de cada docente.
    - O calendário deve exibir: dias reservados para cursos, feriados (vermelho), emendas de feriado (amarelo), e eventos do ano letivo (outras cores).
    - Possibilidade de reservar datas customizadas.
- **Prioridade:** P1 (Alta)


### **F3. Sistema de quórum para aprovação de turmas**
- **Descrição:** Visualizar o número de matrículas estimadas e efetivadas para cada curso, com um esquema de cores para indicar o status de quórum. Ao atingir o quórum, deve ser possível notificar automaticamente a secretaria escolar.
- **Critérios de Aceitação:**
    - Visualizar o número de matrículas estimadas e realizadas por curso.
    - Indicar os cursos que atingiram o quórum mínimo (verde).
    - Enviar e-mail automatizado para a secretaria escolar quando o quórum for atingido.
- **Prioridade:** P1 (Alta)


### **F4. Alocação de docentes**
- **Descrição:** Permitir a alocação manual de professores em cursos.
- **Critérios de Aceitação:**
  - Atribuir um novo professor ao curso.
- **Prioridade:** P2 (Baixa)


### **F5. Relatório de materiais por cursos**
- **Descrição:** Gerar e exportar relatórios de materiais necessários para cada curso.
- **Critérios de Aceitação:**
  - Inserir materiais necessário para o curso (código, descrição e quantidade).
  - Calcular a quantidade total de materiais com base no número de alunos matriculados.
  - Permitir exportação da lista de materiais por aluno em formato PDF.
- **Prioridade:** P2 (Baixa)



### Casos de uso

> **Caso de uso F1:** Lucas acessa o dashboard para obter uma visão geral do desempenho dos cursos. Ele visualiza gráficos que mostram o número de cursos lecionados, matrículas e a receita gerada. Ao comparar os valores atuais com as metas anuais, Lucas pode identificar áreas que precisam de atenção.

> **Caso de uso F2:** Lucas deseja visualizar o calendário de um docente específico para planejar a alocação de aulas. Ele pode editar o calendário conforme necessário.

> **Caso de uso F3:** Lucas verifica o status de quórum das turmas, visualizando matrículas estimadas e efetivas. Quando uma turma atinge o quórum, ele pode notificar a secretaria escolar automaticamente.

> **Caso de uso F4:** Lucas precisa alocar um docente a um curso específico. Ele utiliza a funcionalidade de alocação manual.

> **Caso de uso F5:** Lucas precisa gerar um relatório dos materiais necessários para um curso específico, incluindo a quantidade com base nas matrículas.



---

## Requisitos Não Funcionais

1. **NF1**: O sistema deve ser capaz de lidar com até 500 turmas e 200 docentes simultaneamente. **P1**
2. **NF2**: O sistema deve ser acessado por login integrado ao SG7, garantindo segurança para usuários autenticados. **P1**
3. **NF3**: Relatórios exportáveis em PDF e Excel, compatíveis com as normas de formato do SENAI. **P2**

### 📊 Métricas

| Medida | Estado atual | Esperado | Resultados |
| --- | --- | --- | --- |
| Tempo de carregamento |  | Máximo 2 segundos |  |
| Quórum mínimo por turma |  | 51% |  |
| Número de relatórios gerados |  | Mínimo 10 por mês |  |

---

## Fora de escopo

🚫 Integração com outros sistemas fora do SG7, como ERPs ou CRMs externos, ficará fora deste escopo inicial.

---

## User Experience

🖍️ Link para fluxos UX/UI e protótipos: [Insira aqui o link para o fluxo UX]

---

## Dependências

⚠️ Acesso aos dados do SG7, especialmente o calendário de cursos e docentes, é essencial para o funcionamento do sistema.

---

## Plano de lançamento

1. **Regras para lançamento interno:**
    - [ ] Validação com o cliente.


---

## 💌 Plano de comunicação

Comunicações serão feitas via e-mail e notificações no sistema para todos os gestores e assistentes administrativos. Uma série de e-mails será enviada informando sobre a aprovação de turmas, mudanças no calendário e relatórios gerados.
