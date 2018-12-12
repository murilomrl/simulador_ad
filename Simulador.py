import numpy as np
from math import sqrt
from Fregues import Fregues
from Evento import Evento
import matplotlib.pyplot as plt

##@class Simulador 
# @brief Simula uma Fila M/M/1 FCFS ou LCFS
# 
# Foi criada para ser o principal meio de simular uma fila M/M/1. A Classe Simulador começa definindo seus parâmetros iniciais e gera um evento chegada com uma distribuição Lambda. A partir desse evento novas chegadas são geradas e a simulação começa. Cada evento tem um tempo  de acontecimento e o loop principal de rodada verifica esse tipo para gerar novos eventos de acordo com as condições.
class Simulador:
    

	## Comentário: Método construtor de Simulador que recebe e define as variáveis mi, rho e semente.
	# @param self Referência ao prório objeto.
	# @param mi Taxa de serviço.
	# @param rho Utilização do sistema.
	# @param semente Semente usada na função de geração de número aleatório.
    def __init__(self, mi, rho, semente):
        self.mi = mi
        self.rho = rho
        self.semente = semente

        
	## Comentário: Calcula o tempo de espera na fila
	# @param self Referência ao prório objeto.
	# @param lista_chegada Lista de Eventos do tipo chegada.
	# @param lista_entrada_servico Lista de Eventos do tipo entrada_servico.
	# @return Retorna uma lista com o tempo de espera na fila de cada evento.
    def calcula_w(self, lista_chegada, lista_entrada_servico):
        i = 0
        lista_w = []
        for entrada_servico in lista_entrada_servico:
            w = entrada_servico.tempo - lista_chegada[i].tempo
            #if w < 0:
                #print("\nalerta\n")
                #print(i,lista_chegada[i],entrada_servico)
            lista_w.append(w)
            i+=1
        return lista_w[:]

	## Comentário: Inicia os parêmetros e cria o primeiro evento de chegada da simulação.
	# @param self Referência ao prório objeto.
    def iniciar(self):
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
        #variancia_total_w = 0.0
        variancia_estimada_w = 0.0
        variancia_estimada_w_1 = 0.0
        variancia_estimada_w_2 = 0.0
        variancia_anterior = 0.0
        coletas_totais = 0.0
        media_estimada = []
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
        while rodadas_realizadas < numero_total_rodadas:
            coletas_realizadas = 0
            while coletas_realizadas <= coletas_simulacao and len(fila_eventos) > 0:
                variancia_anterior = variancia_estimada_w
                #print(fila_eventos)
                evento = fila_eventos.pop(0)
                #print(evento)
                #print(numero_fregueses_fila)
                #if evento.rodada == rodadas_realizadas:
                if evento.tipo == "chegada":
                    #print("\nTempo Chegada: " + str(evento.tempo))
                    #print("\nChegou: " + str(evento.tempo))
                    tempo_simulacao = evento.tempo
                    lista_chegada.append(evento)
                    numero_fregueses_fila += 1
                    #print(numero_fregueses_fila)
                    chegada_id += 1
                    random_num = np.random.rand()
                    nova_chegada = np.log(random_num)/(-taxa_chegada)
                    #print("\nChegada: " + str(nova_chegada))
                    tempo_chegada = tempo_simulacao + nova_chegada
                    evento = Evento("chegada", tempo_chegada, rodadas_realizadas)
                    fila_eventos.append(evento)

                    if numero_fregueses_fila == 1:						
                            evento = Evento("entrada_servico", tempo_simulacao, rodadas_realizadas)
                            fila_eventos.append(evento)
                            entrada_servico_id += 1

                elif evento.tipo == "partida":
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
                        #coletas_totais += 1
                        w = lista_entrada_servico[entrada_servico_id-1].tempo - lista_chegada[entrada_servico_id-1].tempo
                        lista_w.append(w)
                        media_w += w/coletas_simulacao
                        if coletas_realizadas > 2:
                            variancia_estimada_w_1 = (variancia_estimada_w_1*(coletas_realizadas-2) + w**2)/(coletas_realizadas-1)
                            variancia_estimada_w_2 = (sqrt(variancia_estimada_w_2*(coletas_realizadas-1)*(coletas_realizadas-2)) + w)**2/(coletas_realizadas*(coletas_realizadas-1))
                        variancia_estimada_w = variancia_estimada_w_1 - variancia_estimada_w_2
                        #lista_variancia.append(variancia_estimada_w)
                        media_estimada.append(media_w*coletas_simulacao/coletas_realizadas)
                    #print("\nEntrou em serviço: " + str(evento.tempo))
                    random_num = np.random.rand()
                    nova_partida = np.log(random_num)/(-self.mi)
                    #print("\nPartida: " + str(nova_partida))
                    tempo_partida = evento.tempo + nova_partida
                    evento = Evento("partida", tempo_partida, rodadas_realizadas)
                    fila_eventos.append(evento)
                    saida_id += 1
            lista_variancia.append(variancia_estimada_w)
            variancia_estimada_w = 0.0
            variancia_estimada_w_1 = 0.0
            variancia_estimada_w_2 = 0.0
            #variancia_w = 0.0
            #for w in lista_w:
            #    variancia_w += (w - media_w)**2
            #variancia_total_w += round(variancia_w/(coletas_realizadas-1), 4)
            lista_w = []
            rodadas_realizadas += 1
        #print(lista_chegada,lista_entrada_servico)
        #lista_w = self.calcula_w(lista_chegada[:], lista_entrada_servico[:])
        #print(lista_w)
        #media_w = 0.0
        
        media_w = round(media_w/numero_total_rodadas,4)
        print(media_w)
        #print(variancia_total_w/numero_total_rodadas)
        print(variancia_estimada_w)
        plt.plot(lista_variancia)
        #plt.plot(media_estimada)
        plt.ylabel('Tempo de Espera')
        plt.show()
