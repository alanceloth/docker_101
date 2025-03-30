# Docker 101

Um projeto educacional sobre Docker para iniciantes. Este site apresenta conceitos básicos do Docker, seus benefícios e exemplos práticos de uso.

## Conteúdo

- O que é Docker
- Para que serve Docker
- Benefícios do uso de Docker
- Problemas que o Docker resolve
- Exemplos práticos de uso do Docker:
  1. Aplicação web simples
  2. Banco de dados
  3. Ambiente de desenvolvimento
  4. Aplicação multi-container com Docker Compose

## Como executar o projeto

### Pré-requisitos

Antes de começar, você precisa ter o Node.js instalado em seu sistema. Siga as instruções abaixo de acordo com seu sistema operacional:

#### Windows

1. Acesse [nodejs.org](https://nodejs.org/pt-br/)
2. Baixe a versão LTS (recomendada para a maioria dos usuários)
3. Execute o instalador e siga as instruções na tela
4. Para verificar se a instalação foi bem-sucedida, abra o Prompt de Comando (ou PowerShell) e digite:
   ```
   node --version
   npm --version
   ```

#### macOS

**Usando Homebrew (recomendado)**:
1. Se você não tem o Homebrew instalado, instale-o executando o seguinte comando no Terminal:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Instale o Node.js:
   ```bash
   brew install node
   ```

**Alternativa - Usando o instalador**:
1. Acesse [nodejs.org](https://nodejs.org/pt-br/)
2. Baixe a versão LTS para macOS
3. Execute o instalador e siga as instruções

#### Linux (Ubuntu/Debian)

```bash
# Atualizar os repositórios
sudo apt update

# Instalar o Node.js e npm
sudo apt install nodejs npm

# Verificar a instalação
node --version
npm --version
```

#### Linux (Fedora/RHEL/CentOS)

```bash
# Instalar o Node.js e npm
sudo dnf install nodejs npm

# Verificar a instalação
node --version
npm --version
```

### Executando o projeto

Depois de instalar o Node.js e o npm, siga estes passos para executar o projeto:

1. Clone ou baixe este repositório para sua máquina
2. Navegue até a pasta do projeto usando o terminal (Command Prompt, PowerShell, Terminal, etc.):
   ```bash
   # Windows
   cd caminho\para\docker_101
   
   # macOS/Linux
   cd caminho/para/docker_101
   ```

3. Instale as dependências:
   ```bash
   npm install
   ```

4. Inicie o servidor de desenvolvimento:
   ```bash
   npm start
   ```

5. Abra seu navegador em `http://localhost:3000` para ver o conteúdo.

6. Para encerrar o servidor, pressione `Ctrl+C` no terminal onde o servidor está rodando.

## Aprendendo Docker

Este projeto inclui exemplos práticos de uso do Docker. Para executar esses exemplos, você precisará instalar o Docker em sua máquina.

### Instalando o Docker

#### Windows
1. Acesse [Docker Desktop para Windows](https://www.docker.com/products/docker-desktop)
2. Baixe o instalador e siga as instruções
3. O Docker Desktop inclui o Docker Engine, o cliente Docker CLI, Docker Compose e outras ferramentas

#### macOS
1. Acesse [Docker Desktop para Mac](https://www.docker.com/products/docker-desktop)
2. Baixe a versão compatível com seu Mac (Intel ou Apple Silicon)
3. Instale normalmente arrastando para a pasta Applications

#### Linux
As instruções variam dependendo da distribuição. Consulte a [documentação oficial](https://docs.docker.com/engine/install/) para detalhes completos.

Para Ubuntu:
```bash
# Atualizar os repositórios
sudo apt update

# Instalar dependências
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Adicionar chave GPG do Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Adicionar repositório do Docker
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Atualizar o banco de dados de pacotes
sudo apt update

# Instalar Docker
sudo apt install docker-ce

# Adicionar seu usuário ao grupo docker (para não precisar usar sudo)
sudo usermod -aG docker $USER

# Necessário fazer logout e login novamente para que as mudanças sejam aplicadas
```

## Resolução de problemas

### Porta 3000 já em uso
Se ao iniciar o servidor você receber um erro dizendo que a porta 3000 já está em uso, você pode:

1. Encerrar o processo que está usando a porta 3000, ou
2. Mudar a porta usada pelo servidor editando o arquivo `server.js` e modificando a variável `PORT`

### Dependências não instaladas corretamente
Se você encontrar erros relacionados a dependências, tente:

```bash
# Limpar o cache do npm
npm cache clean --force

# Remover a pasta node_modules e o arquivo package-lock.json
rm -rf node_modules package-lock.json

# Instalar novamente
npm install
