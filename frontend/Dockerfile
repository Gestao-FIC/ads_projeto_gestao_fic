# Utilizando a imagem oficial do Node.js como base
FROM node:18-alpine AS base

# Definindo diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos de package.json e package-lock.json
COPY package.json package-lock.json ./

# Instalando as dependências do projeto
RUN npm install

# Copiando o restante dos arquivos do projeto para o container
COPY . .

# Compilando o projeto Next.js
RUN npm run build

# Utilizando uma segunda fase para criar uma imagem menor
FROM node:18-alpine AS production

# Definindo diretório de trabalho
WORKDIR /app

# Copiando apenas o necessário da fase anterior (dependências e build)
COPY --from=base /app/node_modules ./node_modules
COPY --from=base /app/package.json ./package.json
COPY --from=base /app/.next ./.next
COPY --from=base /app/public ./public

# Definindo a variável de ambiente para o modo produção
ENV NODE_ENV=production

# Expondo a porta que o Next.js utilizará
EXPOSE 3000

# Comando para rodar a aplicação no ambiente de produção
CMD ["npm", "start"]
