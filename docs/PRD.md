# PRD - Product Requirements Document

## Introdução & objetivo

Este sistema visa otimizar a alocação de docentes e o gerenciamento de turmas dos cursos de formação inicial e continuada (FIC) do SENAI, integrando dados do sistema legado SGSET em um dashboard visual para facilitar o acompanhamento e aprovação de cursos. O principal objetivo é centralizar as informações relacionadas aos cursos e docentes, permitindo uma tomada de decisão eficiente sobre a abertura de turmas com base em critérios de quórum e a gestão do alocamento de docentes aos cursos. A solução também melhora o processo de substituição de docentes em casos de imprevistos, e simplifica o planejamento de infraestrutura e materiais.


## Por que implementar isto?

O sistema surge da necessidade de evitar o gerenciamento manual e fragmentado das turmas e dos docentes, que atualmente envolve múltiplas planilhas e telas. A centralização dessas informações em um único painel visual reduz erros, economiza tempo e facilita o acompanhamento de metas financeiras, quórum de alunos e alocação de docentes. Além disso, o sistema permitirá uma visão clara do status das turmas, seja para cursos em andamento, prorrogados ou concluídos, além de gerar relatórios e ajustes manuais diretamente a partir dos dados.

---

## Público-alvo

Este sistema é direcionado principalmente para gestores do SENAI responsáveis pelo planejamento e execução dos cursos.

| Perfil de usuário | Descrição, necessidades e interesses. |
| --- | --- |
| Coordenador dos cursos FIC | Necessita de uma visão centralizada para aprovar a abertura de turmas, alocar docentes e gerenciar o calendário de cursos.  |
| Orientador de práticas profissionais |  Necessita visualizar o progresso alcançado em relação à metas anuais (cursos, matrículas e receita)  |


---

## Personas

> **Lucas, Coordenador dos cursos FIC**: Responsável por aprovar a abertura de turmas. Ele valoriza um dashboard claro com indicadores financeiros, quórum de alunos e visão de disponibilidade dos docentes. Lucas precisa de um sistema fácil de usar para evitar a navegação em múltiplas planilhas.


> **Felipe, Orientador de práticas profissionais:** Responsável por acompanhar o progresso anual de cursos, matrículas e receita gerada com os cursos realizados. Felipe valoriza uma visão clara e detalhada do quanto já foi alcançado em comparação às metas anuais.


---

## Requisitos Funcionais


### **F1. Dashboard visual com indicadores (cursos, matrículas, receita)**
- **Descrição:**  Exibir um dashboard com gráficos de progresso para cursos lecionados, matrículas e receita, comparando os valores atuais com as metas anuais. 
- **Critérios de Aceitação:**
    - Gráficos de progresso para cada métrica (quantidade de cursos, matrículas e receita total gerada).
- **Prioridade:** P1 


### **F2. Calendário de aulas dos docentes**
- **Descrição:**  Visualizar o calendário de aulas de um docente específico, com opção de edição do calendário.
- **Critérios de Aceitação:**
  - Exibir o calendário de cada docente, destacando os períodos reservados para cursos, datas letivas do SENAI, feriados (em vermelho), emendas (em amarelo) e eventos pessoais (em outras cores).
  - Incluir feriados municipais de Sorocaba e Itapetininga, de acordo com a cidade onde o docente leciona.
  - Permitir a edição do calendário com a inclusão de novas datas.
- **Prioridade:** P1


### **F3. Sistema de quórum para aprovação de turmas**
- **Descrição:** Visualizar o número de matrículas estimadas e efetivadas para cada curso. Ao atingir o ponto de equilíbrio de alunos (quórum), deve ser possível notificar automaticamente a secretaria escolar.
- **Critérios de Aceitação:**
    - Visualizar o número de matrículas estimadas e realizadas por curso.
    - Cadastrar o quórum para cada curso.
    - Indicar os cursos que atingiram o quórum (verde).
    - Opção de enviar um e-mail para a secretaria escolar quando o quórum for atingido.
- **Prioridade:** P1 


### **F4. Alocação de docentes**
- **Descrição:** Permitir a alocação manual de professores em cursos.
- **Critérios de Aceitação:**
  - Atribuir ou modificar o docente de um curso.
  - Caso haja diferença entre o docente alocado na plataforma e o registrado no SGSET, notificar o usuário do conflito, mas manter a atualização feita no software. 
- **Prioridade:** P1


### **F5. Relatório de materiais por cursos**
- **Descrição:** Gerar e exportar relatórios de materiais necessários para cada curso.
- **Critérios de Aceitação:**
  - Inserir materiais necessários para os cursos (campos por item: código, descrição e quantidade).
  - Calcular a quantidade total de materiais com base no número de alunos matriculados.
  - Permitir a exportação da lista de materiais por aluno em formato PDF.
- **Prioridade:** P2 



### Casos de uso

> **Caso de uso F1:** O coordenador de cursos ou o orientador de práticas profissionais o acessa o sistema e visualiza um dashboard que apresenta gráficos referentes a quantidade de cursos finalizados, o total de matrículas e a receita gerada. Ele compara os valores atuais com as metas anuais e utiliza essas informações para tomar decisões estratégicas sobre o andamento das atividades, priorizando os cursos com menor desempenho e ajustando os planos para alcançar as metas.

> **Caso de uso F2:** O coordenador seleciona um docente específico e visualiza seu calendário de aulas, que exibe as datas reservadas para cursos, feriados, emendas e eventos pessoais. Se necessário, ele pode editar o calendário, adicionando novas datas ou ajustando eventos já programados, garantindo a disponibilidade adequada do docente para lecionar.

> **Caso de uso F3:** O coordenador verifica o número de matrículas estimadas e realizadas para um curso específico no sistema. Ao constatar que o quórum mínimo foi atingido, o sistema destaca o curso em verde e permite o envio automático de uma notificação via e-mail para a secretaria escolar, confirmando a aprovação da turma.

> **Caso de uso F4:** O coordenador acessa a lista de cursos e atribui manualmente um docente a um curso específico. Caso o curso possua um docente diferente registrado no SGSET, o sistema deve notificar o conflito, mas persistir a modificação manual.

> **Caso de uso F5:** O coordenador atribui um novo item à lista de material de um curso, inserindo o código, a descrição e a quantidade. O sistema calcula a quantidade total com base no número de alunos matriculados e permite a exportação da lista de materiais em formato PDF, facilitando a distribuição aos responsáveis.



---

## Requisitos Não Funcionais

### **N1. Segurança**
- **Descrição:** O sistema deve utilizar a mesma autenticação do sistema legado SGSET, com atenção especial ao transporte seguro das credenciais entre os sistemas, garantindo a integridade e confidencialidade dos dados durante a transição.
- **Caso de uso:** Ao fazer login no novo sistema, o Coordenador utiliza suas credenciais do SGSET. O sistema autentica o usuário, transportando as credenciais de forma segura entre os sistemas sem comprometer a integridade dos dados, permitindo que o Coordenador acesse as funcionalidades sem precisar de um novo cadastro.


### **N2. Integridade dos Dados**
- **Descrição:** O sistema deve garantir a integridade dos dados recebidos do sistema SGSET, sincronizando corretamente as informações entre os dois sistemas para evitar inconsistências.
- **Caso de uso:** Quando o Coordenador acessa o sistema, ele visualiza as informações provenientes do SGSET, como os cursos ou o número de matrículas. 


### **N3. Disponibilidade**
- **Descrição:** O sistema deve estar disponível 99,9% do tempo, garantindo acesso contínuo, exceto durante manutenções programadas. Caso o sistema SGSET esteja indisponível, o sistema deve continuar funcionando e exibir a data e hora da última atualização dos dados, sem interromper o uso da aplicação.
- **Caso de uso:** O Coordenador acessa o sistema em diferentes momentos do dia para realizar suas tarefas, sem interrupções, exceto em manutenções planejadas. Se o sistema SGSET estiver temporariamente fora do ar, o Coordenador ainda pode continuar usando o sistema visualizando claramente a data e hora da última sincronização sem impactar suas atividades.


### **N4. Escalabilidade**
- **Descrição:** O sistema deve ser escalável para suportar um aumento de até 50% no número de dados, sem degradação significativa do desempenho.
- **Caso de uso:** A instituição amplia seu quadro de cursos e matrículas, resultando em um aumento significativo no número de dados processados. Mesmo com esse crescimento, o sistema continua funcionando de forma eficiente, sem quedas de desempenho.


### **N5. Manutenibilidade**
- **Descrição:** O sistema deve permitir a implementação de atualizações e correções de bugs de maneira eficiente, com impacto mínimo sobre os usuários.
- **Caso de uso:** Durante uma atualização de rotina para melhorar o desempenho do dashboard, a equipe de TI realiza a manutenção sem que os usuários experimentem interrupções significativas, garantindo que as melhorias possam ser aplicadas rapidamente e sem problemas.


### **N6. Compatibilidade**
- **Métrica:** O sistema deve ser compatível com os principais navegadores (Chrome, Firefox, Safari, Edge).
- **Tolerância:** 100% das funcionalidades principais devem estar disponíveis em todos os navegadores e dispositivos suportados, com no máximo 1% de falhas em dispositivos específicos.


## 📊 Métricas

| Medida                        | Esperado                  | Resultados                     |
|-------------------------------|---------------------------|--------------------------------|
| Segurança                     | 100% criptografia          |                                |
| Integridade dos Dados         | 100% consistência          |                                |
| Disponibilidade                | 99,9% uptime               |                                |
| Escalabilidade                | Suportar 50% mais dados    |                                |
| Manutenibilidade              | 95% sem impacto            |                                |
| Compatibilidade               | 100% funcionalidade        |                                |



---

## Fora de escopo

🚫 Integração com outros sistemas fora do SG7, como ERPs ou CRMs externos, ficará fora deste escopo inicial.

---

## User Experience

🖍️ [Link para o protótipo](https://www.figma.com/design/JiFxkPtXNBCjG1CGDuEBUG/GS7?node-id=0-1&t=rRbjzQz7rIeZv2Pp-1)

---

## Dependências

⚠️ Acesso aos dados do SG7, especialmente os cursos e docentes, é essencial para o funcionamento do sistema.

---

## Plano de lançamento

1. **Regras para lançamento interno:**
    - [ ] Validação com o cliente.



