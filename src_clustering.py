# src/clustering.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Funções que estavam no main.py, mas agora organizadas aqui
from main import PONTO_RESTAURANTE, OUTPUT_DIR, DATA_DIR

def preparar_dados(num_pedidos=15):
    """Geração dos dados de teste."""
    
    num_pedidos = 15
    pedidos_data = {
        'ID': [f'P{i+1}' for i in range(num_pedidos)],
        'X': np.random.uniform(-10, 10, num_pedidos).round(2),
        'Y': np.random.uniform(-10, 10, num_pedidos).round(2)
    }

    df_pedidos = pd.DataFrame(pedidos_data)
    df_pedidos.to_csv(f'{DATA_DIR}/pedidos.csv', index=False)
    
    return df_pedidos

def aplicar_kmeans(df_pedidos, K):
    """Aplicação do K-Means para agrupamento."""
    
    X = df_pedidos[['X', 'Y']]

    # n_init=10 é o valor padrão para versões mais antigas do scikit-learn
    kmeans = KMeans(n_clusters=K, random_state=42, n_init='auto') 
    df_pedidos['Cluster'] = kmeans.fit_predict(X)

    # Cria e salva o gráfico
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
    
    return df_pedidos