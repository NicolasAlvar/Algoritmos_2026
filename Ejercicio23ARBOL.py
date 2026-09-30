"""Ejercicio 23: Árbol Binario."""
import unicodedata
from collections import deque


class NodoArbol:
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None
        self.altura = 0



def criterio(dato, campo=None):
    """Devuelve el valor por el cual se compara: un atributo del registro
    (si `campo` es atributo de la clase) o el dato tal cual."""
    if campo is not None and hasattr(dato, '__dict__'):
        dic = dato.__dict__
        if campo in dic:
            return dic[campo]
    return dato


def normalizar(valor):
    """Para cadenas: minusculas y sin tildes. Otros tipos quedan igual."""
    if isinstance(valor, str):
        texto = unicodedata.normalize('NFD', valor)
        texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
        return texto.lower()
    return valor


def _clave(dato, campo=None):
    return normalizar(criterio(dato, campo))



def altura(raiz):
    return -1 if raiz is None else raiz.altura


def actualizar_altura(raiz):
    if raiz is not None:
        raiz.altura = max(altura(raiz.izq), altura(raiz.der)) + 1



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
    """Busca el mayor nodo del subarbol (el que reemplaza al eliminado)
    y lo quita de su lugar. Devuelve (subarbol, nodo_reemplazo)."""
    if raiz.der is None:
        return raiz.izq, raiz
    raiz.der, aux = reemplazar(raiz.der)
    return balancear(raiz), aux


def eliminar_nodo(raiz, clave, campo=None):
    """Devuelve (raiz, valor_eliminado). valor_eliminado es None si no estaba."""
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
    """Barrido por nivel usando una cola (arribo/atencion)."""
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



DATOS = [
    ('Ceto', None, 'Diosa marina, madre de monstruos marinos.'),
    ('Tifon', 'Zeus', 'Gigante monstruoso, padre de muchos monstruos.'),
    ('Equidna', 'Argos Panoptes', 'Mitad mujer, mitad serpiente; madre de monstruos.'),
    ('Dino', None, 'Una de las Grayas, hermana de Pefredo y Enio.'),
    ('Pefredo', None, 'Una de las Grayas; compartia un ojo y un diente.'),
    ('Enio', None, 'Una de las Grayas.'),
    ('Escila', None, 'Monstruo marino de seis cabezas.'),
    ('Caribdis', None, 'Remolino monstruoso que engullia barcos.'),
    ('Euriale', None, 'Una de las Gorgonas, hermana de Medusa.'),
    ('Esteno', None, 'Una de las Gorgonas.'),
    ('Medusa', 'Perseo', 'Gorgona cuya mirada convertia en piedra.'),
    ('Ladon', 'Heracles', 'Dragon guardian de las manzanas de oro de las Hesperides.'),
    ('Aguila del Caucaso', None, 'Aguila que devoraba el higado de Prometeo.'),
    ('Quimera', 'Belerofonte', 'Leon con cabeza de cabra y cola de serpiente.'),
    ('Hidra de Lerna', 'Heracles', 'Serpiente acuatica de varias cabezas regenerables.'),
    ('Leon de Nemea', 'Heracles', 'Leon de piel invulnerable.'),
    ('Esfinge', 'Edipo', 'Criatura alada con cuerpo de leon que planteaba enigmas.'),
    ('Dragon de la Colquida', None, 'Dragon que guardaba el vellocino de oro.'),
    ('Cerbero', None, 'Perro de tres cabezas guardian del Hades.'),
    ('Cerda de Cromion', 'Teseo', 'Enorme cerda que asolaba la region de Cromion.'),
    ('Ortro', 'Heracles', 'Perro de dos cabezas, guardian del ganado de Gerion.'),
    ('Toro de Creta', 'Teseo', 'Toro salvaje que asolaba la isla de Creta.'),
    ('Jabali de Calidon', 'Atalanta', 'Jabali enviado por Artemisa a Calidon.'),
    ('Carcinos', None, 'Cangrejo gigante aliado de la Hidra.'),
    ('Gerion', 'Heracles', 'Gigante de tres cuerpos, dueño de un rebaño.'),
    ('Cloto', None, 'Moira que hilaba el hilo de la vida.'),
    ('Laquesis', None, 'Moira que media el hilo de la vida.'),
    ('Atropos', None, 'Moira que cortaba el hilo de la vida.'),
    ('Minotauro de Creta', 'Teseo', 'Hombre con cabeza de toro, encerrado en el laberinto.'),
    ('Harpias', None, 'Mitad mujer, mitad ave; robaban la comida.'),
    ('Argos Panoptes', 'Hermes', 'Gigante de cien ojos.'),
    ('Aves del Estinfalo', None, 'Aves de plumas metalicas que asolaban un lago.'),
    ('Talos', 'Medea', 'Automata de bronce guardian de Creta.'),
    ('Sirenas', None, 'Seres que atraian a los marineros con su canto.'),
    ('Piton', 'Apolo', 'Serpiente gigante guardiana del oraculo de Delfos.'),
    ('Cierva de Cerinea', None, 'Cierva de cuernos de oro consagrada a Artemisa.'),
    ('Basilisco', None, 'Serpiente cuya mirada y aliento eran mortales.'),
    ('Jabali de Erimanto', None, 'Jabali gigante del monte Erimanto.'),
]


def titulo(texto):
    print(f"\n=== {texto} ===")


def main():
    raiz = None
    for nombre, heroe, desc in DATOS:
        raiz = insertar_nodo(raiz, Criatura(nombre, heroe, desc), 'nombre')

    titulo("a) Listado inorden de criaturas y quien las derroto")
    for c in iterar_inorden(raiz):
        print(f"{c.nombre:<24} -> {c.derrotado_por or '-'}")

    titulo("b) Cada criatura tiene su descripcion (campo 'descripcion')")
    print("Cargada en la creacion; ejemplo:", buscar(raiz, 'Hidra de Lerna', 'nombre').info.descripcion)

    titulo("c) Informacion de Talos")
    print(buscar(raiz, 'Talos', 'nombre').info)

    titulo("d) Los 3 heroes/dioses que derrotaron mas criaturas")
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
        print(f"(Nota: el tercer puesto esta empatado con {umbral} criatura; "
              f"tambien: {', '.join(empatados)})")

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

    titulo("h) Heracles atrapo a Cerbero, Toro de Creta, Cierva de Cerinea y Jabali de Erimanto")
    for nombre in ('Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabali de Erimanto'):
        buscar(raiz, nombre, 'nombre').info.capturada = 'Heracles'
        print(f"{nombre}: capturada por Heracles")

    titulo("i) Busqueda por coincidencia (ejemplo: 'cer')")
    for c in buscar_por_proximidad(raiz, 'cer', 'nombre'):
        print(c.nombre)

    titulo("j) Eliminar al Basilisco y a las Sirenas")
    for nombre in ('Basilisco', 'Sirenas'):
        raiz, quitado = eliminar_nodo(raiz, nombre, 'nombre')
        print("Eliminada:" if quitado else "No estaba:", nombre)

    titulo("k) Aves del Estinfalo: Heracles derroto a varias")
    aves = buscar(raiz, 'Aves del Estinfalo', 'nombre').info
    aves.derrotado_por = 'Heracles'
    aves.descripcion += ' Heracles derroto a varias.'
    print(aves)

    titulo("l) Renombrar Ladon por Dragon Ladon")
    # cambia el campo clave: se quita, se modifica y se vuelve a insertar
    raiz, ladon = eliminar_nodo(raiz, 'Ladon', 'nombre')
    ladon.nombre = 'Dragon Ladon'
    raiz = insertar_nodo(raiz, ladon, 'nombre')
    print(buscar(raiz, 'Dragon Ladon', 'nombre').info)

    titulo("m) Listado por nivel")
    por_nivel(raiz)

    titulo("n) Criaturas capturadas por Heracles")
    for c in iterar_inorden(raiz):
        if c.capturada == 'Heracles':
            print(c.nombre)


if __name__ == '__main__':
    main()
