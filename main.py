##@package main
# Função principal que importa e inicia Simulador

from Simulador import Simulador

## Variável simuladordo tipo Simulador que recebe como parâmetros de entrada mi, rho e uma semente de número aleatório. Normalmente um número primo grande é escolhido
simulador = Simulador(1,0.8,807)

## Função iniciar começa a simulação com os parâmetros mi, rho e semente.
simulador.iniciar()
