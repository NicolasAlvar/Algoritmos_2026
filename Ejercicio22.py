def usar_la_fuerza(mochila, intentos=0):
    """
    Saca objetos de la mochila de a uno hasta encontrar un sable de luz
    o hasta que no queden más objetos.
    
    Retorna una tupla: (encontrado: bool, intentos: int)
    """
    # Caso base 1: mochila vacía → no encontró sable
    if len(mochila) == 0:
        return (False, intentos)
    
    objeto_actual = mochila[0]
    print(f"Sacando objeto #{intentos + 1}: '{objeto_actual}'")
    
    # Caso base 2: encontró el sable de luz
    if objeto_actual == "sable de luz":
        return (True, intentos + 1)
    
    # Caso recursivo: sigue buscando en el resto de la mochila
    return usar_la_fuerza(mochila[1:], intentos + 1)


# ── Mochila representada como vector (lista) ────────────────────
mochila_jedi = [
    "comlink",
    "racion",
    "capa",
    "sable de luz",   # ← está en la mochila
    "holocron",
]

# ── Ejecución ───────────────────────────────────────────────────
encontrado, cantidad = usar_la_fuerza(mochila_jedi)

print()
if encontrado:
    print(f"¡El Jedi encontró el sable de luz!")
    print(f"Objetos sacados para encontrarlo: {cantidad}")
else:
    print("No había sable de luz en la mochila.")
    print(f"Objetos revisados: {cantidad}")