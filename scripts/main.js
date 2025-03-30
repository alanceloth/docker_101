// Inicializar highlight.js para destacar a sintaxe de código
document.addEventListener('DOMContentLoaded', () => {
    hljs.highlightAll();
    
    // Ativar navegação por abas nos exemplos
    setupTabs();
    
    // Adicionar animação de scroll suave para links de âncora
    setupSmoothScroll();
});

// Configurar a funcionalidade de abas para os exemplos
function setupTabs() {
    // Não é necessário adicionar event listeners dinâmicos aqui
    // pois são adicionados diretamente no HTML via onclick
}

// Função para mostrar a aba selecionada
function showTab(tabId) {
    // Encontrar o container pai da aba
    const tabContent = document.getElementById(tabId);
    if (!tabContent) return;
    
    // Encontrar todos os conteúdos de aba no mesmo grupo
    const parentExample = tabContent.closest('.example');
    const allTabContents = parentExample.querySelectorAll('.tab-content');
    const allTabButtons = parentExample.querySelectorAll('.tab-button');
    
    // Esconder todos os conteúdos de aba
    allTabContents.forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Desativar todos os botões de aba
    allTabButtons.forEach(button => {
        button.classList.remove('active');
    });
    
    // Mostrar a aba selecionada
    tabContent.classList.add('active');
    
    // Ativar o botão correspondente
    const tabButton = parentExample.querySelector(`button[onclick="showTab('${tabId}')"]`);
    if (tabButton) {
        tabButton.classList.add('active');
    }
}

// Configurar rolagem suave para links de âncora
function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                // Ajuste para considerar a barra de navegação fixa
                const navHeight = document.querySelector('nav').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}
