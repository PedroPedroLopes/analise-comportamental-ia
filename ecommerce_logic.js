// Script de Simulação de Conversão para Dropshipping
// Desenvolvido por Pedro Lopes

function calcularConversao(visitas, vendas) {
    if (visitas === 0) return "Aguardando tráfego...";
    
    let taxa = (vendas / visitas) * 100;
    let status = taxa > 2 ? "Alta Performance" : "Necessita Otimização de Criativo";
    
    return `Taxa de Conversão: ${taxa.toFixed(2)}% | Status: ${status}`;
}

// Exemplo de dados da loja Shopee
console.log(calcularConversao(1500, 45));
