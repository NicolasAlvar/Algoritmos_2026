
# EJERCICIO 20 - Robot con pila de movimientos
# Algoritmos y Estructuras de Datos - Tema: Pilas
# El robot se mueve en 8 direcciones:
# Norte, Sur, Este, Oeste, Noreste, Noroeste, Sureste, Suroroeste

# --- Dirección opuesta para el retorno ---
OPUESTO = {
    'N':  'S',
    'S':  'N',
    'E':  'O',
    'O':  'E',
    'NE': 'SO',
    'NO': 'SE',
    'SE': 'NO',
    'SO': 'NE',
}

DIRECCIONES_VALIDAS = list(OPUESTO.keys())

# Algoritmo 1: registrar movimientos del robot usando una pila
def registrar_movimientos():
    """
    Solicita al usuario los movimientos del robot y los apila.
    Devuelve la pila con todos los movimientos registrados.
    """
    pila = []
    print("\n=== REGISTRO DE MOVIMIENTOS DEL ROBOT ===")
    print(f"Direcciones válidas: {', '.join(DIRECCIONES_VALIDAS)}")
    print("Escriba 'FIN' para terminar el ingreso.\n")

    while True:
        movimiento = input("Ingrese dirección: ").strip().upper()
        if movimiento == 'FIN':
            break
        if movimiento in DIRECCIONES_VALIDAS:
            pila.append(movimiento)
            print(f"  -> '{movimiento}' apilado. Pila actual: {pila}")
        else:
            print(f"  [!] Dirección '{movimiento}' no válida. Intente de nuevo.")

    return pila

# Algoritmo 2: generar secuencia de retorno desapilando
def retornar_al_origen(pila_movimientos):
    """
    Desapila los movimientos registrados y genera la secuencia
    de movimientos inversos para regresar al punto de partida.
    Devuelve la lista de movimientos de retorno.
    """
    pila = list(pila_movimientos)   # copia para no destruir la original
    retorno = []

    print("\n=== SECUENCIA DE RETORNO AL ORIGEN ===")
    print(f"Pila de movimientos realizados: {pila}\n")

    while pila:
        ultimo = pila.pop()          # desapilar último movimiento
        inverso = OPUESTO[ultimo]    # obtener la dirección contraria
        retorno.append(inverso)
        print(f"  Desapilado '{ultimo}'  ->  moverse en '{inverso}'")

    print(f"\nSecuencia de retorno: {retorno}")
    return retorno


if __name__ == "__main__":
    pila = registrar_movimientos()

    if not pila:
        print("\nNo se registraron movimientos.")
    else:
        print(f"\nMovimientos registrados ({len(pila)}): {pila}")
        retornar_al_origen(pila)