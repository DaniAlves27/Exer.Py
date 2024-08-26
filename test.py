# 1 Recebe dois dados do usuário
inf1 = input("Digite o primeiro dado: ")
inf2 = input("Digite o segundo dado: ")

# Concatena os dados em uma única string
resultado = inf1 + " " + inf2

# Exibe o resultado
print("O resultado é:", resultado)

#---------------------------------------------
# 2 Solicita uma string e um número inteiro como entrada
string_usuario = input("Digite uma string: ")
numero_usuario = int(input("Digite um número inteiro: "))

# Repete a string o número de vezes informado
resultado = string_usuario * numero_usuario

# Exibe o resultado
print("O resultado é:", resultado)

#---------------------------------------------
# 3 Solicita dois números como entrada
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Realiza uma operação simples entre os dois números
resultado = num1 + num2

# Exibe o resultado
print("O resultado é:", resultado)

#---------------------------------------------
#4 Recebe um número inteiro como entrada
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")

#---------------------------------------------
#5 Recebe as três notas como entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média
print("A média das notas é:", media)

#---------------------------------------------
# 6Recebe a palavra como entrada
palavra = input("Digite uma palavra: ")

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se a palavra é um palíndromo
if palavra == palavra_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo!")

