
# Gestão de Cursos e Docentes FIC

Este projeto é uma aplicação desenvolvida em Django para gerenciar cursos, turmas, docentes e suas interações. Ele foi criado para oferecer uma solução robusta para a administração de cursos e aulas, com foco na flexibilidade, rastreamento de metas e organização de cronogramas.

## 1 - Funcionalidades

- **Gerenciamento de Cursos**: Criação, edição e controle de informações de cursos, como preço por aluno e modalidades.
- **Gestão de Turmas**: Controle detalhado das turmas de cada curso, incluindo duração, modalidade, horários e status.
- **Alocação de Docentes**: Associação entre docentes e turmas, garantindo unicidade e rastreamento eficiente.
- **Metas e Planejamento**: Registro de metas anuais para cursos, matrículas e receitas.
- **Calendário e Eventos**: Gestão de reservas de datas, incluindo feriados, eventos e períodos de aulas.
- **Cronograma de Aulas**: Organização dos horários de aula com base nos dias da semana.
- **Gestão de Usuários**: Criação, atualização, exclusão e recuperação de usuários autenticados no sistema.

## 2 - Modelos Principais

### CourseModel
Representa um curso oferecido, como "Arduino" ou "Mecânico Ajustador".
- **id**: Identificador único.
- **name**: Nome do curso.
- **price_per_student**: Preço cobrado por aluno.

### CourseClassModel
Representa uma turma específica de um curso, incluindo informações sobre horários, modalidade e status.
- **code**: Código único da turma.
- **course**: Referência ao curso relacionado.
- **shift**: Turno (e.g., noturno).
- **duration**: Duração total em horas.
- **status**: Status atual da turma (e.g., programado, concluído).

### Instructor
Representa um docente responsável pelas aulas.
- **id**: Identificador único.
- **name**: Nome do docente.
- **source**: Origem do cadastro (e.g., SGSET, Usuário).

### ClassScheduleModel
Associa uma turma a um horário específico em determinado dia da semana.
- **id**: Identificador único.
- **class_instance**: Referência à turma.
- **day_of_week**: Dia da semana relacionado.

### Goal
Define metas anuais para cursos, matrículas ou receitas.
- **year**: Ano da meta.
- **goal_description**: Tipo de meta (e.g., cursos, matrículas).
- **value**: Valor esperado.

### EventModel
Gerencia reservas de datas para feriados, eventos ou períodos de aulas.
- **title**: Título da reserva (e.g., Feriado Nacional).
- **start_date**: Data de início.
- **end_date**: Data de término.
- **tag**: Categoria (e.g., feriado, curso).

### InstructorClass
Representa a relação entre um docente e uma turma específica.
- **instructor**: Referência ao docente.
- **course_class**: Referência à turma.

## 3 - Repositório de Usuários

O **UserRepository** é responsável por gerenciar as operações de CRUD (criação, recuperação, atualização e exclusão) para usuários autenticados. Ele utiliza o modelo padrão de usuários do Django.

### Principais Métodos

- **create_user**: Cria um novo usuário com nome, e-mail e senha.
- **get_user_by_id**: Recupera um usuário específico pelo ID. Retorna um erro se o usuário não for encontrado.
- **update_user**: Atualiza os detalhes de um usuário existente, incluindo senha, nome de usuário ou e-mail.
- **delete_user**: Exclui um usuário e retorna uma mensagem de confirmação.

## 4 - Serializadores (Serializers)

Os **serializers** traduzem os dados do modelo para formatos como JSON, permitindo a integração com APIs RESTful.

- **EventSerializer**: Serializa os eventos criados com o modelo **EventModel**, incluindo títulos, datas e categorias.
- **InstructorSerializer**: Converte os dados do modelo **Instructor** para JSON, utilizado para gerenciar os docentes do sistema.
- **AuthSerializer**: Utilizado para autenticação, recebe as credenciais do usuário (nome de usuário e senha) e valida os dados.
- **CourseSerializer**: Traduz os dados do modelo **CourseModel** para JSON, incluindo nome, ID e preço por aluno.
- **GoalSerializer**: Converte as metas anuais (**Goal**) para JSON, incluindo ano, descrição e valor esperado.
- **UpdateQuorumSerializer**: Permite a atualização do quorum de uma turma específica (**CourseClassModel**). Inclui validações como valores mínimos.

## 5 - Serviços (Services)

### CalendarService
Este serviço gerencia as operações relacionadas aos eventos no calendário, como criar, buscar, atualizar e excluir eventos.

- **Métodos principais**:
  - `create_event(data)`: Cria um novo evento com base nos dados fornecidos.
  - `get_event(event_id)`: Recupera um evento específico pelo ID.
  - `update_event(event_id, data)`: Atualiza as informações de um evento existente.
  - `delete_event(event_id)`: Exclui um evento pelo ID.
  - `list_events()`: Lista todos os eventos.

### InstructorService
Este serviço gerencia as operações relacionadas aos docentes, como criar, buscar, atualizar e excluir docentes.

- **Métodos principais**:
  - `create_instructor(data)`: Cria um novo docente com os dados fornecidos.
  - `get_instructor(instructor_id)`: Recupera um docente pelo ID.
  - `update_instructor(instructor_id, data)`: Atualiza as informações de um docente existente.
  - `delete_instructor(instructor_id)`: Exclui um docente pelo ID.
  - `list_instructors()`: Lista todos os docentes.

### UserService
Este serviço gerencia as operações relacionadas aos usuários do sistema, como criar, buscar, atualizar e excluir usuários.

- **Métodos principais**:
  - `create_user(data)`: Cria um novo usuário com base nos dados fornecidos.
  - `get_user(user_id)`: Recupera um usuário específico pelo ID.
  - `update_user(user_id, data)`: Atualiza as informações de um usuário existente.
  - `delete_user(user_id)`: Exclui um usuário pelo ID.

### AuthService
Este serviço gerencia a autenticação de usuários, validando as credenciais e gerando um token de autenticação.

- **Métodos principais**:
  - `authenticate_user(username, password)`: Valida as credenciais e retorna um token de autenticação.

### GoalService
Este serviço gerencia as operações relacionadas às metas anuais, como criar, buscar, atualizar e excluir metas.

- **Métodos principais**:
  - `create_goal(data)`: Cria uma nova meta com os dados fornecidos.
  - `get_goal(goal_id)`: Recupera uma meta pelo ID.
  - `update_goal(goal_id, data)`: Atualiza as informações de uma meta existente.
  - `delete_goal(goal_id)`: Exclui uma meta pelo ID.
  - `list_goals()`: Lista todas as metas.

## 6 - Views

As **views** implementam a lógica de apresentação e manipulação de dados no Django.

- **CourseView**: Responsável pela criação, leitura, atualização e exclusão de cursos.
  - `get()`: Lista todos os cursos disponíveis.
  - `post()`: Cria um novo curso.
  - `put()`: Atualiza um curso existente.
  - `delete()`: Exclui um curso.

- **CourseClassView**: Responsável pela criação, leitura, atualização e exclusão de turmas.
  - `get()`: Lista todas as turmas de um curso específico.
  - `post()`: Cria uma nova turma.
  - `put()`: Atualiza uma turma existente.
  - `delete()`: Exclui uma turma.

- **InstructorView**: Gerencia os docentes.
  - `get()`: Recupera informações de um docente.
  - `post()`: Cria um novo docente.
  - `put()`: Atualiza um docente existente.
  - `delete()`: Exclui um docente.

- **GoalView**: Responsável pela gestão das metas.
  - `get()`: Recupera as metas registradas.
  - `post()`: Cria uma nova meta.
  - `put()`: Atualiza uma meta existente.
  - `delete()`: Exclui uma meta.

## 7 - URLs da API

### Calendário e Eventos

- **GET** `/calendar/`: Lista eventos no calendário.
- **POST** `/calendar/`: Cria um novo evento.
- **GET** `/calendar/uuid:pk/`: Recupera detalhes de um evento específico.
- **PUT** `/calendar/uuid:pk/`: Atualiza um evento específico.
- **DELETE** `/calendar/uuid:pk/`: Exclui um evento específico.

### Docentes

- **GET** `/instructor/`: Lista todos os docentes.
- **POST** `/instructor/`: Cria um novo docente.
- **GET** `/instructor/uuid:Instructor_id/`: Recupera detalhes de um docente específico.
- **PUT** `/instructor/uuid:Instructor_id/`: Atualiza informações de um docente.
- **DELETE** `/instructor/uuid:Instructor_id/`: Exclui um docente específico.

### Autenticação

- **POST** `/login/`: Realiza o login do usuário e retorna

 um token de autenticação.

## 8 - Guia de Configuração da API no Computador Local

Este guia vai ajudar você a configurar e executar a API em seu computador local. Siga os passos abaixo para garantir que tudo esteja funcionando corretamente.

### A) Requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados no seu computador:

- **Python 3.8+**: Baixe e instale a partir do [site oficial do Python](https://www.python.org/downloads/).
- **Git**: Para clonar o repositório. Baixe e instale em [Git-scm.com](https://git-scm.com/).

### B) Clonar o Repositório

Abra o terminal e execute o seguinte comando para clonar o repositório da API:

```bash
git clone <URL_DO_REPOSITORIO>
```

Substitua `<URL_DO_REPOSITORIO>` pelo link do repositório Git.

### C) Criar e Ativar um Ambiente Virtual

Navegue até a pasta do projeto e crie um ambiente virtual para isolar as dependências do projeto:

```bash
cd nome_do_projeto
python -m venv .venv
```

Ative o ambiente virtual:

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```bash
  source .venv/bin/activate
  ```

### D) Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências do projeto que estão listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### E) Configurar o Arquivo `.env`

O projeto utiliza um arquivo `.env` para armazenar variáveis de ambiente, como a chave secreta do Django e as credenciais do superusuário.

- Copie o arquivo `.env.example` para `.env`:
  
  ```bash
  cp .env.example .env
  ```

- Abra o arquivo `.env` e preencha as informações necessárias, como `SECRET_KEY`, `DEBUG`, e as credenciais do superusuário.

### F) Aplicar Migrações ao Banco de Dados

Execute as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```

Esse comando criará um superusuário com base nas informações fornecidas no arquivo `.env`.

### G) Executar o Servidor de Desenvolvimento

Agora você pode iniciar o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

O servidor será iniciado em `http://127.0.0.1:8000/`. Você pode acessar esse endereço no navegador para testar a API.

### H) Testar a API

- Para testar o login, use um cliente REST como [Postman](https://www.postman.com/) ou [Insomnia](https://insomnia.rest/).
- Envie uma requisição POST para `/auth/login/` com `username` e `password` para obter o token de autenticação.
- Use o token para acessar as rotas protegidas.

### I) Desativar o Ambiente Virtual

Quando terminar de trabalhar, desative o ambiente virtual com o comando:

```bash
deactivate
```

## 9 - Problemas Comuns

- **Erro de Dependências**: Certifique-se de que todas as dependências estão instaladas corretamente com `pip install -r requirements.txt`.
- **Arquivo `.env` ausente**: Certifique-se de copiar e configurar o `.env` corretamente antes de rodar o servidor.


