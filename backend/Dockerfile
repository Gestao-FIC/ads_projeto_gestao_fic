# Utilizar a imagem oficial do Python como base
FROM python:3.11-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements.txt para dentro do container
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código do projeto para o container
COPY . .

# Definir as variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expor a porta que o Django vai rodar (8000 por padrão)
EXPOSE 8000

# Rodar as migrações específicas do app 'sgset' e iniciar o servidor
CMD ["sh", "-c", "python manage.py makemigrations sgset && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]