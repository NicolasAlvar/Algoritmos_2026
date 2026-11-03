import json
import os
import textwrap


class NodoCola:
    def __init__(self, info=None, sig=None):
        self.info = info
        self.sig = sig


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def arribo(cola, elemento):
    nodo = NodoCola(elemento)
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1


def atencion(cola):
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


class NodoArbol:
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None
        self.altura = 0


def criterio(dato, campo=None):
    if hasattr(dato, '__dict__'):
        dic = dato.__dict__
        if campo is not None and campo in dic:
            return dic[campo]
    return dato


def arbol_vacio(raiz):
    return raiz is None


def altura(raiz):
    if raiz is None:
        return -1
    return raiz.altura


def actualizar_altura(raiz):
    if raiz is not None:
        raiz.altura = max(altura(raiz.izq), altura(raiz.der)) + 1


def rotacion_simple(raiz, control):
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


def rotacion_doble(raiz, control):
    if control:
        raiz.izq = rotacion_simple(raiz.izq, False)
        raiz = rotacion_simple(raiz, True)
    else:
        raiz.der = rotacion_simple(raiz.der, True)
        raiz = rotacion_simple(raiz, False)
    return raiz


def balancear(raiz):
    if raiz is not None:
        actualizar_altura(raiz)
        if altura(raiz.der) - altura(raiz.izq) == 2:
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rotacion_simple(raiz, False)
            else:
                raiz = rotacion_doble(raiz, False)
        elif altura(raiz.izq) - altura(raiz.der) == 2:
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rotacion_simple(raiz, True)
            else:
                raiz = rotacion_doble(raiz, True)
    return raiz


def insertar_nodo(raiz, dato, campo=None):
    if raiz is None:
        raiz = NodoArbol(dato)
    elif criterio(dato, campo) < criterio(raiz.info, campo):
        raiz.izq = insertar_nodo(raiz.izq, dato, campo)
    else:
        raiz.der = insertar_nodo(raiz.der, dato, campo)
    raiz = balancear(raiz)
    return raiz


def reemplazar(raiz):
    if raiz.der is None:
        return raiz.izq, raiz
    raiz.der, aux = reemplazar(raiz.der)
    raiz = balancear(raiz)
    return raiz, aux


def eliminar_nodo(raiz, clave, campo=None):
    x = None
    if raiz is not None:
        if clave < criterio(raiz.info, campo):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave, campo)
        elif clave > criterio(raiz.info, campo):
            raiz.der, x = eliminar_nodo(raiz.der, clave, campo)
        else:
            x = raiz.info
            if raiz.izq is None:
                raiz = raiz.der
            elif raiz.der is None:
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info
        raiz = balancear(raiz)
    return raiz, x


def buscar(raiz, clave, campo=None):
    pos = None
    if raiz is not None:
        valor = criterio(raiz.info, campo)
        if valor == clave:
            pos = raiz
        elif clave < valor:
            pos = buscar(raiz.izq, clave, campo)
        else:
            pos = buscar(raiz.der, clave, campo)
    return pos


def buscar_todos(raiz, clave, campo=None, resultado=None):
    if resultado is None:
        resultado = []
    if raiz is not None:
        valor = criterio(raiz.info, campo)
        if clave <= valor:
            buscar_todos(raiz.izq, clave, campo, resultado)
        if clave == valor:
            resultado.append(raiz.info)
        if clave >= valor:
            buscar_todos(raiz.der, clave, campo, resultado)
    return resultado


def preorden(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz is not None:
        resultado.append(raiz.info)
        preorden(raiz.izq, resultado)
        preorden(raiz.der, resultado)
    return resultado


def inorden(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz is not None:
        inorden(raiz.izq, resultado)
        resultado.append(raiz.info)
        inorden(raiz.der, resultado)
    return resultado


def postorden(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz is not None:
        postorden(raiz.izq, resultado)
        postorden(raiz.der, resultado)
        resultado.append(raiz.info)
    return resultado


def por_nivel(raiz):
    resultado = []
    pendientes = Cola()
    if raiz is not None:
        arribo(pendientes, raiz)
        while not cola_vacia(pendientes):
            nodo = atencion(pendientes)
            resultado.append(nodo.info)
            if nodo.izq is not None:
                arribo(pendientes, nodo.izq)
            if nodo.der is not None:
                arribo(pendientes, nodo.der)
    return resultado


class Pokemon:
    def __init__(self, nombre, numero, tipos, debilidades, megaevolucion, gigamax):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos
        self.debilidades = debilidades
        self.megaevolucion = megaevolucion
        self.gigamax = gigamax


class Indice:
    def __init__(self, clave, nrr):
        self.clave = clave
        self.nrr = nrr


def cargar_pokemons():
    archivo = []
    raiz_nombre = None
    raiz_numero = None
    raiz_tipo = None
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pokemons.json")
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    for nrr, dato in enumerate(datos):
        pokemon = Pokemon(dato["nombre"], dato["numero"], dato["tipos"], dato["debilidades"],
                          dato["megaevolucion"], dato["gigamax"])
        archivo.append(pokemon)
        raiz_nombre = insertar_nodo(raiz_nombre, Indice(pokemon.nombre, nrr), "clave")
        raiz_numero = insertar_nodo(raiz_numero, Indice(pokemon.numero, nrr), "clave")
        for tipo in pokemon.tipos:
            raiz_tipo = insertar_nodo(raiz_tipo, Indice(tipo, nrr), "clave")
    return archivo, raiz_nombre, raiz_numero, raiz_tipo


def mostrar_pokemon(pokemon):
    print("No.", pokemon.numero, "-", pokemon.nombre)
    print("   Tipos:", ", ".join(pokemon.tipos))
    print("   Debil frente a:", ", ".join(pokemon.debilidades))
    print("   Megaevolucion:", "Si" if pokemon.megaevolucion else "No")
    print("   Gigamax:", "Si" if pokemon.gigamax else "No")


def mostrar_nombres(titulo, nombres):
    print(titulo, "(" + str(len(nombres)) + ")")
    print(textwrap.fill(", ".join(nombres), width=100, initial_indent="   ", subsequent_indent="   "))


def buscar_por_numero(raiz_numero, archivo, numero):
    nodo = buscar(raiz_numero, numero, "clave")
    if nodo is None:
        print("No existe el Pokemon numero", numero)
    else:
        mostrar_pokemon(archivo[nodo.info.nrr])


def proximidad(raiz, archivo, texto, resultado):
    if raiz is not None:
        proximidad(raiz.izq, archivo, texto, resultado)
        if texto.lower() in raiz.info.clave.lower():
            resultado.append(archivo[raiz.info.nrr])
        proximidad(raiz.der, archivo, texto, resultado)


def buscar_por_nombre(raiz_nombre, archivo, texto):
    resultado = []
    proximidad(raiz_nombre, archivo, texto, resultado)
    if not resultado:
        print("Ningun Pokemon coincide con", texto)
    for pokemon in resultado:
        mostrar_pokemon(pokemon)


def nombres_por_tipo(raiz_tipo, archivo, tipo):
    indices = buscar_todos(raiz_tipo, tipo, "clave")
    nombres = [archivo[indice.nrr].nombre for indice in indices]
    mostrar_nombres("Pokemons de tipo " + tipo, sorted(nombres))


def debiles_frente_a(raiz_nombre, archivo, nombre):
    nodo = buscar(raiz_nombre, nombre, "clave")
    if nodo is None:
        print(nombre, "no esta cargado")
    else:
        tipos = archivo[nodo.info.nrr].tipos
        nombres = []
        for indice in inorden(raiz_nombre):
            pokemon = archivo[indice.nrr]
            debil = False
            for tipo in tipos:
                if tipo in pokemon.debilidades:
                    debil = True
            if debil:
                nombres.append(pokemon.nombre)
        mostrar_nombres("Debiles frente a " + nombre + " (tipos: " + ", ".join(tipos) + ")", nombres)


def contar_por_tipo(raiz_tipo):
    conteo = []
    for indice in inorden(raiz_tipo):
        if conteo and conteo[-1][0] == indice.clave:
            conteo[-1][1] += 1
        else:
            conteo.append([indice.clave, 1])
    return conteo


def contar_megaevolucion(raiz_nombre, archivo):
    cantidad = 0
    for indice in inorden(raiz_nombre):
        if archivo[indice.nrr].megaevolucion:
            cantidad += 1
    return cantidad


def contar_gigamax(raiz_nombre, archivo):
    cantidad = 0
    for indice in inorden(raiz_nombre):
        if archivo[indice.nrr].gigamax:
            cantidad += 1
    return cantidad


archivo, raiz_nombre, raiz_numero, raiz_tipo = cargar_pokemons()
print("Pokemons cargados:", len(archivo))

print("\n--- Busqueda por numero (25) ---")
buscar_por_numero(raiz_numero, archivo, 25)

print("\n--- Busqueda por proximidad de nombre ('bul') ---")
buscar_por_nombre(raiz_nombre, archivo, "bul")

print("\n--- Busqueda por proximidad de nombre ('char') ---")
buscar_por_nombre(raiz_nombre, archivo, "char")

print("\n--- Nombres por tipo ---")
for tipo in ["fantasma", "fuego", "acero", "electrico"]:
    nombres_por_tipo(raiz_tipo, archivo, tipo)

print("\n--- Listado ascendente por numero ---")
mostrar_nombres("Por numero", [str(archivo[i.nrr].numero) + " " + archivo[i.nrr].nombre for i in inorden(raiz_numero)])

print("\n--- Listado ascendente por nombre ---")
mostrar_nombres("Por nombre", [archivo[i.nrr].nombre for i in inorden(raiz_nombre)])

print("\n--- Listado por nivel (arbol de nombres) ---")
mostrar_nombres("Por nivel", [archivo[i.nrr].nombre for i in por_nivel(raiz_nombre)])

print("\n--- Debiles frente a ---")
for nombre in ["Jolteon", "Lycanroc", "Tyrantrum"]:
    debiles_frente_a(raiz_nombre, archivo, nombre)

print("\n--- Cantidad de Pokemons por tipo ---")
for tipo, cantidad in contar_por_tipo(raiz_tipo):
    print("  ", tipo + ":", cantidad)

print("\nPokemons con megaevolucion:", contar_megaevolucion(raiz_nombre, archivo))
print("Pokemons con forma gigamax:", contar_gigamax(raiz_nombre, archivo))
