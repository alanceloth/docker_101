-- Criar tabela para armazenar dados
CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    data_venda DATE NOT NULL,
    produto VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL
);

-- Inserir dados de exemplo
INSERT INTO vendas (data_venda, produto, categoria, valor, quantidade)
VALUES 
  ('2025-01-15', 'Curso Python', 'Educação', 197.00, 45),
  ('2025-01-20', 'Assinatura BI', 'Software', 89.90, 28),
  ('2025-02-05', 'Consultoria', 'Serviços', 1200.00, 3),
  ('2025-02-12', 'Curso SQL', 'Educação', 147.00, 52),
  ('2025-03-01', 'Licença Tableau', 'Software', 999.00, 15);

-- Análise de vendas por categoria
SELECT 
    categoria,
    COUNT(*) AS total_vendas,
    SUM(valor * quantidade) AS receita_total,
    AVG(valor) AS ticket_medio
FROM vendas
GROUP BY categoria
ORDER BY receita_total DESC;