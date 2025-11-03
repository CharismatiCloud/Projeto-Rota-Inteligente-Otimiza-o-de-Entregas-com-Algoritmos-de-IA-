# src/route_optimization.py

import numpy as np
from config import PONTO_RESTAURANTE

def heuristica(coord_atual, coord_destino):
    """Função Heurística h(n): Distância Euclidiana (Usada como custo g(n))."""
    return np.sqrt((coord_atual[0] - coord_destino[0])**2 + (coord_atual[1] - coord_destino[1])**2)

def calcular_rota_gulosa_simples(pontos_cluster):
    """
    IMPLEMENTAÇÃO GULOSA SIMPLIFICADA (TSP).
    A rota é determinada por uma ordenação simples (por X) dos pontos.
    """
    
    distancia_total_gn = 0.0
    rota_sugerida = [PONTO_RESTAURANTE]
    
    pontos_coord = [(row['X'], row['Y'], row['ID']) for _, row in pontos_cluster.iterrows()]
    
    # Heurística Gulosa: Ordena pela coordenada X
    pontos_coord.sort(key=lambda x: x[0]) 

    ponto_atual = PONTO_RESTAURANTE
    
    # Percorre os pontos na ordem determinada
    for x, y, id in pontos_coord:
        ponto_destino = (x, y)
        
        custo_segmento = heuristica(ponto_atual, ponto_destino) 
        
        distancia_total_gn += custo_segmento
        
        rota_sugerida.append(ponto_destino)
        ponto_atual = ponto_destino
        
    # Volta para o restaurante
    distancia_volta = heuristica(ponto_atual, PONTO_RESTAURANTE)
    distancia_total_gn += distancia_volta
    rota_sugerida.append(PONTO_RESTAURANTE)

    return rota_sugerida, distancia_total_gn