import heapq

# Grafo con costos

transporte = {
    "A": [("B", 1), ("D", 2)],  # directo más barato
    "B": [("A", 1), ("C", 1)],
    "C": [("B", 1), ("D", 1)],
    "D": [("A", 2), ("C", 1)]
}
"""
transporte = {
    "A": [("B", 1), ("D", 5)],  # directo más caro
    "B": [("A", 1), ("C", 1)],
    "C": [("B", 1), ("D", 1)],
    "D": [("A", 5), ("C", 1)]
}
"""

# Heurística (estimación al destino "D")
heuristica = {
    "A": 2,
    "B": 2,
    "C": 1,
    "D": 0
}

import heapq

def a_estrella(grafo, inicio, objetivo):
    cola = []
    heapq.heappush(cola, (0, 0, inicio, [inicio]))  
    # (prioridad, costo_real, nodo, ruta)

    visitados = set()

    while cola:
        (prioridad, costo_real, nodo, ruta) = heapq.heappop(cola)

        if nodo == objetivo:
            return ruta, costo_real

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino, peso in grafo[nodo]:
                nuevo_costo = costo_real + peso
                nueva_ruta = ruta + [vecino]
                nueva_prioridad = nuevo_costo + heuristica[vecino]

                heapq.heappush(cola, (nueva_prioridad, nuevo_costo, vecino, nueva_ruta))

    return None, float("inf")


# PRUEBA
ruta, costo = a_estrella(transporte, "A", "D")
#ruta, costo = a_estrella(transporte, "B", "D")


print("Ruta óptima:", ruta)
print("Costo total:", costo)
