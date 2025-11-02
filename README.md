# ROTA INTELIGENTE: OTIMIZAÇÃO DE ENTREGAS COM ALGORITMOS DE IA

## 1. INTRODUÇÃO E OBJETIVOS

Este projeto propõe uma solução inteligente para a otimização logística em serviços de *delivery*. O foco é aplicar algoritmos clássicos de Inteligência Artificial para otimizar a distribuição de pedidos, melhorando a eficiência e reduzindo custos.

**Cliente:** Sabor Express (Empresa local de delivery de alimentos).

**Objetivo Central:** Desenvolver uma solução baseada em grafos e algoritmos de IA, capaz de sugerir as rotas mais eficientes para os entregadores, reduzindo atrasos e aumentando a satisfação dos clientes.

## 2. O DESAFIO

A empresa "Sabor Express" atua na região central da cidade e tem enfrentado grandes desafios no gerenciamento de entregas durante horários de pico. As rotas são definidas manualmente, resultando em rotas ineficientes que causam atrasos e aumento no custo de combustível.

A missão é utilizar a IA para encontrar o menor caminho entre múltiplos pontos de entrega e otimizar a alocação de pedidos.

## 3. ABORDAGEM METODOLÓGICA (SOLUÇÃO PROPOSTA)

A solução foi estruturada para lidar com o roteamento em duas fases, garantindo eficiência em situações de alta demanda:

### 3.1. Fase 1: Agrupamento Inteligente de Entregas (Clustering)
O algoritmo K-Means é utilizado para agrupar as entregas em zonas eficientes (*clusters*) a serem atribuídas a entregadores específicos.

### 3.2. Fase 2: Otimização do Caminho Mínimo
Para cada grupo (cluster), uma heurística de busca encontra o percurso ideal para visitar todos os pontos do cluster, minimizando a distância percorrida e o tempo de entrega entre os pontos.

## 4. ALGORITMOS DE INTELIGÊNCIA ARTIFICIAL

Os seguintes algoritmos de IA foram utilizados para resolver o problema computacional:

| Algoritmo | Área da IA | Aplicação no Projeto |
| :--- | :--- | :--- |
| **K-Means** | Aprendizado Não Supervisionado (Clustering) | Utilizado para agrupar as entregas em zonas eficientes, otimizando o trabalho dos entregadores. |
| **Heurística Gulosa Simplificada (TSP)** | Algoritmo de Busca Heurística | Encontra uma sequência de visitas para cada grupo (resolução simplificada do Problema do Caixeiro Viajante - TSP) após o K-Means, minimizando a distância percorrida. |
| **Representação por Grafos** | Estruturas de Dados e Lógica Algorítmica | A cidade é modelada como um grafo, onde os pontos são os locais de entrega (nós) e as arestas representam as ruas com pesos de distância ou tempo. |

## 5. ESTRUTURA E MODELO DO GRAFO

O modelo de dados implementado representa a topologia urbana da área de atuação da "Sabor Express".

* **Nós (Vértices):** Locais de entrega (com coordenadas X, Y).
* **Arestas (Pesos):** Ruas interligando os pontos, com peso baseado em distância (métrica Euclidiana) ou tempo estimado.

## 6. ANÁLISE DE RESULTADOS E EFICIÊNCIA

A avaliação da solução foi realizada comparando a rota otimizada pela IA com a gestão manual, utilizando métricas adequadas.

#### 6.1. Comparativo de Eficiência (Resultados da Simulação)

A simulação, utilizando 15 pedidos agrupados em 3 clusters, demonstrou uma melhoria significativa na logística.

| Cenário | Distância Total (Simulada) | Tempo Estimado (Simulado) |
| :--- | :--- | :--- |
| **Rota Manual (Baseada em Experiência)** | **159.62 km** | **319 min** |
| **Rota Inteligente (K-Means + Heurística)** | **83.71 km** | **167 min** |
| **Economia Estimada** | **47.55 %** | **47.55 %** |

**Visualização do Modelo:** O gráfico abaixo representa uma das rotas otimizadas para um dos entregadores, onde os pontos azuis são as entregas e a estrela vermelha é o restaurante.

<img width="1000" height="800" alt="kmeans_clusters" src="https://github.com/user-attachments/assets/d72531c4-cdf7-4b14-a9bb-ab887c8b2578" />


#### 6.2. Limitações e Sugestões de Melhoria

**Limitações Atuais:**
* **Simplificação do Roteamento (TSP):** A implementação da rota é baseada em uma heurística gulosa simplificada (ordenação por X), o que não garante o menor caminho global (Ótimo de Pareto).
* O modelo de grafo utiliza pesos estáticos, não incorporando dados de tráfego em tempo real.

**Sugestões de Melhoria (Pesquisa e Leitura):**
* **Roteamento Dinâmico:** Integrar dados de sensores IoT e tráfego em tempo real, utilizando algoritmos heurísticos mais avançados como Genéticos ou Aprendizado por Reforço (RL).
* **Otimização Contínua:** Explorar o uso de Programação Linear Inteira Mista (MILP) em conjunto com Clustering para otimização contínua de rotas e análise de território.
* **Recomendação de Leitura:** Estudo de caso da UPS - ORION (On-Road Integrated Optimization and Navigation).

## 7. INSTRUÇÕES DE EXECUÇÃO

O projeto é funcional e segue as instruções para sua execução.

#### 7.1. Pré-Requisitos

É necessário ter o **Python (versão 3.x)** instalado no ambiente.

#### 7.2. Instalação das Dependências

Instale as bibliotecas necessárias para o projeto:

````bash
pip install -r requirements.txt
````

7.3. Estrutura do Repositório
O código-fonte e os arquivos de dados estão organizados para fácil manutenção, demonstrando a visão sistêmica:
````
/
├── src/                  # Código-fonte principal e classes dos algoritmos (clustering.py, route_optimization.py)
├── data/                 # Arquivos de dados gerados (ex: CSVs com pedidos)
├── outputs/              # Imagens e gráficos gerados pela execução do código
├── requirements.txt      # Lista de bibliotecas necessárias
└── README.md             # Documentação do Projeto (Este arquivo)
````
7.4. Execução do Projeto
Para rodar a simulação e gerar a rota otimizada:
````
python main.py
````
8. AUTOR(ES)
Este projeto foi desenvolvido por:

Felipe Pardinho - GitHub: @CharismatiCloud - Email: felipepardinho9@gmail.com
