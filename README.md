# Docker 101

[![Node.js](https://img.shields.io/badge/Node.js-18.x-green.svg)](https://nodejs.org/)
[![Express.js](https://img.shields.io/badge/Express-4.18.2-blue.svg)](https://expressjs.com/)
[![Docker](https://img.shields.io/badge/Docker-latest-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub last commit](https://img.shields.io/github/last-commit/alanceloth/docker_101.svg)](https://github.com/alanceloth/docker_101/commits/master)

Um projeto educacional sobre Docker para iniciantes. Este site apresenta conceitos básicos do Docker, seus benefícios e exemplos práticos de uso.

## Conteúdo

- O que é Docker
- Para que serve Docker
- Benefícios do uso de Docker
- Problemas que o Docker resolve
- Exemplos práticos de uso do Docker focados em ciência de dados:
  1. Dashboard de dados com Streamlit
  2. API de dados com FastAPI
  3. Banco de dados PostgreSQL
  4. Aplicação completa de análise de dados com Docker Compose

## Tecnologias

- ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
- ![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)
- ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Streamlit](https://img.shields.io/badge/streamlit-%23FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
- ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
- ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

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

## Exemplos com Docker

Para executar os exemplos de Docker apresentados no tutorial, você precisa ter o Docker instalado em seu sistema:

- [Instalação do Docker para Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Instalação do Docker para macOS](https://docs.docker.com/desktop/install/mac-install/)
- [Instalação do Docker para Linux](https://docs.docker.com/engine/install/)

## Autor

[![Alan Lanceloth](https://img.shields.io/badge/Alan%20Lanceloth-GitHub-black.svg)](https://github.com/alanceloth/)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
