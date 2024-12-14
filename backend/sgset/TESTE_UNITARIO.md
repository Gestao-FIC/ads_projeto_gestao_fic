# README

## Descrição

Este projeto implementa testes unitários automatizados utilizando o framework `pytest` para garantir a integridade e o comportamento correto da manipulação da base de dados da API. Os testes cobrem a criação, a validação e os tratamentos da instâncias dos modelos do sistema.

### Funcionalidades testadas:
- Criação e representação em string de cursos, turmas de cursos e horários de aulas.
- Associações entre modelos relacionados.
- Testes de integridade ao tentar criar objetos sem os campos obrigatórios.
- Testes de visualização de dados por meio de uma API, garantindo respostas HTTP corretas.

## Como executar

Para executar os testes, é necessário ter o Python e o Django configurados corretamente no ambiente. Siga os passos abaixo:

***⚠️ Certifique-se de ter o Docker instalado ⚠️*** 

1. **Clone o projeto**
    ```bash
        git clone https://github.com/Gestao-FIC/ads_projeto_gestao_fic.git
    ```

2. **Execute o container da API no Docker:**
   ```bash
    docker-compose up --build -d
   ```

3. **Veja os contêineres rodando**
    ```bash
        docker ps
    ```
    Procure pelo ID do contêiners baseado na imagem `ads_projeto_gestao_fic-backend`

4. **Se conecte com o terminal do contêiner**
    ```bash
        docker exec -it <container_id> /bin/bash
    ```

5. **Execute o teste**
    ```bash
        pytest
    ```

## Testes implementados

Foram implementados diversos testes, agrupados conforme os modelos. Os principais testes são:

1. **Modelos de Curso e Turma de Curso:**
- Verificação da criação e atributos dos modelos `Course` e `CourseClass`.
- Teste da string de representação dos objetos `Course` e `CourseClass`.


2. **Teste da criação do modelo DayOfWeek e sua representação em string**
- Modelos de `DayOfWeek` e `ClassSchedule`:
- Verificação da criação de `ClassSchedule` e as associações entre `CourseClass` e `DayOfWeek`.

3. **Testes de Integridade**
- Garantia de que a criação de `ClassSchedule` sem os campos obrigatórios (`class_instance` ou `day_of_week`) levanta um erro de IntegrityError.

4. **Testes da API de Instrutores**
- Verificação de requisições `GET` para listar os instrutores.
- Testes de requisições `POST` para criação de instrutores, com dados válidos e inválidos.

5. **Testes de Visualização e Respostas da API:**
- Testes de status HTTP adequados para as APIs.