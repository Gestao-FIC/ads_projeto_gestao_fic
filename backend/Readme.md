# Guia de Configuração da API no Computador Local

Este guia vai ajudar você a configurar e executar a API em seu computador local. Siga os passos abaixo para garantir que tudo esteja funcionando corretamente.

## 1. Requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados no seu computador:

- **Python 3.8+**: Baixe e instale a partir do [site oficial do Python](https://www.python.org/downloads/).
- **Git**: Para clonar o repositório. Baixe e instale em [Git-scm.com](https://git-scm.com/).

## 2. Clonar o Repositório

Abra o terminal e execute o seguinte comando para clonar o repositório da API:

```bash
git clone <URL_DO_REPOSITORIO>
```

Substitua `<URL_DO_REPOSITORIO>` pelo link do repositório Git.

## 3. Criar e Ativar um Ambiente Virtual

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

## 4. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências do projeto que estão listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 5. Configurar o Arquivo `.env`

O projeto utiliza um arquivo `.env` para armazenar variáveis de ambiente, como a chave secreta do Django e as credenciais do superusuário.

- Copie o arquivo `.env.example` para `.env`:
  
  ```bash
  cp .env.example .env
  ```

- Abra o arquivo `.env` e preencha as informações necessárias, como `SECRET_KEY`, `DEBUG`, e as credenciais do superusuário.

## 6. Aplicar Migrações ao Banco de Dados

Execute as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```

Esse comando criará um superusuário com base nas informações fornecidas no arquivo `.env`.

## 7. Executar o Servidor de Desenvolvimento

Agora você pode iniciar o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

O servidor será iniciado em `http://127.0.0.1:8000/`. Você pode acessar esse endereço no navegador para testar a API.

## 8. Testar a API

- Para testar o login, use um cliente REST como [Postman](https://www.postman.com/) ou [Insomnia](https://insomnia.rest/).
- Envie uma requisição POST para `/auth/login/` com `username` e `password` para obter o token de autenticação.
- Use o token para acessar as rotas protegidas.

## 9. Desativar o Ambiente Virtual

Quando terminar de trabalhar, desative o ambiente virtual com o comando:

```bash
deactivate
```

## Problemas Comuns

- **Erro de Dependências**: Certifique-se de que todas as dependências estão instaladas corretamente com `pip install -r requirements.txt`.
- **Arquivo `.env` ausente**: Certifique-se de copiar e configurar o `.env` corretamente antes de rodar o servidor.

## Contato

Se encontrar algum problema ou tiver dúvidas, entre em contato com o time de desenvolvimento ou abra uma *issue* no repositório.

---

Isso deve ser suficiente para configurar e executar a API em seu ambiente local. Boa sorte e qualquer coisa, é só perguntar! 😊

