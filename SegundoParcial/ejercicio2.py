from math import inf

class NodoPila:
    def __init__(self, info=None, sig=None):
        self.info = info
        self.sig = sig


class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0


def apilar(pila, elemento):
    nodo = NodoPila(elemento, pila.cima)
    pila.cima = nodo
    pila.tamanio += 1


def desapilar(pila):
    elemento = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return elemento


def pila_vacia(pila):
    return pila.cima is None


def cima(pila):
    if pila.cima is None:
        return None
    return pila.cima.info


class NodoCola:
    def __init__(self, info=None, sig=None):
        self.info = info
        self.sig = sig


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def arribo_cola(cola, elemento):
    nodo = NodoCola(elemento)
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1


def atencion_cola(cola):
    elemento = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return elemento


def cola_vacia(cola):
    return cola.frente is None


def en_frente(cola):
    if cola.frente is None:
        return None
    return cola.frente.info


class Heap:
    def __init__(self):
        self.elementos = []
        self.tamanio = 0


def heap_vacio(heap):
    return heap.tamanio == 0


def intercambio(heap, i, j):
    heap.elementos[i], heap.elementos[j] = heap.elementos[j], heap.elementos[i]


def flotar(heap, indice):
    control = True
    while indice > 0 and control:
        padre = (indice - 1) // 2
        if heap.elementos[indice][0] < heap.elementos[padre][0]:
            intercambio(heap, indice, padre)
            indice = padre
        else:
            control = False


def hundir(heap, indice):
    hijo_izq = 2 * indice + 1
    control = True
    while hijo_izq < heap.tamanio and control:
        hijo_der = hijo_izq + 1
        menor = hijo_izq
        if hijo_der < heap.tamanio and heap.elementos[hijo_der][0] < heap.elementos[hijo_izq][0]:
            menor = hijo_der
        if heap.elementos[menor][0] < heap.elementos[indice][0]:
            intercambio(heap, indice, menor)
            indice = menor
            hijo_izq = 2 * indice + 1
        else:
            control = False


def agregar(heap, dato):
    heap.elementos.append(dato)
    heap.tamanio += 1
    flotar(heap, heap.tamanio - 1)


def quitar(heap):
    elemento = heap.elementos[0]
    heap.elementos[0] = heap.elementos[heap.tamanio - 1]
    heap.elementos.pop()
    heap.tamanio -= 1
    if heap.tamanio > 0:
        hundir(heap, 0)
    return elemento


def arribo_heap(heap, dato, prioridad):
    agregar(heap, [prioridad, dato])


def atencion_heap(heap):
    return quitar(heap)


def cambiar_prioridad(heap, indice, prioridad):
    anterior = heap.elementos[indice][0]
    heap.elementos[indice][0] = prioridad
    if prioridad < anterior:
        flotar(heap, indice)
    else:
        hundir(heap, indice)


class NodoArista:
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None


class Arista:
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


class NodoVertice:
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()


class Grafo:
    def __init__(self, dirigido=True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


def grafo_vacio(grafo):
    return grafo.inicio is None


def insertar_vertice(grafo, dato):
    nodo = NodoVertice(dato)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info < dato:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def agregar_arista(vertice, dato, destino):
    nodo = NodoArista(dato, destino)
    lista = vertice.adyacentes
    if lista.inicio is None or lista.inicio.destino > destino:
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while act is not None and act.destino < destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1


def buscar_vertice(grafo, clave):
    aux = grafo.inicio
    while aux is not None and aux.info != clave:
        aux = aux.sig
    return aux


def insertar_arista(grafo, dato, origen, destino):
    vertice_origen = buscar_vertice(grafo, origen)
    vertice_destino = buscar_vertice(grafo, destino)
    if vertice_origen is not None and vertice_destino is not None:
        agregar_arista(vertice_origen, dato, destino)
        if not grafo.dirigido:
            agregar_arista(vertice_destino, dato, origen)


def buscar_arista(vertice, destino):
    aux = vertice.adyacentes.inicio
    while aux is not None and aux.destino != destino:
        aux = aux.sig
    return aux


def es_adyacente(vertice, destino):
    return buscar_arista(vertice, destino) is not None


def marcar_no_visitado(grafo):
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig


def profundidad(grafo, vertice, resultado):
    vertice.visitado = True
    resultado.append(vertice.info)
    ady = vertice.adyacentes.inicio
    while ady is not None:
        siguiente = buscar_vertice(grafo, ady.destino)
        if not siguiente.visitado:
            profundidad(grafo, siguiente, resultado)
        ady = ady.sig


def barrido_profundidad(grafo, vertice_inicio):
    resultado = []
    aux = buscar_vertice(grafo, vertice_inicio)
    while aux is not None:
        if not aux.visitado:
            profundidad(grafo, aux, resultado)
        aux = aux.sig
    return resultado


def barrido_amplitud(grafo, vertice_inicio):
    resultado = []
    pendientes = Cola()
    aux = buscar_vertice(grafo, vertice_inicio)
    while aux is not None:
        if not aux.visitado:
            aux.visitado = True
            arribo_cola(pendientes, aux)
            while not cola_vacia(pendientes):
                nodo = atencion_cola(pendientes)
                resultado.append(nodo.info)
                ady = nodo.adyacentes.inicio
                while ady is not None:
                    siguiente = buscar_vertice(grafo, ady.destino)
                    if not siguiente.visitado:
                        siguiente.visitado = True
                        arribo_cola(pendientes, siguiente)
                    ady = ady.sig
        aux = aux.sig
    return resultado


def existe_paso(grafo, origen, destino):
    resultado = []
    inicio = buscar_vertice(grafo, origen)
    if inicio is not None:
        profundidad(grafo, inicio, resultado)
    return destino in resultado


def buscar_en_heap(heap, clave):
    pos = None
    i = 0
    while i < heap.tamanio and pos is None:
        if heap.elementos[i][1][0].info == clave:
            pos = i
        i += 1
    return pos


def dijkstra(grafo, origen, destino):
    no_visitados = Heap()
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info == origen:
            arribo_heap(no_visitados, [aux, None], 0)
        else:
            arribo_heap(no_visitados, [aux, None], inf)
        aux = aux.sig
    continuar = True
    while continuar and not heap_vacio(no_visitados):
        dato = atencion_heap(no_visitados)
        if dato[0] == inf:
            continuar = False
        else:
            apilar(camino, dato)
            if dato[1][0].info == destino:
                continuar = False
            else:
                ady = dato[1][0].adyacentes.inicio
                while ady is not None:
                    pos = buscar_en_heap(no_visitados, ady.destino)
                    if pos is not None:
                        nuevo = dato[0] + ady.info
                        if nuevo < no_visitados.elementos[pos][0]:
                            no_visitados.elementos[pos][1][1] = dato[1][0].info
                            cambiar_prioridad(no_visitados, pos, nuevo)
                    ady = ady.sig
    return camino


def agregar_aristas_disponibles(grafo, vertice, aristas):
    ady = vertice.adyacentes.inicio
    while ady is not None:
        destino = buscar_vertice(grafo, ady.destino)
        if not destino.visitado:
            arribo_heap(aristas, [vertice.info, ady.destino], ady.info)
        ady = ady.sig


def prim(grafo, origen):
    bosque = []
    marcar_no_visitado(grafo)
    inicio = buscar_vertice(grafo, origen)
    if inicio is not None:
        aristas = Heap()
        inicio.visitado = True
        agregar_aristas_disponibles(grafo, inicio, aristas)
        while not heap_vacio(aristas):
            elemento = atencion_heap(aristas)
            peso = elemento[0]
            vertice_origen = elemento[1][0]
            vertice_destino = buscar_vertice(grafo, elemento[1][1])
            if not vertice_destino.visitado:
                vertice_destino.visitado = True
                bosque.append([vertice_origen, vertice_destino.info, peso])
                agregar_aristas_disponibles(grafo, vertice_destino, aristas)
    return bosque


TOTAL_EPISODIOS = 9

APARICIONES = {
    "Luke Skywalker": [3, 4, 5, 6, 7, 8, 9],
    "Darth Vader": [3, 4, 5, 6],
    "Yoda": [1, 2, 3, 5, 6, 8, 9],
    "Boba Fett": [2, 5, 6],
    "C-3PO": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Leia": [3, 4, 5, 6, 7, 8, 9],
    "Rey": [7, 8, 9],
    "Kylo Ren": [7, 8, 9],
    "Chewbacca": [3, 4, 5, 6, 7, 8, 9],
    "Han Solo": [4, 5, 6, 7, 9],
    "R2-D2": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "BB-8": [7, 8, 9],
    "Obi-Wan Kenobi": [1, 2, 3, 4, 5, 6],
    "Palpatine": [1, 2, 3, 5, 6, 9],
    "Lando Calrissian": [5, 6, 9],
    "Padme Amidala": [1, 2, 3],
    "Finn": [7, 8, 9],
    "Poe Dameron": [7, 8, 9],
}


def cargar_grafo():
    grafo = Grafo(dirigido=False)
    personajes = list(APARICIONES)
    for personaje in personajes:
        insertar_vertice(grafo, personaje)
    for i in range(len(personajes)):
        for j in range(i + 1, len(personajes)):
            juntos = 0
            for episodio in APARICIONES[personajes[i]]:
                if episodio in APARICIONES[personajes[j]]:
                    juntos += 1
            if juntos > 0:
                insertar_arista(grafo, juntos, personajes[i], personajes[j])
    return grafo


def arbol_expansion_minimo(grafo, origen):
    bosque = prim(grafo, origen)
    total = 0
    print("Arbol de expansion minimo desde", origen)
    for vertice_origen, vertice_destino, peso in bosque:
        print("  ", vertice_origen, "-", vertice_destino, "(" + str(peso) + ")")
        total += peso
    print("   Peso total:", total)


def aristas_del_grafo(grafo):
    aristas = []
    vertice = grafo.inicio
    while vertice is not None:
        ady = vertice.adyacentes.inicio
        while ady is not None:
            if vertice.info < ady.destino:
                aristas.append([vertice.info, ady.destino, ady.info])
            ady = ady.sig
        vertice = vertice.sig
    return aristas


def maximo_episodios_compartidos(grafo):
    aristas = aristas_del_grafo(grafo)
    maximo = 0
    for arista in aristas:
        if arista[2] > maximo:
            maximo = arista[2]
    pares = [arista for arista in aristas if arista[2] == maximo]
    return maximo, pares


def camino_minimo(grafo, origen, destino):
    pila = dijkstra(grafo, origen, destino)
    camino = []
    peso = None
    buscado = destino
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato[1][0].info == buscado:
            if peso is None:
                peso = dato[0]
            camino.insert(0, buscado)
            buscado = dato[1][1]
    if camino and camino[0] == origen:
        return camino, peso
    return None, None


def mostrar_camino(grafo, origen, destino):
    camino, peso = camino_minimo(grafo, origen, destino)
    if camino is None:
        print("No existe camino de", origen, "a", destino)
    else:
        print("Camino mas corto de", origen, "a", destino + ":", " -> ".join(camino), "| peso total:", peso)


def personajes_en_todos_los_episodios(grafo):
    elegidos = []
    for origen, destino, peso in aristas_del_grafo(grafo):
        if peso == TOTAL_EPISODIOS:
            for personaje in (origen, destino):
                if personaje not in elegidos:
                    elegidos.append(personaje)
    return sorted(elegidos)


grafo = cargar_grafo()
print("Vertices:", grafo.tamanio)
print("Aristas:", len(aristas_del_grafo(grafo)))

print("\n--- Arbol de expansion minimo ---")
for personaje in ["C-3PO", "Yoda", "Leia"]:
    arbol_expansion_minimo(grafo, personaje)

print("\n--- Maximo de episodios compartidos ---")
maximo, pares = maximo_episodios_compartidos(grafo)
print("Maximo:", maximo)
for origen, destino, peso in pares:
    print("  ", origen, "-", destino)

print("\n--- Caminos mas cortos ---")
mostrar_camino(grafo, "C-3PO", "R2-D2")
mostrar_camino(grafo, "Yoda", "Darth Vader")

print("\n--- Personajes que aparecieron en los nueve episodios ---")
for personaje in personajes_en_todos_los_episodios(grafo):
    print("  ", personaje)
