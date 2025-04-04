// Função para adicionar botões de copiar a todos os blocos de código
document.addEventListener('DOMContentLoaded', function() {
    // Selecionar todos os elementos pre que contêm code
    const codeBlocks = document.querySelectorAll('pre');
    
    // Para cada bloco de código, adicionar um botão de copiar
    codeBlocks.forEach((preElement, index) => {
        // Verificar se há elemento code dentro do pre
        const codeElement = preElement.querySelector('code');
        if (!codeElement) return;
        
        // Criar o botão
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.textContent = 'Copiar';
        copyButton.title = 'Copiar para área de transferência';
        copyButton.dataset.index = index;
        
        // Adicionar o botão ao elemento pre
        preElement.classList.add('has-copy-button');
        preElement.appendChild(copyButton);
        
        // Adicionar evento de clique
        copyButton.addEventListener('click', function() {
            // Obter o conteúdo do código
            const code = codeElement.textContent;
            
            // Feedback visual durante a cópia
            copyButton.textContent = '...';
            
            // Usar a API de clipboard para copiar o texto
            navigator.clipboard.writeText(code)
                .then(() => {
                    // Feedback de sucesso
                    copyButton.textContent = 'Copiado!';
                    copyButton.classList.add('copied');
                    
                    // Restaurar o texto original após 2 segundos
                    setTimeout(() => {
                        copyButton.textContent = 'Copiar';
                        copyButton.classList.remove('copied');
                    }, 2000);
                })
                .catch(err => {
                    console.error('Erro ao copiar: ', err);
                    copyButton.textContent = 'Erro';
                    
                    // Restaurar o texto original após 2 segundos
                    setTimeout(() => {
                        copyButton.textContent = 'Copiar';
                    }, 2000);
                });
        });
    });
});
