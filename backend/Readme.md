# SGSET - Sistema de Gestão
Este projeto é uma aplicação web desenvolvida com Django 5.1.2.

## Passo a Passo para Rodar o Projeto

### 1. Criar e Ativar um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- No Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- No Linux/macOS:
  ```bash
  source venv/bin/activate
  ```

### 2. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Executar o Servidor de Desenvolvimento

Após configurar tudo, execute o servidor de desenvolvimento com o comando:

```bash
python manage.py runserver
```

Acesse o projeto no navegador através da URL [http://127.0.0.1:8000](http://127.0.0.1:8000).