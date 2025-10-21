# main.py

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import deque 

# ====================================================================
# CONFIGURAÇÕES GLOBAIS
# ====================================================================
K_ENTREGADORES = 3
PONTO_RESTAURANTE = (0, 0)
OUTPUT_DIR = 'outputs'
DATA_DIR = 'data'
np.random.seed(42)
random.seed(42)

import os
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)


# ====================================================================
# FUNÇÕES CORE DE INTELIGÊNCIA ARTIFICIAL
# ====================================================================

def heuristica(coord_atual, coord_destino):
    """Função Heurística h(n): Distância Euclidiana."""
    return np.sqrt((coord_atual[0] - coord_destino[0])**2 + (coord_atual[1] - coord_destino[1])**2)

def encontrar_rota_a_star(pontos_cluster):
    """Simulação da Otimização de Rota usando a lógica do Algoritmo A* (VRP)."""
    
    distancia_total_gn = 0.0
    rota_sugerida = [PONTO_RESTAURANTE]
    
    pontos_coord = [(row['X'], row['Y'], row['ID']) for _, row in pontos_cluster.iterrows()]
    
    pontos_coord.sort(key=lambda x: x[0]) 

    ponto_atual = PONTO_RESTAURANTE
    
    for x, y, id in pontos_coord:
        ponto_destino = (x, y)
        
        custo_segmento = heuristica(ponto_atual, ponto_destino) 
        
        distancia_total_gn += custo_segmento
        
        rota_sugerida.append(ponto_destino)
        ponto_atual = ponto_destino
        
    distancia_volta = heuristica(ponto_atual, PONTO_RESTAURANTE)
    distancia_total_gn += distancia_volta
    rota_sugerida.append(PONTO_RESTAURANTE)

    return rota_sugerida, distancia_total_gn


# ====================================================================
# ORQUESTRADOR PRINCIPAL (MAIN)
# ====================================================================

def preparar_dados(num_pedidos=15):
    """Etapa 1: Geração dos dados de teste."""
    print("--- 1. PREPARAÇÃO DE DADOS ---")
    
    restaurante_coord = {'ID': 'Restaurante', 'X': PONTO_RESTAURANTE[0], 'Y': PONTO_RESTAURANTE[1]}
    
    num_pedidos = 15
    pedidos_data = {
        'ID': [f'P{i+1}' for i in range(num_pedidos)],
        'X': np.random.uniform(-10, 10, num_pedidos).round(2),
        'Y': np.random.uniform(-10, 10, num_pedidos).round(2)
    }

    df_pedidos = pd.DataFrame(pedidos_data)
    df_pedidos.to_csv(f'{DATA_DIR}/pedidos.csv', index=False)
    
    print(f"Gerados {num_pedidos} pedidos aleatórios em {DATA_DIR}/pedidos.csv.")
    return df_pedidos

def aplicar_kmeans(df_pedidos, K):
    """Etapa 2: Aplicação do K-Means para agrupamento."""
    print("\n--- 2. AGRUPAMENTO K-MEANS ---")
    
    X = df_pedidos[['X', 'Y']]

    kmeans = KMeans(n_clusters=K, random_state=42, n_init=10)
    df_pedidos['Cluster'] = kmeans.fit_predict(X)

    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(df_pedidos['X'], df_pedidos['Y'], c=df_pedidos['Cluster'], cmap='viridis', s=100)
    plt.scatter(PONTO_RESTAURANTE[0], PONTO_RESTAURANTE[1], marker='*', color='red', s=350, label='Restaurante')
    plt.title(f'Agrupamento de Pedidos com K-Means (K={K})')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(True, linestyle='--')
    plt.legend(*scatter.legend_elements(), title="Cluster")
    plt.savefig(f'{OUTPUT_DIR}/kmeans_clusters.png')
    plt.close()
    
    df_pedidos.to_csv(f'{DATA_DIR}/pedidos_com_clusters.csv', index=False)
    print(f"Pedidos agrupados em {K} clusters. Gráfico salvo em {OUTPUT_DIR}/kmeans_clusters.png.")
    
    return df_pedidos

def otimizar_rotas_e_analisar(df_com_clusters):
    """Etapa 3: Otimização de Rotas e Análise de Desempenho."""
    print("\n--- 3. OTIMIZAÇÃO DE ROTAS (A*) E ANÁLISE ---")
    
    distancia_total_otimizada = 0.0
    todas_as_rotas = {}

    for cluster_id in sorted(df_com_clusters['Cluster'].unique()):
        pontos_cluster = df_com_clusters[df_com_clusters['Cluster'] == cluster_id]
        
        rota, distancia = encontrar_rota_a_star(pontos_cluster)
        
        distancia_total_otimizada += distancia
        todas_as_rotas[cluster_id] = {'rota': rota, 'distancia': distancia}
        
        print(f"Cluster {cluster_id}: {len(pontos_cluster)} entregas. Distância Otimizada: {distancia:.2f} km.")
    
    print("-" * 50)
    print(f"DISTÂNCIA TOTAL OTIMIZADA (K={K_ENTREGADORES}): {distancia_total_otimizada:.2f} km.")

    df_manual = df_com_clusters.sort_values(by='ID')
    distancia_manual = 0.0
    ponto_atual_manual = PONTO_RESTAURANTE
    
    for _, row in df_manual.iterrows():
        ponto_destino_manual = (row['X'], row['Y'])
        distancia_manual += heuristica(ponto_atual_manual, ponto_destino_manual)
        ponto_atual_manual = ponto_destino_manual
    
    distancia_manual += heuristica(ponto_atual_manual, PONTO_RESTAURANTE) 

    print(f"DISTÂNCIA TOTAL MANUAL (SIMULADA): {distancia_manual:.2f} km.")
    
    economia_percentual = ((distancia_manual - distancia_total_otimizada) / distancia_manual) * 100
    print(f"ECONOMIA ESTIMADA PELO MODELO: {economia_percentual:.2f} %")