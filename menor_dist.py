from collections import deque

def bfs(grafo, start, end):
    queue = deque() #fila
    visitado = set() #vertices visitados
    distancias = {start: 0} #mapeia cada vértice à sua distância do vértice de partida.
    caminho = {start: None}  # Dicionário para rastrear o caminho
    
    queue.append(start)
    visitado.add(start)
    
    while queue:
        vertice = queue.popleft()
        
        if vertice == end:
            return distancias[vertice], reconstruir_caminho(caminho, start, end)
        
        for vizinho in grafo[vertice]:
            if vizinho not in visitado:
                queue.append(vizinho)
                visitado.add(vizinho)
                distancias[vizinho] = distancias[vertice] + 1
                caminho[vizinho] = vertice
    
    return None, None

def reconstruir_caminho(caminho, start, end):
    caminho_percorrido = []
    vertice_atual = end
    
    while vertice_atual != start:
        caminho_percorrido.append(vertice_atual)
        vertice_atual = caminho[vertice_atual]
    
    caminho_percorrido.append(start)
    
    return ' -> '.join(reversed(caminho_percorrido))

# Exemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F', 'G'],
    'F': ['D', 'E', 'G'],
    'G': ['E', 'F', 'H', 'I'],
    'H': ['G', 'I'],
    'I': ['G', 'H'],
    'J': ['I', 'K'],
    'K': ['J', 'L'],
    'L': ['K']
}

start_vertice = 'A'
end_vertice = 'I'

distancia, caminho = bfs(grafo, start_vertice, end_vertice)

if distancia is not None:
    print(f"A distância mínima entre {start_vertice} e {end_vertice} é: {distancia}")
    print(f"Caminho percorrido: {caminho}")
else:
    print(f"Não há um caminho entre {start_vertice} e {end_vertice}.")
