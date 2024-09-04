def calcular_faturamento(faturamentos):
    # Calcula o menor valor de faturamento
    menor_faturamento = min(faturamentos)
    
    # Calcula o maior valor de faturamento
    maior_faturamento = max(faturamentos)
    
    # Calcula a média mensal de faturamento
    media_mensal = sum(faturamentos) / len(faturamentos)
    
    # Conta o número de dias em que o faturamento foi superior à média mensal
    dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

# Exemplo de vetor com faturamentos diários (em reais)
faturamentos_diarios = [2500, 3000, 2900, 3200, 3100, 3300, 3400, 2500, 2700, 2800, 3000, 2900]

# Calcula os valores
menor, maior, dias_acima = calcular_faturamento(faturamentos_diarios)

# Exibe os resultados
print(f"Menor valor de faturamento: R${menor}")
print(f"Maior valor de faturamento: R${maior}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima}")
