# Etapa base para instalação de dependências
FROM node:18-alpine AS base

# Definindo o diretório de trabalho no container
WORKDIR /app

# Copiando arquivos necessários para instalar as dependências
COPY package.json ./

# Instalando apenas as dependências de produção
RUN npm install --production

# Copiando o restante dos arquivos do projeto
COPY . .

# Construindo o projeto Next.js
RUN npm run build

# Configurando a etapa final para a imagem de produção
FROM node:18-alpine AS final

# Definindo o diretório de trabalho no container
WORKDIR /app

# Copiando apenas o necessário da etapa anterior
COPY --from=base /app/node_modules ./node_modules
COPY --from=base /app/package.json ./package.json
COPY --from=base /app/.next ./.next
COPY --from=base /app/public ./public

# Configurando o ambiente de produção
ENV NODE_ENV=production

# Expondo a porta padrão usada pelo Next.js
EXPOSE 3000

# Comando padrão para iniciar o servidor em produção
CMD ["npm", "start"]
