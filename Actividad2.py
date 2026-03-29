import heapq

# Grafo con costos
transporte = {
    "A": [("B", 1), ("D", 2)],  # directo más barato
    "B": [("A", 1), ("C", 1)],
    "C": [("B", 1), ("D", 1)],
    "D": [("A", 2), ("C", 1)]
}

# Heurística (estimación al destino "D")
heuristica = {
    "A": 2,
    "B": 2,
    "C": 1,
    "D": 0
}

def a_estrella(grafo, inicio, objetivo):
    cola = []
    heapq.heappush(cola, (0, inicio, [inicio]))
    visitados = set()

    while cola:
        (costo, nodo, ruta) = heapq.heappop(cola)

        if nodo == objetivo:
            return ruta, costo

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino, peso in grafo[nodo]:
                nueva_ruta = ruta + [vecino]
                nuevo_costo = costo + peso
                prioridad = nuevo_costo + heuristica[vecino]

                heapq.heappush(cola, (prioridad, vecino, nueva_ruta))

    return None, float("inf")


# PRUEBA
ruta, costo = a_estrella(transporte, "B", "A")

print("Ruta óptima:", ruta)
print("Costo total:", costo)
