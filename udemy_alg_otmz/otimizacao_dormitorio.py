import time
import random
import math
import otimizacao_engine

dormitorios = ['São Paulo', 'Flamengo', 'Coritiba', 'Cruzeiro', 'Fortaleza']

preferencias=[('Amanda', ('Cruzeiro', 'Coritiba')),
              ('Pedro', ('São Paulo', 'Fortaleza')),
              ('Marcos', ('Flamengo', 'São Paulo')),
              ('Priscila', ('São Paulo', 'Fortaleza')),
              ('Jessica', ('Flamengo', 'Cruzeiro')), 
              ('Paulo', ('Coritiba', 'Fortaleza')), 
              ('Fred', ('Fortaleza', 'Flamengo')), 
              ('Suzana', ('Cruzeiro', 'Coritiba')), 
              ('Laura', ('Cruzeiro', 'Coritiba')), 
              ('Ricardo', ('Coritiba', 'Flamengo'))]

dominio = [(0, len(dormitorios) * 2 -i -1)  for i in range(0, len(dormitorios) * 2)]

def imprimir_solucao(solucao):
  vagas = []
  for i in range(len(dormitorios)):
    vagas += [i,i]
  for i  in range(len(solucao)):
    atual = solucao[i]
    dormitorio = dormitorios[vagas[atual]]
    print(preferencias[i][0], dormitorio)
    del vagas[atual]

def funcao_custo(solucao):
  custo = 0
  vagas = [0,0, 1,1, 2,2, 3,3, 4,4]
  for i in range(len(solucao)):
    atual = solucao[i]
    dormitorio = dormitorios[vagas[atual]]
    preferencia = preferencias[i][1]
    if preferencia[0] == dormitorio:
      custo +=0
    elif preferencia[1] == dormitorio:
      custo +=1 
    else:
      custo += 3
  return custo


solucao_randomica = otimizacao_engine.pesquisa_randomica(dominio, funcao_custo)
custo_randomica = funcao_custo(solucao_randomica)
imprimir_solucao(solucao_randomica)

solucao_subida_encosta = otimizacao_engine.subida_encosta(dominio, funcao_custo)
custo_subida_encosta = funcao_custo(solucao_subida_encosta)
imprimir_solucao(solucao_subida_encosta)  

solucao_tempera = otimizacao_engine.tempera_simulada(dominio, funcao_custo)
custo_tempera = funcao_custo(solucao_tempera)
imprimir_solucao(solucao_tempera) 

solucao_genetico = otimizacao_engine.genetico(dominio, funcao_custo)
custo_genetico = funcao_custo(solucao_genetico)
imprimir_solucao(solucao_genetico)     

