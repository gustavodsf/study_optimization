import time
import otimizacao_engine
import math


pessoas = [
            ('Amanda', 'CWB'),
            ('Pedro', 'GIG'),
            ('Marcos', 'POA'),
            ('Priscila', 'FLN'),
            ('Jessica', 'CNF'),
            ('Paulo', 'GYN')
          ]

destino = 'GRU'

voos = {}
for linha in open('voo.txt'):
  _origem, _destino, _saida, _chegada, _preco = linha.split(',')
  voos.setdefault((_origem,_destino), [])
  voos[_origem,_destino].append((_saida,_chegada, int(_preco)))


def imprimir_agenda(agenda):
  id_voo = -1
  for i in range(len(pessoas)):
    nome = pessoas[i][0]
    origem = pessoas[i][1]
    id_voo = id_voo + 1
    ida = voos[(origem, destino)][agenda[id_voo]]
    id_voo = id_voo + 1
    volta = voos[(destino, origem)][agenda[id_voo]]
    print('%10s%10s %5s-%5s R$%3s %5s-%5s R$%3s' %(nome, origem, ida[0], ida[1], ida[2], volta[0], volta[1], volta[2]))

def get_minutos(hora):
  x = time.strptime(hora, "%H:%M")
  minutos = x[3] * 60 + x[4]
  return minutos


def funcao_custo(solucao):
  preco_total = 0
  ultima_chegada = 0
  primeira_partida = 1439

  id_voo =  -1
  for i in range(len(solucao) // 2):
    origem = pessoas[i][1]
    id_voo +=1 
    ida = voos[(origem, destino)][solucao[id_voo]]
    id_voo +=1
    volta = voos[(destino, origem)][solucao[id_voo]]

    preco_total += ida[2]
    preco_total += volta[2]

    if ultima_chegada < get_minutos(ida[1]):
      ultima_chegada = get_minutos(ida[1])

    if primeira_partida > get_minutos(volta[0]):
      primeira_partida =  get_minutos(volta[0])

  total_espera = 0
  id_voo = -1
  for i  in range(len(solucao) //2):
    origem = pessoas[i][1]
    id_voo +=1 
    ida = voos[(origem, destino)][solucao[id_voo]]
    id_voo +=1
    volta = voos[(destino, origem)][solucao[id_voo]]

    total_espera += ultima_chegada - get_minutos(ida[1])
    total_espera += get_minutos(volta[0]) - primeira_partida
  
  if ultima_chegada > primeira_partida:
    preco_total += 50

  return preco_total + total_espera

dominio = [(0,9)] * (len(pessoas) * 2)

start_time = time.time()
solucao_genetica = otimizacao_engine.genetico(dominio, funcao_custo)
end_time = time.time()
print("Runtime GA: {:.2f}".format(end_time -  start_time))
custo_genetica = funcao_custo(solucao_genetica)
print("Custo: {}".format(custo_genetica))
imprimir_agenda(solucao_genetica)