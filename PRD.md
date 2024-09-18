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
| Gestores de Cursos | Necessitam de uma visão centralizada para aprovar a abertura de turmas, ajustar a alocação de docentes e gerenciar o calendário. |
| Coordenadores de Docentes | Precisam alocar os docentes de acordo com a demanda de cursos e identificar quando mudanças de professores são necessárias. |
| Assistentes Administrativos | Utilizam o sistema para emitir relatórios, acompanhar quórum e comunicar mudanças na programação das turmas. |

---

## Personas

1. **João, Gestor de Cursos**: Responsável por aprovar a abertura de turmas. Ele valoriza um dashboard claro com indicadores financeiros, quórum de alunos e visão de disponibilidade dos docentes. João precisa de um sistema fácil de usar para evitar a navegação em múltiplas planilhas.
2. **Maria, Coordenadora de Docentes**: Faz o acompanhamento dos horários dos docentes. Sua frustração é a falta de visibilidade clara de disponibilidade e sobreposição de horários. Ela quer poder ajustar rapidamente o cronograma e ver o status das turmas.
3. **Lucas, Assistente Administrativo**: Precisa de uma ferramenta para exportar relatórios e acompanhar o progresso das turmas. Lucas valoriza um sistema que automatize a geração de relatórios e facilite o ajuste de informações financeiras e de quórum.

---

## Requisitos Funcionais

1. **F1**: Dashboard visual com indicadores (cursos, matrículas, situação financeira). Deve permitir a visualização rápida do status das turmas e dos docentes. **P1**
2. **F2**: Alocação de docentes conforme o calendário predefinido. Permitir ajustes manuais para substituição de professores. **P1**
3. **F3**: Sistema de quórum para aprovação de turmas. Um botão de aprovação será ativado quando o número mínimo de alunos for atingido. **P1**
4. **F4**: Geração e exportação de relatórios de calendário e materiais necessários por curso. **P2**
5. **F5**: Notificações automáticas para gestores e assistentes quando uma turma atingir o número mínimo de alunos. **P2**

### Casos de uso

> **Caso de uso 1:** João acessa o dashboard, visualiza o número de matrículas em uma turma e aprova sua abertura ao atingir o número mínimo de alunos.
>
> **Caso de uso 2:** Maria verifica o calendário de docentes e realiza uma substituição manual para evitar sobreposição de horários.
>
> **Caso de uso 3:** Lucas gera um relatório de materiais necessários para uma turma específica e exporta o arquivo em PDF.

---

## Requisitos Não Funcionais

1. **NF1**: O sistema deve ser capaz de lidar com até 500 turmas e 200 docentes simultaneamente. **P1**
2. **NF2**: O sistema deve ser acessado por login integrado ao SG7, garantindo segurança para usuários autenticados. **P1**
3. **NF3**: Relatórios exportáveis em PDF e Excel, compatíveis com as normas de formato do SENAI. **P2**

### 📊 Métricas

| Medida | Estado atual | Esperado | Resultados |
| --- | --- | --- | --- |
| Tempo de carregamento | 5 segundos | Máximo 2 segundos |  |
| Quórum mínimo por turma | Varia | Mínimo 7 alunos |  |
| Número de relatórios gerados | Não disponível | Mínimo 10 por mês |  |

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
    - [ ] Validação com o cliente baseada no SG7.
    - [ ] Divulgação interna aos gestores do SENAI.

---

## 💌 Plano de comunicação

Comunicações serão feitas via e-mail e notificações no sistema para todos os gestores e assistentes administrativos. Uma série de e-mails será enviada informando sobre a aprovação de turmas, mudanças no calendário e relatórios gerados.
