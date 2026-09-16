"""
Ejercicio 15 - Tema Lista (Capítulo VIII)
------------------------------------------
Se cuenta con una lista de entrenadores Pokémon. De cada uno se conoce:
nombre, cantidad de torneos ganados, cantidad de batallas perdidas y
cantidad de batallas ganadas; además la lista de sus Pokémon, de los
cuales se sabe: nombre, nivel, tipo y subtipo.

Se resuelve utilizando LISTA DE LISTA: una lista de entrenadores, donde
cada entrenador contiene, entre sus datos, otra lista con sus Pokémon.

Cada entrenador se representa como un diccionario:
{
    "nombre": str,
    "torneos_ganados": int,
    "batallas_perdidas": int,
    "batallas_ganadas": int,
    "pokemons": [ {"nombre":.., "nivel":.., "tipo":.., "subtipo":..}, ... ]
}
"""


def crear_entrenador(nombre, torneos, perdidas, ganadas, pokemons):
    return {
        "nombre": nombre,
        "torneos_ganados": torneos,
        "batallas_perdidas": perdidas,
        "batallas_ganadas": ganadas,
        "pokemons": pokemons,
    }


def buscar_entrenador(entrenadores, nombre):
    for e in entrenadores:
        if e["nombre"].lower() == nombre.lower():
            return e
    return None


# a) cantidad de Pokémon de un determinado entrenador
def cantidad_pokemons(entrenadores, nombre_entrenador):
    e = buscar_entrenador(entrenadores, nombre_entrenador)
    if e is None:
        print(f"-> No se encontró al entrenador '{nombre_entrenador}'.")
        return None
    cantidad = len(e["pokemons"])
    print(f"-> {e['nombre']} tiene {cantidad} Pokémon(s).")
    return cantidad


# b) entrenadores que hayan ganado más de tres torneos
def entrenadores_mas_de_tres_torneos(entrenadores):
    resultado = [e["nombre"] for e in entrenadores if e["torneos_ganados"] > 3]
    print(f"-> Entrenadores con más de 3 torneos ganados: {resultado}")
    return resultado


# c) el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel_del_mejor_entrenador(entrenadores):
    if not entrenadores:
        return None
    mejor_entrenador = entrenadores[0]
    for e in entrenadores:
        if e["torneos_ganados"] > mejor_entrenador["torneos_ganados"]:
            mejor_entrenador = e

    if not mejor_entrenador["pokemons"]:
        print(f"-> {mejor_entrenador['nombre']} no tiene Pokémon.")
        return None

    mejor_pokemon = mejor_entrenador["pokemons"][0]
    for p in mejor_entrenador["pokemons"]:
        if p["nivel"] > mejor_pokemon["nivel"]:
            mejor_pokemon = p

    print(f"-> Entrenador con más torneos: {mejor_entrenador['nombre']} "
          f"({mejor_entrenador['torneos_ganados']} torneos)")
    print(f"-> Su Pokémon de mayor nivel es: {mejor_pokemon['nombre']} "
          f"(nivel {mejor_pokemon['nivel']})")
    return mejor_pokemon


# d) mostrar todos los datos de un entrenador y sus Pokémon
def mostrar_datos_entrenador(entrenadores, nombre_entrenador):
    e = buscar_entrenador(entrenadores, nombre_entrenador)
    if e is None:
        print(f"-> No se encontró al entrenador '{nombre_entrenador}'.")
        return
    print(f"-> Entrenador: {e['nombre']}")
    print(f"   Torneos ganados: {e['torneos_ganados']}")
    print(f"   Batallas ganadas: {e['batallas_ganadas']} | "
          f"Batallas perdidas: {e['batallas_perdidas']}")
    print("   Pokémon:")
    for p in e["pokemons"]:
        print(f"     - {p['nombre']} | nivel {p['nivel']} | "
              f"tipo {p['tipo']}/{p['subtipo']}")


# e) entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79%
def entrenadores_porcentaje_ganadas_mayor_a(entrenadores, porcentaje=79):
    resultado = []
    for e in entrenadores:
        total = e["batallas_ganadas"] + e["batallas_perdidas"]
        if total == 0:
            continue
        pct = (e["batallas_ganadas"] / total) * 100
        if pct > porcentaje:
            resultado.append((e["nombre"], round(pct, 2)))
    print(f"-> Entrenadores con más de {porcentaje}% de batallas ganadas: {resultado}")
    return resultado


# f) entrenadores que tengan Pokémon de tipo fuego y (planta o agua/volador)
def entrenadores_fuego_y_planta_o_agua_volador(entrenadores):
    resultado = []
    for e in entrenadores:
        tiene_fuego = any(p["tipo"].lower() == "fuego" for p in e["pokemons"])
        tiene_planta = any(p["tipo"].lower() == "planta" for p in e["pokemons"])
        tiene_agua_volador = any(
            p["tipo"].lower() == "agua" and p["subtipo"].lower() == "volador"
            for p in e["pokemons"]
        )
        if tiene_fuego and (tiene_planta or tiene_agua_volador):
            resultado.append(e["nombre"])
    print(f"-> Entrenadores con Pokémon fuego y (planta o agua/volador): {resultado}")
    return resultado


# g) promedio de nivel de los Pokémon de un determinado entrenador
def promedio_nivel(entrenadores, nombre_entrenador):
    e = buscar_entrenador(entrenadores, nombre_entrenador)
    if e is None or not e["pokemons"]:
        print(f"-> No se puede calcular el promedio para '{nombre_entrenador}'.")
        return None
    promedio = sum(p["nivel"] for p in e["pokemons"]) / len(e["pokemons"])
    print(f"-> Promedio de nivel de los Pokémon de {e['nombre']}: {promedio:.2f}")
    return promedio


# h) determinar cuántos entrenadores tienen a un determinado Pokémon
def contar_entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    contador = 0
    for e in entrenadores:
        if any(p["nombre"].lower() == nombre_pokemon.lower() for p in e["pokemons"]):
            contador += 1
    print(f"-> Cantidad de entrenadores que tienen a {nombre_pokemon}: {contador}")
    return contador


# i) mostrar los entrenadores que tienen Pokémon repetidos
def entrenadores_con_pokemons_repetidos(entrenadores):
    resultado = []
    for e in entrenadores:
        nombres = [p["nombre"].lower() for p in e["pokemons"]]
        if len(nombres) != len(set(nombres)):
            resultado.append(e["nombre"])
    print(f"-> Entrenadores con Pokémon repetidos: {resultado}")
    return resultado


# j) entrenadores que tengan uno de los siguientes Pokémon: Tyrantrum, Terrakion o Wingull
def entrenadores_con_alguno_de(entrenadores, lista_pokemons_buscados):
    buscados = [n.lower() for n in lista_pokemons_buscados]
    resultado = []
    for e in entrenadores:
        nombres_pokemon = [p["nombre"].lower() for p in e["pokemons"]]
        if any(n in nombres_pokemon for n in buscados):
            resultado.append(e["nombre"])
    print(f"-> Entrenadores con alguno de {lista_pokemons_buscados}: {resultado}")
    return resultado


# k) determinar si un entrenador "X" tiene al Pokémon "Y"
def tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    e = buscar_entrenador(entrenadores, nombre_entrenador)
    if e is None:
        print(f"-> No existe el entrenador '{nombre_entrenador}'.")
        return False
    for p in e["pokemons"]:
        if p["nombre"].lower() == nombre_pokemon.lower():
            print(f"-> Sí, {e['nombre']} tiene a {p['nombre']} "
                  f"(nivel {p['nivel']}, tipo {p['tipo']}/{p['subtipo']}).")
            return True
    print(f"-> {e['nombre']} no tiene al Pokémon '{nombre_pokemon}'.")
    return False


if __name__ == "__main__":
    entrenadores = [
        crear_entrenador("Ash", 5, 10, 40, [
            {"nombre": "Charizard", "nivel": 78, "tipo": "Fuego", "subtipo": "Volador"},
            {"nombre": "Pikachu", "nivel": 65, "tipo": "Eléctrico", "subtipo": "-"},
            {"nombre": "Wingull", "nivel": 30, "tipo": "Agua", "subtipo": "Volador"},
        ]),
        crear_entrenador("Misty", 2, 8, 22, [
            {"nombre": "Starmie", "nivel": 55, "tipo": "Agua", "subtipo": "Psíquico"},
            {"nombre": "Wingull", "nivel": 40, "tipo": "Agua", "subtipo": "Volador"},
        ]),
        crear_entrenador("Brock", 4, 3, 27, [
            {"nombre": "Onix", "nivel": 60, "tipo": "Roca", "subtipo": "Tierra"},
            {"nombre": "Tyrantrum", "nivel": 70, "tipo": "Roca", "subtipo": "Dragón"},
        ]),
        crear_entrenador("Gary", 7, 5, 50, [
            {"nombre": "Blastoise", "nivel": 80, "tipo": "Agua", "subtipo": "-"},
            {"nombre": "Venusaur", "nivel": 79, "tipo": "Planta", "subtipo": "Veneno"},
            {"nombre": "Arcanine", "nivel": 72, "tipo": "Fuego", "subtipo": "-"},
        ]),
        crear_entrenador("Erika", 1, 15, 5, [
            {"nombre": "Vileplume", "nivel": 45, "tipo": "Planta", "subtipo": "Veneno"},
            {"nombre": "Vileplume", "nivel": 45, "tipo": "Planta", "subtipo": "Veneno"},
        ]),
    ]

    print("=== a) Cantidad de Pokémon de Ash ===")
    cantidad_pokemons(entrenadores, "Ash")

    print("\n=== b) Entrenadores con más de 3 torneos ganados ===")
    entrenadores_mas_de_tres_torneos(entrenadores)

    print("\n=== c) Pokémon de mayor nivel del entrenador con más torneos ===")
    pokemon_mayor_nivel_del_mejor_entrenador(entrenadores)

    print("\n=== d) Todos los datos de Gary ===")
    mostrar_datos_entrenador(entrenadores, "Gary")

    print("\n=== e) Entrenadores con más del 79% de batallas ganadas ===")
    entrenadores_porcentaje_ganadas_mayor_a(entrenadores)

    print("\n=== f) Entrenadores con Pokémon fuego y (planta o agua/volador) ===")
    entrenadores_fuego_y_planta_o_agua_volador(entrenadores)

    print("\n=== g) Promedio de nivel de los Pokémon de Ash ===")
    promedio_nivel(entrenadores, "Ash")

    print("\n=== h) Cuántos entrenadores tienen a Wingull ===")
    contar_entrenadores_con_pokemon(entrenadores, "Wingull")

    print("\n=== i) Entrenadores con Pokémon repetidos ===")
    entrenadores_con_pokemons_repetidos(entrenadores)

    print("\n=== j) Entrenadores con Tyrantrum, Terrakion o Wingull ===")
    entrenadores_con_alguno_de(entrenadores, ["Tyrantrum", "Terrakion", "Wingull"])

    print("\n=== k) ¿Ash tiene a Pikachu? ===")
    tiene_pokemon(entrenadores, "Ash", "Pikachu")
