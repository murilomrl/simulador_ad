##@package main
# Função principal que importa e inicia Simulador

rho = input("\nDigite a utilização: ")

semente = input("\nDigite a semente: ") #9707 padrao


## Variável simuladordo tipo Simulador que recebe como parâmetros de entrada mi, rho e uma semente de número aleatório. Normalmente um número primo grande é escolhido
simulador = Simulador(1,rho,semente)


tipo_fila = input("Digite o tipo de fila FCFS ou LCFS:")


if tipo_fila.lower() == "fcfs":
	## Função iniciar começa a simulação com os parâmetros mi, rho e semente.
	simulador.iniciar()
elif tipo_fila.lower == "lcfs":
	## Função iniciar começa a simulação com os parâmetros mi, rho e semente.
	simulador.iniciarLCFS()
else:
	print("\nTipo de fila inválido!")
	exit()
