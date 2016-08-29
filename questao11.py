inicio=eval(input("Informe o valor inicial do intervalo:"))

fim=eval(input("informe o valor final do intervalo:"))

if(inicio<=fim):

	auxiliar=inicio+1

	soma=0
	while(auxiliar<fim):

		print(auxiliar)

		soma=auxiliar+soma

		auxiliar+=1

else:

	print("Valores informados inválidos")

print("O valor inicial era: ", inicio)

print("O valor final era: ", fim)

print("A soma dos intervalos é: ", soma)