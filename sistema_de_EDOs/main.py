# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:38:14 2026

@author: pinhe
"""

import rotinaP
import random

print('========== Solve de Sistema de Equações Diferenciais Ordinárias ==========')
ordem = int(input('Digite a ordem do sistema: '))
escolha = int(input('Digite 0 para gerar uma matriz aleatória / 1 para escolher os parâmetros: '))

if escolha == 0:

    matriz = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(random.uniform(0,10))
        matriz.append(linha)

elif escolha == 1:

    parametros = list(map(float,
        input('Digite os parametros (ex ordem 2: a11 a12 a21 a22): ').split()))
    matriz = [[0]*ordem for _ in range(ordem)]
    k = 0
    for i in range(ordem):
        for j in range(ordem):
            matriz[i][j] = parametros[k]
            k += 1

vetor_inicial = list(map(float, input('Digite o vetor y inicial (t=0): ').split()))
vetor_bias = list(map(float, input('Digite o vetor de bias: ').split()))
passo = float(input('Digite o passo de tempo: '))
tempo_simulacao = int(input('Digite o tempo de simulação: '))

rotinaP.solve(ordem, matriz, vetor_inicial, vetor_bias, passo, tempo_simulacao)