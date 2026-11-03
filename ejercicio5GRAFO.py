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


class Equipo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __eq__(self, otro):
        if isinstance(otro, Equipo):
            return self.nombre == otro.nombre
        return self.nombre == otro

    def __lt__(self, otro):
        if isinstance(otro, Equipo):
            return self.nombre < otro.nombre
        return self.nombre < otro

    def __gt__(self, otro):
        if isinstance(otro, Equipo):
            return self.nombre > otro.nombre
        return self.nombre > otro

    def __str__(self):
        return self.nombre + " [" + self.tipo + "]"


EQUIPOS = [
    ("Manjaro", "pc"),
    ("Fedora", "pc"),
    ("Ubuntu", "pc"),
    ("Red Hat", "notebook"),
    ("Debian", "notebook"),
    ("Arch", "notebook"),
    ("Guarani", "servidor"),
    ("MongoDB", "servidor"),
    ("Router 01", "router"),
    ("Router 02", "router"),
    ("Switch 01", "switch"),
    ("Switch 02", "switch"),
    ("Impresora", "impresora"),
]

CONEXIONES = [
    ("Switch 01", "Manjaro", 1),
    ("Switch 01", "Red Hat", 2),
    ("Switch 01", "Debian", 3),
    ("Switch 01", "Router 01", 2),
    ("Switch 01", "Switch 02", 6),
    ("Router 01", "Impresora", 3),
    ("Router 01", "Router 02", 4),
    ("Router 02", "Switch 02", 2),
    ("Router 02", "MongoDB", 3),
    ("Switch 02", "Fedora", 1),
    ("Switch 02", "Ubuntu", 2),
    ("Switch 02", "Arch", 2),
    ("Switch 02", "Guarani", 2),
]


def eliminar_arista(vertice, destino):
    lista = vertice.adyacentes
    x = None
    if lista.inicio is not None:
        if lista.inicio.destino == destino:
            x = lista.inicio
            lista.inicio = lista.inicio.sig
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while act is not None and act.destino != destino:
                ant = act
                act = act.sig
            if act is not None:
                x = act
                ant.sig = act.sig
        if x is not None:
            lista.tamanio -= 1
    return x


def cargar_red():
    grafo = Grafo(dirigido=False)
    for nombre, tipo in EQUIPOS:
        insertar_vertice(grafo, Equipo(nombre, tipo))
    for origen, destino, peso in CONEXIONES:
        insertar_arista(grafo, peso, origen, destino)
    return grafo


def nombres(lista):
    return " -> ".join(str(elemento) for elemento in lista)


def barridos(grafo, inicio):
    marcar_no_visitado(grafo)
    profundidad_res = barrido_profundidad(grafo, inicio)
    marcar_no_visitado(grafo)
    amplitud_res = barrido_amplitud(grafo, inicio)
    marcar_no_visitado(grafo)
    print("Desde", inicio)
    print("   Profundidad:", nombres(profundidad_res))
    print("   Amplitud:   ", nombres(amplitud_res))


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
            camino.insert(0, dato[1][0].info)
            buscado = dato[1][1]
    if camino and camino[0] == origen:
        return camino, peso
    return None, None


def mostrar_camino(grafo, origen, destino):
    camino, peso = camino_minimo(grafo, origen, destino)
    if camino is None:
        print("No hay camino de", origen, "a", destino)
    else:
        print("Camino de", origen, "a", destino + ":", nombres(camino), "| peso total:", peso)


def vertices_de_tipo(grafo, tipos):
    resultado = []
    vertice = grafo.inicio
    while vertice is not None:
        if vertice.info.tipo in tipos:
            resultado.append(vertice.info.nombre)
        vertice = vertice.sig
    return resultado


def mas_cercano(grafo, candidatos, destino):
    mejor = None
    elegidos = []
    for candidato in candidatos:
        camino, peso = camino_minimo(grafo, candidato, destino)
        if camino is not None:
            if mejor is None or peso < mejor:
                mejor = peso
                elegidos = [[candidato, camino]]
            elif peso == mejor:
                elegidos.append([candidato, camino])
    return mejor, elegidos


def arbol_expansion_minima(grafo, origen):
    bosque = prim(grafo, origen)
    total = 0
    for vertice_origen, vertice_destino, peso in bosque:
        print("  ", vertice_origen, "-", vertice_destino, "(" + str(peso) + ")")
        total += peso
    print("   Peso total:", total)


def equipos_del_switch(grafo, nombre_switch):
    switch = buscar_vertice(grafo, nombre_switch)
    resultado = []
    ady = switch.adyacentes.inicio
    while ady is not None:
        vecino = buscar_vertice(grafo, ady.destino)
        if vecino.info.tipo in ("pc", "notebook"):
            resultado.append(vecino.info.nombre)
        ady = ady.sig
    return resultado


def mover_impresora(grafo, router_nuevo):
    vertice = buscar_vertice(grafo, "Impresora")
    ady = vertice.adyacentes.inicio
    while ady is not None:
        viejo = ady.destino
        ady = ady.sig
        eliminar_arista(vertice, viejo)
        eliminar_arista(buscar_vertice(grafo, viejo), "Impresora")
    insertar_arista(grafo, 3, router_nuevo, "Impresora")


grafo = cargar_red()
print("Equipos cargados:", grafo.tamanio)

print("\n--- b) Barridos desde las tres notebooks ---")
for notebook in ["Red Hat", "Debian", "Arch"]:
    barridos(grafo, notebook)

print("\n--- c) Camino mas corto hasta la impresora ---")
for pc in ["Manjaro", "Red Hat", "Fedora"]:
    mostrar_camino(grafo, pc, "Impresora")

print("\n--- d) Arbol de expansion minima ---")
arbol_expansion_minima(grafo, "Router 01")

print("\n--- e) PC (no notebook) con el camino mas corto al servidor Guarani ---")
peso, elegidos = mas_cercano(grafo, vertices_de_tipo(grafo, ["pc"]), "Guarani")
for nombre, camino in elegidos:
    print("  ", nombre, "| peso:", peso, "|", nombres(camino))

print("\n--- f) Computadora del Switch 01 con el camino mas corto al servidor MongoDB ---")
peso, elegidos = mas_cercano(grafo, equipos_del_switch(grafo, "Switch 01"), "MongoDB")
for nombre, camino in elegidos:
    print("  ", nombre, "| peso:", peso, "|", nombres(camino))

print("\n--- g) Impresora conectada al Router 02: se repite el punto b ---")
mover_impresora(grafo, "Router 02")
for notebook in ["Red Hat", "Debian", "Arch"]:
    barridos(grafo, notebook)
