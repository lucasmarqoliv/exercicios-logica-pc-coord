# Solicita os números do usuário
numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

# Calcula o produto do dobro do primeiro com metade do segundo
produto = (numero_inteiro1 * 2) * (numero_inteiro2 / 2)

# Calcula a soma do triplo do primeiro com o terceiro
soma = (numero_inteiro1 * 3) + numero_real

# Calcula o terceiro elevado ao cubo
cubo = numero_real ** 3

# Mostra os resultados
print("O produto do dobro do primeiro com metade do segundo é:", produto)
print("A soma do triplo do primeiro com o terceiro é:", soma)
print("O terceiro elevado ao cubo é:", cubo)
