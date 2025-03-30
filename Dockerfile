# Usar uma imagem Node.js como base
FROM node:16-alpine

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos de dependências
COPY package*.json ./

# Instalar dependências
RUN npm install

# Copiar todos os arquivos do projeto para o contêiner
COPY . .

# Expor a porta que o servidor vai usar
EXPOSE 3000

# Comando para iniciar a aplicação
CMD ["npm", "start"]
