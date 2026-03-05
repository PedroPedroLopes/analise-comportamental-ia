# Script de Análise de Padrões Linguísticos para IA
# Desenvolvido por Pedro Lopes - Psicólogo e Especialista em IA

def analisar_sentimento(texto):
    # Lista de termos que indicam equilíbrio e saúde mental
    positivos = ["equilíbrio", "consciência", "evolução", "saúde", "bem-estar", "analítica"]
    palavras = texto.lower().split()
    
    # Lógica de contagem de padrões detectados
    score = sum(1 for p in palavras if p in positivos)
    
    if score > 0:
        return f"Análise concluída: Padrão positivo detectado (Score: {score})"
    else:
        return "Análise concluída: Padrão neutro ou em observação para refinamento."

# Exemplo de processamento de linguagem natural (NLP)
entrada_exemplo = "Busco equilíbrio e consciência no meu processo de desenvolvimento analítico"
print(analisar_sentimento(entrada_exemplo))
