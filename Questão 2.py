def pertenceFibonacci(n):
    # Função para verificar se um número pertence à sequência de Fibonacci
    if n < 0:
        return False
    
    # Inicializando os dois primeiros valores da sequência de Fibonacci
    a, b = 0, 1
    
    # Verifica se n é um dos primeiros números da sequência
    if n == a or n == b:
        return True

    # Calcula a sequência de Fibonacci até o valor máximo de n
    while b <= n:
        a, b = b, a + b
        if b == n:
            return True
    
    return False

# Solicita ao usuário para inserir um número
while True:
    
    try:
        print("Olá, bem vindo a sequência de Fibonacci!") 
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci (ou digite '0' para sair): "))
        
        if pertenceFibonacci(numero):   
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
        
        # Interromper o Looping 
        if numero == 0:
            print("Saindo do programa.")
            break
    except ValueError:
        print("Por favor, insira um número válido.")