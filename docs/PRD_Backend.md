# Diagramas de Engenharia de Software

## 1 Diagrama de Processos

```mermaid
sequenceDiagram
    participant Usuário
    participant SistemaEspelho
    participant Selenium
    participant GRSET
    participant ETL
    participant Banco
  

    Usuário ->> SistemaEspelho: Faz login no sistema espelho
    SistemaEspelho ->> Selenium: Autentica usuário no GRSET (simultaneamente)
    Selenium ->> GRSET: Envia login e senha
    GRSET ->> Selenium: Login bem-sucedido
    
    Selenium ->> SistemaEspelho: Confirmação de login no sistema espelho e GRSET
    SistemaEspelho ->> Usuário: Confirmação

    SistemaEspelho ->> GRSET: Consulta genérica (URL)

  
    GRSET ->> SistemaEspelho: Resposta com docs

    SistemaEspelho ->> ETL: Dados Brutos

    ETL ->> ETL: Processar Dados

    ETL ->> ETL: Verifica divergências de dados

    ETL ->> Banco: Dados Tratados Divergentes

    Usuário ->> SistemaEspelho: Faz consulta
    
    SistemaEspelho ->> Banco: Busca os dados (de acordo com o filtro)

    Banco ->> SistemaEspelho: Envia dados

    SistemaEspelho ->> SistemaEspelho: Exibe no Dashboard

    SistemaEspelho ->> Usuário: Visualização

    Usuário ->> SistemaEspelho: Inserir dados

    SistemaEspelho ->> Banco: Persistir dados
```