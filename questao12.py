numero=eval(input("Informe um número de 1 a 10 para ver a tabuada: "))
if (numero<=10 and numero>=1):
	numero_final= numero*10
	mutiplica=0
	resultado=numero
	while (resultado<numero_final):
		mutiplica+=1 
		resultado=numero*mutiplica
		print(numero, "x", mutiplica,"=",resultado)
else:
	print("Valores inseridos inválidos")