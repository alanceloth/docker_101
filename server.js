const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

// Servir arquivos estáticos da pasta raiz
app.use(express.static(path.join(__dirname)));

// Rota padrão serve o index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Iniciar o servidor
app.listen(PORT, () => {
  console.log(`Servidor Docker 101 rodando em http://localhost:${PORT}`);
  console.log('Pressione Ctrl+C para encerrar');
});
