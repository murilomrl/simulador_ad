import numpy as np
from math import sqrt
from Evento import Evento
import matplotlib.pyplot as plt
import time

##@class Simulador 
# @brief Simula uma Fila M/M/1 FCFS ou LCFS
# 
# Foi criada para ser o principal meio de simular uma fila M/M/1. A Classe Simulador começa definindo seus parâmetros iniciais e gera um evento chegada com uma distribuição Lambda. A partir desse evento novas chegadas são geradas e a simulação começa. Cada evento tem um tempo  de acontecimento e o loop principal de rodada verifica esse tipo para gerar novos eventos de acordo com as condições.
class Simulador:
    

	## Método construtor de Simulador que recebe e define as variáveis mi, rho e semente.
	# @param self Referência ao prório objeto.
	# @param mi Taxa de serviço.
	# @param rho Utilização do sistema.
	# @param semente Semente usada na função de geração de número aleatório.
    def __init__(self, mi, rho, semente):
        self.mi = mi
        self.rho = rho
        self.semente = semente

	## ...explicar o que a função faz...
	# @param self ...explicar a variavel...
	# @param numero_total_rodadas ...explicar variavel...
	# @param coletas_simulacao ...explicar variavel...
	# @return ...explicar o que essa função retorna...
    def t_student(self, lista, numero_total_rodadas, coletas_simulacao):
        media_w = round(sum(lista)/(numero_total_rodadas*coletas_simulacao),4)
        variancia = self.variancia(lista)
        limite_superior_t_student = media_w + 1.961*sqrt(variancia/numero_total_rodadas)
        limite_inferior_t_student = media_w - 1.961*sqrt(variancia/numero_total_rodadas)
        print("\nPrecisão t-Student: " + str((limite_superior_t_student - limite_inferior_t_student)/(limite_superior_t_student + limite_inferior_t_student)))
        print("\nIC da média t-Student:\nLimite Inferior: " + str(limite_inferior_t_student) + "\nLimite Superior: " + str(limite_superior_t_student))
        return (limite_superior_t_student,limite_inferior_t_student)
        
	## ...explicar o que a função faz...
	# @param self ...explicar a variavel...
	# @param lista ...explicar variavel...
	# @return ...explicar o que essa função retorna...
    def variancia(self, lista):
        n = len(lista)
        media_lista = sum(lista)/n
        variancia = 0.0
        for valor in lista:
            variancia += (valor - media_lista)**2
        return variancia/(n-1)

	## Comentário: Inicia os parêmetros e cria o primeiro evento de chegada da simulação.
	# @param self Referência ao prório objeto.
    def iniciar(self):
        inicio = time.time()
        taxa_chegada = self.rho/self.mi
        print(taxa_chegada)
        np.random.seed(self.semente)
        coletas_simulacao = 100
        tempo_simulacao = 0.0
        numero_total_rodadas = 3200
        rodadas_realizadas = 0
        numero_fregueses_fila = 0
        chegada_id = 0
        entrada_servico_id = 0
        saida_id = 0
        media_w = 0.0
        variancia_estimada_w = 0.0
        variancia_estimada_w_1 = 0.0
        variancia_estimada_w_2 = 0.0
        coletas_totais = 0
        lista_variancia = []
        fila_eventos = []
        lista_w = []
        random_num = np.random.rand()
        tempo_chegada = np.log(random_num)/(-taxa_chegada)
        evento = Evento("chegada", tempo_chegada, rodadas_realizadas)
        fila_eventos.append(evento)
        lista_entrada_servico = []
        lista_chegada = []
        lista_partidas = []
        fase_transiente = True
        media_espera_maxima = 0.0
        media_espera_minima = 0.0
        termino_fase_transiente = 0
        tempo_total = 0.0
        numero_em_espera = 0.0
        numero_fila_atual = 0.0
        variancia_estimada_fregueses = 0.0
        variancia_estimada_fregueses_1 = 0.0
        variancia_estimada_fregueses_2 = 0.0
        coletas_numero_espera = 0
        while rodadas_realizadas < numero_total_rodadas or fase_transiente == True:
            coletas_realizadas = 0
            while coletas_realizadas < coletas_simulacao and len(fila_eventos) > 0:
                evento = fila_eventos.pop(0)
                if evento.tipo == "chegada":
                    numero_fila_atual = numero_fregueses_fila* (evento.tempo - tempo_simulacao)
                    numero_em_espera += numero_fila_atual
                    coletas_numero_espera +=1
                    if coletas_numero_espera > 2:
                        variancia_estimada_fregueses_1 = (variancia_estimada_fregueses_1*(coletas_numero_espera-2) + numero_fila_atual**2)/(coletas_numero_espera-1)
                        variancia_estimada_fregueses_2 = (sqrt(variancia_estimada_fregueses_2*(coletas_numero_espera-1)*(coletas_numero_espera-2)) + numero_fila_atual)**2/(coletas_numero_espera*(coletas_numero_espera-1))
                    variancia_estimada_fregueses = variancia_estimada_w_1 - variancia_estimada_w_2
                    tempo_simulacao = evento.tempo
                    lista_chegada.append(evento)
                    numero_fregueses_fila += 1
                    chegada_id += 1
                    random_num = np.random.rand()
                    nova_chegada = np.log(random_num)/(-taxa_chegada)
                    tempo_chegada = tempo_simulacao + nova_chegada
                    evento = Evento("chegada", tempo_chegada, rodadas_realizadas)
                    fila_eventos.append(evento)

                    if numero_fregueses_fila == 1:						
                            evento = Evento("entrada_servico", tempo_simulacao, rodadas_realizadas)
                            fila_eventos.append(evento)
                            entrada_servico_id += 1

                elif evento.tipo == "partida":
                    numero_fila_atual = numero_fregueses_fila* (evento.tempo - tempo_simulacao)
                    numero_em_espera += numero_fila_atual
                    coletas_numero_espera +=1
                    if coletas_numero_espera > 2:
                        variancia_estimada_fregueses_1 = (variancia_estimada_fregueses_1*(coletas_numero_espera-2) + numero_fila_atual**2)/(coletas_numero_espera-1)
                        variancia_estimada_fregueses_2 = (sqrt(variancia_estimada_fregueses_2*(coletas_numero_espera-1)*(coletas_numero_espera-2)) + numero_fila_atual)**2/(coletas_numero_espera*(coletas_numero_espera-1))
                    variancia_estimada_fregueses = variancia_estimada_w_1 - variancia_estimada_w_2
                    tempo_simulacao = evento.tempo
                    lista_partidas.append(evento)
                    numero_fregueses_fila -= 1
                    if numero_fregueses_fila > 0:
                        if lista_chegada[entrada_servico_id].tempo < tempo_simulacao:
                            evento = Evento("entrada_servico", tempo_simulacao, rodadas_realizadas)
                            fila_eventos.append(evento)
                        else:
                            evento = Evento("entrada_servico", lista_chegada[entrada_servico_id].tempo, rodadas_realizadas)
                            fila_eventos.append(evento)
                        entrada_servico_id += 1
                else:
                    lista_entrada_servico.append(evento)
                    if evento.rodada == rodadas_realizadas:
                        coletas_realizadas += 1
                        coletas_totais += 1
                        w = lista_entrada_servico[entrada_servico_id-1].tempo - lista_chegada[entrada_servico_id-1].tempo
                        lista_w.append(w)
                        media_w += w/coletas_simulacao
                        if coletas_totais > 2:
                            variancia_estimada_w_1 = (variancia_estimada_w_1*(coletas_totais-2) + w**2)/(coletas_totais-1)
                            variancia_estimada_w_2 = (sqrt(variancia_estimada_w_2*(coletas_totais-1)*(coletas_totais-2)) + w)**2/(coletas_totais*(coletas_totais-1))
                        variancia_estimada_w = variancia_estimada_w_1 - variancia_estimada_w_2
                        lista_variancia.append(variancia_estimada_w)
                    random_num = np.random.rand()
                    nova_partida = np.log(random_num)/(-self.mi)
                    tempo_partida = evento.tempo + nova_partida
                    evento = Evento("partida", tempo_partida, rodadas_realizadas)
                    fila_eventos.append(evento)
                    saida_id += 1

            rodadas_realizadas += 1
            if coletas_totais == 190000:
                fase_transiente = False
                rodadas_realizadas = 0

	
        media_w = round(sum(lista_w[190000:])/(numero_total_rodadas*coletas_simulacao),4)
        #ITEM C
        numero_em_espera = numero_em_espera/tempo_simulacao
        #ITEM A
        limites_t_student_media_w = self.t_student(lista_w[190000:], numero_total_rodadas, coletas_simulacao)
        #ITEM B, VERIFICAR SOBREPOSICAO
        media_variancia = sum(lista_variancia[190000:])/(coletas_simulacao*numero_total_rodadas)
        limite_superior_chi_square = media_variancia*(numero_total_rodadas-1)/3045.1056
        limite_inferior_chi_square = media_variancia*(numero_total_rodadas-1)/3358.6827
        print("\nPrecisão Chi-square: " + str((limite_superior_chi_square - limite_inferior_chi_square)/(limite_superior_chi_square + limite_inferior_chi_square)))
        print("\nMedia : " + str(limite_inferior_chi_square + (limite_superior_chi_square - limite_inferior_chi_square)/2))
        print("\nIC da variancia Chi-square:\nLimite Inferior: " + str(limite_inferior_chi_square) + "\nLimite Superior: " + str(limite_superior_chi_square))
        limites_t_student_variancia = self.t_student(lista_variancia[190000:], numero_total_rodadas, coletas_simulacao)
        print(variancia_estimada_w)
        print(media_w)
        #ITEM D
        print(variancia_estimada_fregueses)

        #TEMPO DE SIMULAÇÃO
        print("\nTempo de simulação: " + str(time.time()-inicio))
        
        x = [media_variancia,media_variancia]
        y = [1,2]
        errors = [limites_t_student_variancia[0] - media_variancia, limite_superior_chi_square - media_variancia]

        plt.figure()
        plt.errorbar(x, y, xerr=errors, fmt = 'o', color = 'k')
        plt.yticks((0, 1, 2, 3 ),('','t_student variancia','Chi-square variancia', ''))
        '''
        x = [2, 4, 3]
        y = [1, 3, 5]
        errors = [0.5, 0.25, 0.75]

        plt.figure()
        plt.errorbar(x, y, xerr=errors, fmt = 'o', color = 'k')
        plt.yticks((0, 1, 3, 5, 6), ('', 'x3', 'x2', 'x1','')) 
        '''
        #plt.plot(lista_variancia)
        #plt.ylabel('Tempo de Espera')
        plt.show()

    ## Comentário: Inicia os parêmetros e cria o primeiro evento de chegada da simulação.
    # @param self Referência ao prório objeto.
    def iniciarLCFS(self):
        inicio = time.time()
        taxa_chegada = self.rho/self.mi
        print(taxa_chegada)
        np.random.seed(self.semente)
        coletas_simulacao = 100
        tempo_simulacao = 0.0
        numero_total_rodadas = 3200
        rodadas_realizadas = 0
        numero_fregueses_fila = 0
        chegada_id = 0
        entrada_servico_id = 0
        saida_id = 0
        media_w = 0.0
        variancia_estimada_w = 0.0
        variancia_estimada_w_1 = 0.0
        variancia_estimada_w_2 = 0.0
        coletas_totais = 0
        lista_variancia = []
        fila_eventos = []
        lista_w = []
        random_num = np.random.rand()
        tempo_chegada = np.log(random_num)/(-taxa_chegada)
        evento = Evento("chegada", tempo_chegada, rodadas_realizadas)
        fila_eventos.append(evento)
        lista_entrada_servico = []
        lista_chegada = []
        lista_partidas = []
        fase_transiente = True
        media_espera_maxima = 0.0
        media_espera_minima = 0.0
        termino_fase_transiente = 0
        tempo_total = 0.0
        numero_em_espera = 0.0
        numero_fila_atual = 0.0
        variancia_estimada_fregueses = 0.0
        variancia_estimada_fregueses_1 = 0.0
        variancia_estimada_fregueses_2 = 0.0
        coletas_numero_espera = 0
        while rodadas_realizadas < numero_total_rodadas or fase_transiente == True:
            coletas_realizadas = 0
            while coletas_realizadas < coletas_simulacao and len(fila_eventos) > 0:
                evento = fila_eventos.pop(0)
                if evento.tipo == "chegada":
                    numero_fila_atual = numero_fregueses_fila* (evento.tempo - tempo_simulacao)
                    numero_em_espera += numero_fila_atual
                    coletas_numero_espera +=1
                    if coletas_numero_espera > 2:
                        variancia_estimada_fregueses_1 = (variancia_estimada_fregueses_1*(coletas_numero_espera-2) + numero_fila_atual**2)/(coletas_numero_espera-1)
                        variancia_estimada_fregueses_2 = (sqrt(variancia_estimada_fregueses_2*(coletas_numero_espera-1)*(coletas_numero_espera-2)) + numero_fila_atual)**2/(coletas_numero_espera*(coletas_numero_espera-1))
                    variancia_estimada_fregueses = variancia_estimada_w_1 - variancia_estimada_w_2
                    tempo_simulacao = evento.tempo
                    lista_chegada.append(evento)
                    numero_fregueses_fila += 1
                    chegada_id += 1
                    random_num = np.random.rand()
                    nova_chegada = np.log(random_num)/(-taxa_chegada)
                    tempo_chegada = tempo_simulacao + nova_chegada
                    evento = Evento("chegada", tempo_chegada, rodadas_realizadas)
                    fila_eventos.append(evento)

                    if numero_fregueses_fila == 1:                      
                            evento = Evento("entrada_servico", tempo_simulacao, rodadas_realizadas)
                            fila_eventos.append(evento)
                            entrada_servico_id += 1

                elif evento.tipo == "partida":
                    numero_fila_atual = numero_fregueses_fila* (evento.tempo - tempo_simulacao)
                    numero_em_espera += numero_fila_atual
                    coletas_numero_espera +=1
                    if coletas_numero_espera > 2:
                        variancia_estimada_fregueses_1 = (variancia_estimada_fregueses_1*(coletas_numero_espera-2) + numero_fila_atual**2)/(coletas_numero_espera-1)
                        variancia_estimada_fregueses_2 = (sqrt(variancia_estimada_fregueses_2*(coletas_numero_espera-1)*(coletas_numero_espera-2)) + numero_fila_atual)**2/(coletas_numero_espera*(coletas_numero_espera-1))
                    variancia_estimada_fregueses = variancia_estimada_w_1 - variancia_estimada_w_2
                    tempo_simulacao = evento.tempo
                    lista_partidas.append(evento)
                    numero_fregueses_fila -= 1
                    if numero_fregueses_fila > 0:
                        if lista_chegada[len(lista_chegada)-entrada_servico_id].tempo < tempo_simulacao:
                            evento = Evento("entrada_servico", tempo_simulacao, rodadas_realizadas)
                            fila_eventos.append(evento)
                        else:
                            evento = Evento("entrada_servico", lista_chegada[len(lista_chegada)-entrada_servico_id].tempo, rodadas_realizadas)
                            fila_eventos.append(evento)
                        entrada_servico_id += 1
                else:
                    lista_entrada_servico.append(evento)
                    if evento.rodada == rodadas_realizadas:
                        coletas_realizadas += 1
                        coletas_totais += 1
                        w = lista_entrada_servico[entrada_servico_id-1].tempo - lista_chegada[len(lista_chegada)-entrada_servico_id].tempo
                        lista_w.append(w)
                        media_w += w/coletas_simulacao
                        if coletas_totais > 2:
                            variancia_estimada_w_1 = (variancia_estimada_w_1*(coletas_totais-2) + w**2)/(coletas_totais-1)
                            variancia_estimada_w_2 = (sqrt(variancia_estimada_w_2*(coletas_totais-1)*(coletas_totais-2)) + w)**2/(coletas_totais*(coletas_totais-1))
                        variancia_estimada_w = variancia_estimada_w_1 - variancia_estimada_w_2
                        lista_variancia.append(variancia_estimada_w)
                    random_num = np.random.rand()
                    nova_partida = np.log(random_num)/(-self.mi)
                    tempo_partida = evento.tempo + nova_partida
                    evento = Evento("partida", tempo_partida, rodadas_realizadas)
                    fila_eventos.append(evento)
                    saida_id += 1

            rodadas_realizadas += 1
            if coletas_totais == 190000:
                fase_transiente = False
                rodadas_realizadas = 0

        media_w = round(sum(lista_w[190000:])/(numero_total_rodadas*coletas_simulacao),4)
        #ITEM C
        numero_em_espera = numero_em_espera/tempo_simulacao
        #ITEM A
        limites_t_student_media_w = self.t_student(lista_w[190000:], numero_total_rodadas, coletas_simulacao)
        #ITEM B, VERIFICAR SOBREPOSICAO
        media_variancia = sum(lista_variancia[190000:])/(coletas_simulacao*numero_total_rodadas)
        limite_superior_chi_square = media_variancia*(numero_total_rodadas-1)/3045.1056
        limite_inferior_chi_square = media_variancia*(numero_total_rodadas-1)/3358.6827
        print("\nPrecisão Chi-square: " + str((limite_superior_chi_square - limite_inferior_chi_square)/(limite_superior_chi_square + limite_inferior_chi_square)))
        print("\nMedia : " + str(limite_inferior_chi_square + (limite_superior_chi_square - limite_inferior_chi_square)/2))
        print("\nIC da variancia Chi-square:\nLimite Inferior: " + str(limite_inferior_chi_square) + "\nLimite Superior: " + str(limite_superior_chi_square))
        limites_t_student_variancia = self.t_student(lista_variancia[190000:], numero_total_rodadas, coletas_simulacao)
        print(variancia_estimada_w)
        print(media_w)
        #ITEM D
        print(variancia_estimada_fregueses)

        #TEMPO DE SIMULAÇÃO
        print("\nTempo de simulação: " + str(time.time()-inicio))
        
        x = [media_variancia,media_variancia]
        y = [1,2]
        errors = [limites_t_student_variancia[0] - media_variancia, limite_superior_chi_square - media_variancia]

        plt.figure()
        plt.errorbar(x, y, xerr=errors, fmt = 'o', color = 'k')
        plt.yticks((0, 1, 2, 3 ),('','t_student variancia','Chi-square variancia', ''))
        '''
        x = [2, 4, 3]
        y = [1, 3, 5]
        errors = [0.5, 0.25, 0.75]

        plt.figure()
        plt.errorbar(x, y, xerr=errors, fmt = 'o', color = 'k')
        plt.yticks((0, 1, 3, 5, 6), ('', 'x3', 'x2', 'x1','')) 
        '''
        #plt.plot(lista_variancia)
        #plt.ylabel('Tempo de Espera')
        plt.show()
