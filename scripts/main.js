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

// Função para alternar entre abas de conteúdo
function showTab(tabId) {
    // Encontrar o elemento da aba
    const selectedTab = document.getElementById(tabId);
    if (!selectedTab) return;
    
    // Determinar o tipo de aba e encontrar o contexto apropriado
    let context;
    if (tabId.includes('install')) {
        // Para abas de instalação (Windows/macOS/Linux)
        context = document.querySelector('.os-tabs').parentElement;
    } else if (selectedTab.closest('.example')) {
        // Para abas de exemplos
        context = selectedTab.closest('.example');
    } else {
        // Fallback para outros casos
        context = selectedTab.parentElement;
    }
    
    // Ocultar todas as abas de conteúdo no mesmo contexto
    const tabContents = context.querySelectorAll('.tab-content');
    tabContents.forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Desativar todos os botões de aba no mesmo contexto
    const tabButtons = context.querySelectorAll('.tab-button');
    tabButtons.forEach(button => {
        button.classList.remove('active');
    });
    
    // Mostrar a aba selecionada
    selectedTab.classList.add('active');
    
    // Ativar o botão correspondente
    const tabButton = context.querySelector(`button[onclick*="'${tabId}'"]`);
    if (tabButton) {
        tabButton.classList.add('active');
    }
}

// Função para alternar entre distribuições Linux
function showLinuxDistro(distroId) {
    // Ocultar todas as distribuições
    const distros = document.querySelectorAll('.linux-distro');
    distros.forEach(distro => {
        distro.classList.remove('active');
    });
    
    // Mostrar a distribuição selecionada
    const selectedDistro = document.getElementById(distroId);
    if (selectedDistro) {
        selectedDistro.classList.add('active');
    }
    
    // Atualizar os botões de distribuição
    const distroButtons = document.querySelectorAll('.distro-button');
    distroButtons.forEach(button => {
        button.classList.remove('active');
        if (button.getAttribute('onclick').includes(distroId)) {
            button.classList.add('active');
        }
    });
}

// Inicializar a página quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', function() {
    // Inicializar as abas com a primeira aba ativa
    const firstTabButtons = document.querySelectorAll('.code-tabs .tab-button:first-child');
    firstTabButtons.forEach(button => {
        if (!button.classList.contains('active')) {
            const onclickValue = button.getAttribute('onclick');
            if (onclickValue) {
                const tabId = onclickValue.replace("showTab('", "").replace("')", "");
                showTab(tabId);
            }
        }
    });
    
    // Inicializar as abas de distribuição Linux (se existirem)
    const distroButtons = document.querySelectorAll('.distro-button.active');
    distroButtons.forEach(button => {
        const onclickValue = button.getAttribute('onclick');
        if (onclickValue) {
            const distroId = onclickValue.replace("showLinuxDistro('", "").replace("')", "");
            showLinuxDistro(distroId);
        }
    });
});

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
