# Solicita ao usuário a quantidade de números
num_elementos = int(input("Quantos números deseja calcular a média? "))

# Inicializa uma variável para armazenar a soma dos números
soma = 0

# Solicita ao usuário que insira os números e os adiciona à soma
for i in range(num_elementos):
    numero = float(input(f"Digite o número {i + 1}: "))
    soma += numero

# Calcula a média
media = soma / num_elementos

# Exibe o resultado
print(f"A média dos {num_elementos} números é: {media}")
