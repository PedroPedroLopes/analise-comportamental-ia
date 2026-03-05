-- Script de Gestão de Banco de Dados (SQL)
-- Desenvolvido por Pedro Lopes

-- 1. Analisando o engajamento de usuários por categoria
SELECT categoria, COUNT(*) as total_interacoes
FROM logs_treinamento_ia
WHERE data_analise > '2026-01-01'
GROUP BY categoria;

-- 2. Filtro de alta conversão para Dropshipping
SELECT produto_id, preco, taxa_conversao
FROM inventario_shopee
WHERE taxa_conversao > 0.05
ORDER BY taxa_conversao DESC;

-- 3. Triagem de padrões comportamentais frequentes
SELECT padrao_detectado, COUNT(id_sessao) as recorrencia
FROM analise_clinica_data
GROUP BY padrao_detectado
HAVING recorrencia > 10;
