# Diagramas de Engenharia de Software

## 1 Diagrama de Processos

```mermaid
sequenceDiagram
    participant Usuário
    participant SistemaEspelho
    participant SGSETNormalizer
    participant SGSET
    participant ETL
    participant Banco

    %% 1 - Login no Sistema
    Note over Usuário,SistemaEspelho: 1. Login no Sistema
    Usuário ->> SistemaEspelho: [1] Faz login no sistema espelho
    SistemaEspelho ->> SGSET: [2] Autentica usuário no SGSET
    SGSET ->> SistemaEspelho: [3] Confirmação de login bem-sucedido
    SistemaEspelho ->> Usuário: [4] Confirmação de login

    %% 2 - Download Automático de Documentos
    Note over SistemaEspelho,SGSET: 2. Download Automático de Documentos
    SistemaEspelho ->> SGSET: [5] Consulta automática (URL)
    SGSET ->> SistemaEspelho: [6] Resposta com documentos

    %% 3 - Normalização e Processamento de Dados
    Note over SistemaEspelho,SGSETNormalizer: 3. Envio para Tratamento e Normalização
    SistemaEspelho ->> SGSETNormalizer: [7] Envia documentos para normalização
    SGSETNormalizer ->> SGSETNormalizer: [8] Renomeia colunas e remove duplicatas
    SGSETNormalizer ->> ETL: [9] Envia dados normalizados para tratamento
    ETL ->> ETL: [10] Processa os Dados
    ETL ->> ETL: [11] Verifica divergências de dados
    ETL ->> Banco: [12] Salva dados tratados divergentes

    %% 4 - Consulta de Dados Consolidados
    Note over SistemaEspelho,Banco: 4. Consulta de Novos Dados
    SistemaEspelho ->> Banco: [13] Busca dados novos
    Banco ->> SistemaEspelho: [14] Dados Consolidados
    SistemaEspelho ->> SistemaEspelho: [15] Exibe no Dashboard
    SistemaEspelho ->> Usuário: [16] Visualização

    %% 5 - Inserção de Dados pelo Usuário
    Note over Usuário,SistemaEspelho: 5. Inserção de Dados
    Usuário ->> SistemaEspelho: [17] Inserir dados
    SistemaEspelho ->> Banco: [18] Persistir dados

    %% 6 - Consulta Personalizada
    Note over Usuário,SistemaEspelho: 6. Consulta de Dados pelo Usuário
    Usuário ->> SistemaEspelho: [19] Faz consulta
    SistemaEspelho ->> Banco: [20] Busca os dados (de acordo com o filtro)
    Banco ->> SistemaEspelho: [21] Envia dados
    SistemaEspelho ->> Usuário: [22] Visualização

```


## 2 Visão Física

```mermaid
graph TD;
    Usuario --> DOCKER[Docker Container];
    DOCKER[Docker Container] --> SGSET;
    
    subgraph DOCKER
        subgraph Backend_MVC
            
            View --> Service;
            Service --> Serializers;
            Serializers --> BD_Postgres;
        end
        
        subgraph Frontend_NextJS
            
            Pages --> Components;
            Pages --Requisicaoo--> View;
        end

        BD_Postgres[(Banco de Dados)]

    end;
```


## 3 Visão de Desenvolvimento

```mermaid
graph TD
    %% Estrutura geral do MVC com cada Model tendo sua View, Service e Serializer

    subgraph MVC
        %% Course
        CourseView["CourseView (Controller)"] --> CourseService["CourseService"];
        CourseService --> CourseSerializer["CourseSerializer"];
        CourseSerializer --> CourseModel["CourseModel"];
        CourseModel --> Database["BD_Postgres"];
        
        %% Course Class
        CourseClassView["CourseClassView (Controller)"] --> CourseClassService["CourseClassService"];
        CourseClassService --> CourseClassSerializer["CourseClassSerializer"];
        CourseClassSerializer --> CourseClassModel["CourseClassModel"];
        CourseClassModel --> Database;
        
        %% Instructor
        InstructorView["InstructorView (Controller)"] --> InstructorService["InstructorService"];
        InstructorService --> InstructorSerializer["InstructorSerializer"];
        InstructorSerializer --> InstructorModel["InstructorModel"];
        InstructorModel --> Database;
        
        %% Class Schedule
        ClassScheduleView["ClassScheduleView (Controller)"] --> ClassScheduleService["ClassScheduleService"];
        ClassScheduleService --> ClassScheduleSerializer["ClassScheduleSerializer"];
        ClassScheduleSerializer --> ClassScheduleModel["ClassScheduleModel"];
        ClassScheduleModel --> Database;
        
        %% Goal
        GoalView["GoalView (Controller)"] --> GoalService["GoalService"];
        GoalService --> GoalSerializer["GoalSerializer"];
        GoalSerializer --> GoalModel["GoalModel"];
        GoalModel --> Database;
        
        %% Event
        EventView["EventView (Controller)"] --> EventService["EventService"];
        EventService --> EventSerializer["EventSerializer"];
        EventSerializer --> EventModel["EventModel"];
        EventModel --> Database;
    end
```


