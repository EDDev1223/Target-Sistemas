def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    resultado = ""
    
    # Percorre a string original do final para o início
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    
    return resultado

def main():
    while True:
        # Solicita ao usuário para informar uma string
        entrada = input("Digite uma string para inverter (ou 'sair' para terminar): ")
        
        if entrada.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        # Inverte a string
        string_invertida = inverter_string(entrada)
        
        # Exibe o resultado
        print(f"String invertida: {string_invertida}")

if __name__ == '__main__':
    main()
