def calcular_percentuais(faturamentos):
    # Calcula o valor total do faturamento
    total_faturamento = sum(faturamentos.values())
    
    # Calcula o percentual de cada estado
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamentos.items()}
    
    return percentuais, total_faturamento

def main():
    # Faturamento mensal por estado
    faturamentos = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    # Calcula os percentuais
    percentuais, total_faturamento = calcular_percentuais(faturamentos)
    
    # Exibe os resultados
    print(f"Valor total de faturamento: R${total_faturamento:.2f}")
    for estado, percentual in percentuais.items():
        print(f"Percentual de {estado}: {percentual:.2f}%")

if __name__ == '__main__':
    main()
