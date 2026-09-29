"""Ejercicio 5: árbol de superhéroes y villanos del MCU (AVL)."""
class _NodoAVL:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None
        self.altura = 1


def _altura(nodo):
    return nodo.altura if nodo else 0


def _actualizar(nodo):
    nodo.altura = 1 + max(_altura(nodo.izq), _altura(nodo.der))


def _rotar_derecha(y):
    x, temporal = y.izq, y.izq.der
    x.der, y.izq = y, temporal
    _actualizar(y)
    _actualizar(x)
    return x


def _rotar_izquierda(x):
    y, temporal = x.der, x.der.izq
    y.izq, x.der = x, temporal
    _actualizar(x)
    _actualizar(y)
    return y


def insertar_nodo(raiz, dato, clave):
    if raiz is None:
        return _NodoAVL(dato)
    valor, actual = getattr(dato, clave), getattr(raiz.dato, clave)
    if valor < actual:
        raiz.izq = insertar_nodo(raiz.izq, dato, clave)
    elif valor > actual:
        raiz.der = insertar_nodo(raiz.der, dato, clave)
    else:
        return raiz
    _actualizar(raiz)
    balance = _altura(raiz.izq) - _altura(raiz.der)
    if balance > 1:
        if valor > getattr(raiz.izq.dato, clave):
            raiz.izq = _rotar_izquierda(raiz.izq)
        return _rotar_derecha(raiz)
    if balance < -1:
        if valor < getattr(raiz.der.dato, clave):
            raiz.der = _rotar_derecha(raiz.der)
        return _rotar_izquierda(raiz)
    return raiz


def _minimo(raiz):
    while raiz.izq:
        raiz = raiz.izq
    return raiz


def eliminar_nodo(raiz, valor, clave):
    if raiz is None:
        return None, None
    actual = getattr(raiz.dato, clave)
    if valor < actual:
        raiz.izq, eliminado = eliminar_nodo(raiz.izq, valor, clave)
    elif valor > actual:
        raiz.der, eliminado = eliminar_nodo(raiz.der, valor, clave)
    else:
        eliminado = raiz.dato
        if not raiz.izq or not raiz.der:
            return (raiz.izq or raiz.der), eliminado
        sucesor = _minimo(raiz.der)
        raiz.dato = sucesor.dato
        raiz.der, _ = eliminar_nodo(raiz.der, getattr(sucesor.dato, clave), clave)
    _actualizar(raiz)
    balance = _altura(raiz.izq) - _altura(raiz.der)
    if balance > 1:
        if _altura(raiz.izq.izq) < _altura(raiz.izq.der):
            raiz.izq = _rotar_izquierda(raiz.izq)
        return _rotar_derecha(raiz), eliminado
    if balance < -1:
        if _altura(raiz.der.der) < _altura(raiz.der.izq):
            raiz.der = _rotar_derecha(raiz.der)
        return _rotar_izquierda(raiz), eliminado
    return raiz, eliminado


def iterar_inorden(raiz):
    if raiz:
        yield from iterar_inorden(raiz.izq)
        yield raiz.dato
        yield from iterar_inorden(raiz.der)


def iterar_inorden_desc(raiz):
    if raiz:
        yield from iterar_inorden_desc(raiz.der)
        yield raiz.dato
        yield from iterar_inorden_desc(raiz.izq)


def buscar_por_proximidad(raiz, texto, clave):
    texto = texto.casefold()
    return [dato for dato in iterar_inorden(raiz)
            if texto in str(getattr(dato, clave)).casefold()]


def contar_nodos(raiz):
    return sum(1 for _ in iterar_inorden(raiz))


class Personaje:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe 

    def __str__(self):
        return f"{self.nombre} ({'héroe' if self.es_heroe else 'villano'})"


HEROES = ['Iron Man', 'Capitan America', 'Thor', 'Hulk', 'Black Widow',
          'Hawkeye', 'Spider-Man', 'Black Panther', 'Capitana Marvel',
          'Ant-Man', 'Star-Lord', 'Falcon', 'Scarlet Witch', 'Vision',
          'Dr Strange']
VILLANOS = ['Thanos', 'Loki', 'Ultron', 'Red Skull', 'Hela', 'Killmonger',
            'Vulture', 'Mysterio', 'Ronan', 'Yellowjacket', 'Ego', 'Zemo',
            'Whiplash', 'Abomination', 'Dormammu', 'Kaecilius',
            'Crossbones', 'Ebony Maw']


def titulo(texto):
    print(f"\n=== {texto} ===")


def main():
    raiz = None
    for n in HEROES:
        raiz = insertar_nodo(raiz, Personaje(n, True), 'nombre')
    for n in VILLANOS:
        raiz = insertar_nodo(raiz, Personaje(n, False), 'nombre')

    titulo("b) Villanos ordenados alfabéticamente")
    for p in iterar_inorden(raiz):
        if not p.es_heroe:
            print(p.nombre)

    titulo("c) Superhéroes que empiezan con C")
    for p in iterar_inorden(raiz):
        if p.es_heroe and p.nombre.upper().startswith('C'):
            print(p.nombre)

    titulo("d) Cantidad de superhéroes en el árbol")
    print(sum(1 for p in iterar_inorden(raiz) if p.es_heroe))

    titulo("e) Corregir Doctor Strange (búsqueda por proximidad)")
    encontrados = buscar_por_proximidad(raiz, 'strange', 'nombre')
    print("Coincidencias:", [p.nombre for p in encontrados])
    for p in encontrados:
        
        raiz, mal = eliminar_nodo(raiz, p.nombre, 'nombre')
        mal.nombre = 'Doctor Strange'
        raiz = insertar_nodo(raiz, mal, 'nombre')
        print("Corregido:", mal)

    titulo("f) Superhéroes ordenados de manera descendente")
    for p in iterar_inorden_desc(raiz):
        if p.es_heroe:
            print(p.nombre)

    titulo("g) Bosque: un árbol de superhéroes y otro de villanos")
    arbol_heroes = None
    arbol_villanos = None
    for p in iterar_inorden(raiz):
        if p.es_heroe:
            arbol_heroes = insertar_nodo(arbol_heroes, p, 'nombre')
        else:
            arbol_villanos = insertar_nodo(arbol_villanos, p, 'nombre')

    print("\nI) Cantidad de nodos por árbol")
    print("Superhéroes:", contar_nodos(arbol_heroes))
    print("Villanos:   ", contar_nodos(arbol_villanos))

    print("\nII) Barrido ordenado alfabéticamente")
    print("Superhéroes:", ', '.join(p.nombre for p in iterar_inorden(arbol_heroes)))
    print("Villanos:   ", ', '.join(p.nombre for p in iterar_inorden(arbol_villanos)))


if __name__ == '__main__':
    main()