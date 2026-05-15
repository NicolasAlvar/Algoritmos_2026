
# EJERCICIO 24 - Personajes del MCU con pila
# Algoritmos y Estructuras de Datos - Tema: Pilas
# Cada elemento de la pila es un tuple: (nombre, peliculas)
# La cima de la pila es el último elemento de la lista.

# Datos de ejemplo cargados en la pila
def cargar_pila_mcu():
    """
    Crea y devuelve la pila de personajes MCU.
    Formato de cada elemento: (nombre, cantidad_de_peliculas)
    El último en ser apilado queda en la CIMA.
    """
    pila = []
    personajes = [
        ("Thor",            9),
        ("Black Widow",     7),
        ("Captain America", 6),
        ("Iron Man",        10),
        ("Hulk",            5),
        ("Hawkeye",         4),
        ("Groot",           5),
        ("Rocket Raccoon",  6),
        ("Gamora",          5),
        ("Star-Lord",       4),
        ("Spider-Man",      5),
        ("Doctor Strange",  4),
        ("Black Panther",   3),
        ("Scarlet Witch",   6),
        ("Vision",          3),
        ("Falcon",          5),
        ("War Machine",     5),
        ("Ant-Man",         3),
        ("Captain Marvel",  3),
        ("Nebula",          6),
    ]
    for p in personajes:
        pila.append(p)
    return pila



# a) Posición de Rocket Raccoon y Groot desde la cima (pos 1)
def posicion_rocket_groot(pila):
    """
    Determina la posición de Rocket Raccoon y Groot en la pila.
    La cima es posición 1.
    """
    print("\n=== a) POSICIÓN DE ROCKET RACCOON Y GROOT ===")
    n = len(pila)
    buscados = {"Rocket Raccoon", "Groot"}
    encontrados = {}

    for i in range(n):
        nombre = pila[i][0]
        if nombre in buscados:
            # posición desde la cima: el último elemento es posición 1
            pos_cima = n - i
            encontrados[nombre] = pos_cima

    for nombre in buscados:
        if nombre in encontrados:
            print(f"  {nombre}: posición {encontrados[nombre]} desde la cima")
        else:
            print(f"  {nombre}: no encontrado en la pila")


# b) Personajes con más de 5 películas y su cantidad
def personajes_mas_de_5_peliculas(pila):
    """
    Muestra los personajes que participaron en más de 5 películas.
    """
    print("\n=== b) PERSONAJES CON MÁS DE 5 PELÍCULAS ===")
    encontrados = [(nombre, peliculas) for nombre, peliculas in pila if peliculas > 5]

    if encontrados:
        for nombre, peliculas in encontrados:
            print(f"  {nombre}: {peliculas} películas")
    else:
        print("  Ningún personaje supera las 5 películas.")


# c) Cantidad de películas de Black Widow
def peliculas_black_widow(pila):
    """
    Busca a Black Widow en la pila e informa cuántas películas tiene.
    """
    print("\n=== c) PELÍCULAS DE BLACK WIDOW ===")
    for nombre, peliculas in pila:
        if nombre == "Black Widow":
            print(f"  Black Widow participó en {peliculas} película(s).")
            return
    print("  Black Widow no se encuentra en la pila.")



# d) Personajes cuyo nombre empieza con C, D o G

def nombres_con_cdg(pila):
    """
    Muestra todos los personajes cuyo nombre empieza con C, D o G.
    """
    print("\n=== d) PERSONAJES QUE EMPIEZAN CON C, D o G ===")
    letras = {'C', 'D', 'G'}
    encontrados = [(nombre, peliculas) for nombre, peliculas in pila
                   if nombre[0].upper() in letras]

    if encontrados:
        for nombre, peliculas in encontrados:
            print(f"  {nombre} ({peliculas} películas)")
    else:
        print("  No se encontraron personajes con esas iniciales.")


if __name__ == "__main__":
    pila = cargar_pila_mcu()

    print("=== PILA DE PERSONAJES MCU ===")
    print("(Cima -> Fondo)\n")
    for i in range(len(pila) - 1, -1, -1):
        nombre, peliculas = pila[i]
        pos = len(pila) - i
        print(f"  [{pos:2}] {nombre} - {peliculas} película(s)")

    # Resolver cada inciso
    posicion_rocket_groot(pila)
    personajes_mas_de_5_peliculas(pila)
    peliculas_black_widow(pila)
    nombres_con_cdg(pila)