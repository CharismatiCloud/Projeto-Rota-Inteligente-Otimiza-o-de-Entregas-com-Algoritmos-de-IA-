# main.py (Orquestrador)

import pandas as pd
import numpy as np
import random
import os
import matplotlib.pyplot as plt

# Importa as funções dos novos módulos
from src.clustering import preparar_dados, aplicar_kmeans
from src.route_optimization import heuristica, calcular_rota_gulosa_simples

# ====================================================================
# CONFIGURAÇÕES GLOBAIS (Mantidas no main para fácil acesso)
# ====================================================================
K_ENTREGADORES = 3
PONTO_RESTAURANTE = (0, 0)
OUTPUT_DIR = 'outputs'
DATA_DIR = 'data'
np.random.seed(42)
random.seed(42)

# Cria os diretórios para salvar os outputs e dados intermediários
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# ====================================================================
# ORQUESTRADOR PRINCIPAL
# ====================================================================

def otimizar_rotas_e_analisar(df_com_clusters):
    """Etapa 3: Otimização de Rotas e Análise de Desempenho."""
    print("\n--- 3. OTIMIZAÇÃO DE ROTAS (Heurística Gulosa) E ANÁLISE ---")
    
    distancia_total_otimizada = 0.0
    
    # Processa cada cluster
    for cluster_id in sorted(df_com_clusters['Cluster'].unique()):
        pontos_cluster = df_com_clusters[df_com_clusters['Cluster'] == cluster_id]
        
        # Usa a função renomeada
        rota, distancia = calcular_rota_gulosa_simples(pontos_cluster) 
        
        distancia_total_otimizada += distancia
        
        print(f"Cluster {cluster_id}: {len(pontos_cluster)} entregas. Distância Rota: {distancia:.2f} km.")

        # Geração do Gráfico da Rota (Importante para o README)
        plt.figure(figsize=(10, 8))
        
        # Prepara a lista de coordenadas (X, Y) para plotar
        rota_coords = rota[1:-1] # Exclui os dois pontos do restaurante
        
        # Plota a rota
        X_rota = [p[0] for p in rota]
        Y_rota = [p[1] for p in rota]
        plt.plot(X_rota, Y_rota, 'ro-', label=f'Rota Entregador {cluster_id+1}', alpha=0.6)
        
        # Plota pontos de entrega com rótulos
        for index, row in pontos_cluster.iterrows():
             plt.scatter(row['X'], row['Y'], marker='o', color='blue', s=100)
             plt.annotate(row['ID'], (row['X'] + 0.2, row['Y'] + 0.2))

        plt.scatter(PONTO_RESTAURANTE[0], PONTO_RESTAURANTE[1], marker='*', color='red', s=350, label='Restaurante')
        plt.title(f'Rota Otimizada - Entregador {cluster_id + 1} ({distancia:.2f} km)')
        plt.xlabel('Coordenada X')
        plt.ylabel('Coordenada Y')
        plt.grid(True, linestyle='--')
        plt.legend()
        plt.savefig(f'{OUTPUT_DIR}/rota_entregador_{cluster_id + 1}.png')
        plt.close()
    
    print("-" * 50)
    print(f"DISTÂNCIA TOTAL OTIMIZADA (K={K_ENTREGADORES}): {distancia_total_otimizada:.2f} km.")

    # Simulação da Rota Manual
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


if __name__ == '__main__':
    
    print("Iniciando o sistema de Rota Inteligente da Sabor Express...")
    
    # 1. Prepara os dados (Função importada)
    df_pedidos = preparar_dados(num_pedidos=15)
    
    # 2. Agrupa os dados com K-Means (Função importada)
    df_agrupado = aplicar_kmeans(df_pedidos, K_ENTREGADORES)
    print(f"Pedidos agrupados em {K_ENTREGADORES} clusters. Gráfico salvo em {OUTPUT_DIR}/kmeans_clusters.png.")
    
    # 3. Executa a otimização da rota para cada grupo
    otimizar_rotas_e_analisar(df_agrupado)
    
    print("\nProcesso de otimização finalizado. Verifique a pasta 'outputs' para os gráficos de agrupamento e rotas individuais.")