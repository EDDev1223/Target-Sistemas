import json

def calcular_faturamento(faturamentos):
    # Remove os dias sem faturamento e extrai os valores
    valores = [f['valor'] for f in faturamentos if f['valor'] > 0]

    if not valores:
        return None, None, 0

    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    
    # Calcula a média mensal de faturamento
    media_mensal = sum(valores) / len(valores)
    
    # Conta o número de dias em que o faturamento foi superior à média mensal
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

def main():
    # Lê o arquivo JSON
    with open('C:\Users\edemi\OneDrive\Documentos\GitHub\Target-Sistemas\Faturamento\Faturamento.json', 'r') as file:
        data = json.load(file)
    
    faturamentos = data['Faturamento']
    
    # Calcula os valores
    menor, maior, dias_acima = calcular_faturamento(faturamentos)
    
    # Exibe os resultados
    if menor is not None:
        print(f"Menor valor de faturamento: R${menor:.2f}")
        print(f"Maior valor de faturamento: R${maior:.2f}")
        print(f"Número de dias com faturamento acima da média mensal: {dias_acima}")
    else:
        print("Não há faturamentos disponíveis para calcular.")

if __name__ == '__main__':
    main()
