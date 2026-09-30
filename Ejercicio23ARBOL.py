"""Ejercicio 23: Árbol Binario."""
import unicodedata
from collections import deque


class NodoArbol:
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None
        self.altura = 0


# ---------------------------------------------------------------- criterio
def criterio(dato, campo=None):
    """Devuelve el valor por el cual se compara: un atributo del registro
    (si `campo` es atributo de la clase) o el dato tal cual."""
    if campo is not None and hasattr(dato, '__dict__'):
        dic = dato.__dict__
        if campo in dic:
            return dic[campo]
    return dato


def normalizar(valor):
    """Para cadenas: minúsculas y sin tildes. Otros tipos quedan igual."""
    if isinstance(valor, str):
        texto = unicodedata.normalize('NFD', valor)
        texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
        return texto.lower()
    return valor


def _clave(dato, campo=None):
    return normalizar(criterio(dato, campo))


# ------------------------------------------------------------------ alturas
def altura(raiz):
    return -1 if raiz is None else raiz.altura


def actualizar_altura(raiz):
    if raiz is not None:
        raiz.altura = max(altura(raiz.izq), altura(raiz.der)) + 1


# --------------------------------------------------------------- rotaciones
def rotar_simple(raiz, control):
    """control True: rotación a la derecha; False: a la izquierda."""
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizar_altura(raiz)
    actualizar_altura(aux)
    return aux


def rotar_doble(raiz, control):
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz


def balancear(raiz):
    if raiz is not None:
        actualizar_altura(raiz)
        fe = altura(raiz.der) - altura(raiz.izq)
        if fe == -2:
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif fe == 2:
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz


# ---------------------------------------------------------------- operaciones
def arbol_vacio(raiz):
    return raiz is None


def insertar_nodo(raiz, dato, campo=None):
    if raiz is None:
        return NodoArbol(dato)
    if _clave(dato, campo) < _clave(raiz.info, campo):
        raiz.izq = insertar_nodo(raiz.izq, dato, campo)
    else:
        raiz.der = insertar_nodo(raiz.der, dato, campo)
    return balancear(raiz)


def reemplazar(raiz):
    """Busca el mayor nodo del subárbol (el que reemplaza al eliminado)
    y lo quita de su lugar. Devuelve (subárbol, nodo_reemplazo)."""
    if raiz.der is None:
        return raiz.izq, raiz
    raiz.der, aux = reemplazar(raiz.der)
    return balancear(raiz), aux


def eliminar_nodo(raiz, clave, campo=None):
    """Devuelve (raíz, valor_eliminado). valor_eliminado es None si no estaba."""
    valor = None
    if raiz is not None:
        k = normalizar(clave)
        if k < _clave(raiz.info, campo):
            raiz.izq, valor = eliminar_nodo(raiz.izq, clave, campo)
        elif k > _clave(raiz.info, campo):
            raiz.der, valor = eliminar_nodo(raiz.der, clave, campo)
        else:
            valor = raiz.info
            if raiz.der is None:
                return raiz.izq, valor
            if raiz.izq is None:
                return raiz.der, valor
            raiz.izq, aux = reemplazar(raiz.izq)
            raiz.info = aux.info
        raiz = balancear(raiz)
    return raiz, valor


def buscar(raiz, clave, campo=None):
    """Devuelve el nodo con esa clave exacta o None."""
    k = normalizar(clave)
    while raiz is not None:
        actual = _clave(raiz.info, campo)
        if k == actual:
            return raiz
        raiz = raiz.izq if k < actual else raiz.der
    return None


def buscar_por_proximidad(raiz, cadena, campo=None):
    """Devuelve la lista de datos cuya clave contiene `cadena`."""
    k = normalizar(cadena)
    return [d for d in iterar_inorden(raiz) if k in str(_clave(d, campo))]


# ---------------------------------------------------------------- recorridos
def iterar_inorden(raiz):
    if raiz is not None:
        yield from iterar_inorden(raiz.izq)
        yield raiz.info
        yield from iterar_inorden(raiz.der)


def iterar_inorden_desc(raiz):
    if raiz is not None:
        yield from iterar_inorden_desc(raiz.der)
        yield raiz.info
        yield from iterar_inorden_desc(raiz.izq)


def iterar_preorden(raiz):
    if raiz is not None:
        yield raiz.info
        yield from iterar_preorden(raiz.izq)
        yield from iterar_preorden(raiz.der)


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def preorden(raiz):
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izq)
        postorden(raiz.der)
        print(raiz.info)


def por_nivel(raiz):
    """Barrido por nivel usando una cola (arribo/atención)."""
    cola = deque()
    if raiz is not None:
        cola.append((raiz, 1))
    while cola:
        nodo, nivel = cola.popleft()
        print(f"[nivel {nivel}] {nodo.info}")
        if nodo.izq is not None:
            cola.append((nodo.izq, nivel + 1))
        if nodo.der is not None:
            cola.append((nodo.der, nivel + 1))


def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izq) + contar_nodos(raiz.der)


"""Capítulo X - Ejercicio 23: árbol de criaturas mitológicas (AVL)."""


class Criatura:
    def __init__(self, nombre, derrotado_por=None, descripcion='',
                 capturada=None):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = descripcion
        self.capturada = capturada  # héroe o dios que la capturó

    def __str__(self):
        return (f"{self.nombre} | derrotada por: {self.derrotado_por or '-'}"
                f" | capturada por: {self.capturada or '-'}"
                f" | {self.descripcion}")


# (nombre, derrotado por, descripción breve)
DATOS = [
    ('Ceto', None, 'Diosa marina, madre de monstruos marinos.'),
    ('Tifón', 'Zeus', 'Gigante monstruoso, padre de muchos monstruos.'),
    ('Equidna', 'Argos Panoptes', 'Mitad mujer, mitad serpiente; madre de monstruos.'),
    ('Dino', None, 'Una de las Grayas, hermana de Pefredo y Enio.'),
    ('Pefredo', None, 'Una de las Grayas; compartía un ojo y un diente.'),
    ('Enio', None, 'Una de las Grayas.'),
    ('Escila', None, 'Monstruo marino de seis cabezas.'),
    ('Caribdis', None, 'Remolino monstruoso que engullía barcos.'),
    ('Euríale', None, 'Una de las Gorgonas, hermana de Medusa.'),
    ('Esteno', None, 'Una de las Gorgonas.'),
    ('Medusa', 'Perseo', 'Gorgona cuya mirada convertía en piedra.'),
    ('Ladón', 'Heracles', 'Dragón guardián de las manzanas de oro de las Hespérides.'),
    ('Águila del Cáucaso', None, 'Águila que devoraba el hígado de Prometeo.'),
    ('Quimera', 'Belerofonte', 'León con cabeza de cabra y cola de serpiente.'),
    ('Hidra de Lerna', 'Heracles', 'Serpiente acuática de varias cabezas regenerables.'),
    ('León de Nemea', 'Heracles', 'León de piel invulnerable.'),
    ('Esfinge', 'Edipo', 'Criatura alada con cuerpo de león que planteaba enigmas.'),
    ('Dragón de la Cólquida', None, 'Dragón que guardaba el vellocino de oro.'),
    ('Cerbero', None, 'Perro de tres cabezas guardián del Hades.'),
    ('Cerda de Cromión', 'Teseo', 'Enorme cerda que asolaba la región de Cromión.'),
    ('Ortro', 'Heracles', 'Perro de dos cabezas, guardián del ganado de Gerión.'),
    ('Toro de Creta', 'Teseo', 'Toro salvaje que asolaba la isla de Creta.'),
    ('Jabalí de Calidón', 'Atalanta', 'Jabalí enviado por Artemisa a Calidón.'),
    ('Carcinos', None, 'Cangrejo gigante aliado de la Hidra.'),
    ('Gerión', 'Heracles', 'Gigante de tres cuerpos, dueño de un rebaño.'),
    ('Cloto', None, 'Moira que hilaba el hilo de la vida.'),
    ('Láquesis', None, 'Moira que medía el hilo de la vida.'),
    ('Átropos', None, 'Moira que cortaba el hilo de la vida.'),
    ('Minotauro de Creta', 'Teseo', 'Hombre con cabeza de toro, encerrado en el laberinto.'),
    ('Harpías', None, 'Mitad mujer, mitad ave; robaban la comida.'),
    ('Argos Panoptes', 'Hermes', 'Gigante de cien ojos.'),
    ('Aves del Estínfalo', None, 'Aves de plumas metálicas que asolaban un lago.'),
    ('Talos', 'Medea', 'Autómata de bronce guardián de Creta.'),
    ('Sirenas', None, 'Seres que atraían a los marineros con su canto.'),
    ('Pitón', 'Apolo', 'Serpiente gigante guardiana del oráculo de Delfos.'),
    ('Cierva de Cerinea', None, 'Cierva de cuernos de oro consagrada a Artemisa.'),
    ('Basilisco', None, 'Serpiente cuya mirada y aliento eran mortales.'),
    ('Jabalí de Erimanto', None, 'Jabalí gigante del monte Erimanto.'),
]


def titulo(texto):
    print(f"\n=== {texto} ===")


def main():
    raiz = None
    for nombre, heroe, desc in DATOS:
        raiz = insertar_nodo(raiz, Criatura(nombre, heroe, desc), 'nombre')

    titulo("a) Listado inorden de criaturas y quién las derrotó")
    for c in iterar_inorden(raiz):
        print(f"{c.nombre:<24} -> {c.derrotado_por or '-'}")

    titulo("b) Cada criatura tiene su descripción (campo 'descripcion')")
    print("Cargada en la creación; ejemplo:", buscar(raiz, 'Hidra de Lerna', 'nombre').info.descripcion)

    titulo("c) Información de Talos")
    print(buscar(raiz, 'Talos', 'nombre').info)

    titulo("d) Los 3 héroes/dioses que derrotaron más criaturas")
    cuenta = {}
    for c in iterar_inorden(raiz):
        if c.derrotado_por:
            cuenta[c.derrotado_por] = cuenta.get(c.derrotado_por, 0) + 1
    ranking = sorted(cuenta.items(), key=lambda x: (-x[1], x[0]))
    for heroe, n in ranking[:3]:
        print(f"{heroe}: {n}")
    umbral = ranking[2][1]
    empatados = [h for h, n in ranking[3:] if n == umbral]
    if empatados:
        print(f"(Nota: el tercer puesto está empatado con {umbral} criatura; "
              f"también: {', '.join(empatados)})")

    titulo("e) Criaturas derrotadas por Heracles")
    for c in iterar_inorden(raiz):
        if c.derrotado_por == 'Heracles':
            print(c.nombre)

    titulo("f) Criaturas que no han sido derrotadas")
    for c in iterar_inorden(raiz):
        if c.derrotado_por is None:
            print(c.nombre)

    titulo("g) Campo 'capturada' agregado a cada nodo (inicia en None)")
    print("Ejemplo:", buscar(raiz, 'Cerbero', 'nombre').info.capturada)

    titulo("h) Heracles atrapó a Cerbero, Toro de Creta, Cierva de Cerinea y Jabalí de Erimanto")
    for nombre in ('Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto'):
        buscar(raiz, nombre, 'nombre').info.capturada = 'Heracles'
        print(f"{nombre}: capturada por Heracles")

    titulo("i) Búsqueda por coincidencia (ejemplo: 'cer')")
    for c in buscar_por_proximidad(raiz, 'cer', 'nombre'):
        print(c.nombre)

    titulo("j) Eliminar al Basilisco y a las Sirenas")
    for nombre in ('Basilisco', 'Sirenas'):
        raiz, quitado = eliminar_nodo(raiz, nombre, 'nombre')
        print("Eliminada:" if quitado else "No estaba:", nombre)

    titulo("k) Aves del Estínfalo: Heracles derrotó a varias")
    aves = buscar(raiz, 'Aves del Estínfalo', 'nombre').info
    aves.derrotado_por = 'Heracles'
    aves.descripcion += ' Heracles derrotó a varias.'
    print(aves)

    titulo("l) Renombrar Ladón por Dragón Ladón")
    # cambia el campo clave: se quita, se modifica y se vuelve a insertar
    raiz, ladon = eliminar_nodo(raiz, 'Ladón', 'nombre')
    ladon.nombre = 'Dragón Ladón'
    raiz = insertar_nodo(raiz, ladon, 'nombre')
    print(buscar(raiz, 'Dragón Ladón', 'nombre').info)

    titulo("m) Listado por nivel")
    por_nivel(raiz)

    titulo("n) Criaturas capturadas por Heracles")
    for c in iterar_inorden(raiz):
        if c.capturada == 'Heracles':
            print(c.nombre)


if __name__ == '__main__':
    main()
