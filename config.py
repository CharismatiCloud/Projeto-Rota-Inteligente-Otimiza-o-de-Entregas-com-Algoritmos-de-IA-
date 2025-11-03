# config.py
import numpy as np
import random
import os

# CONFIGURAÇÕES GLOBAIS
K_ENTREGADORES = 3
PONTO_RESTAURANTE = (0, 0)
OUTPUT_DIR = 'outputs'
DATA_DIR = 'data'

# Configurações de semente (seed)
np.random.seed(42)
random.seed(42)

# Cria os diretórios
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)