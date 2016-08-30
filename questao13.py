base=int(input("Informe o valor a ser elevado: "))

expoente=int(input("Informe o valor que vai elevar o primeiro valor:"))

result = 1

for i in range(expoente):

    result *= base

print(result)
