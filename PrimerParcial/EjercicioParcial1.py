#  EJERCICIO 1
# Lista simple de 15 superheroes
lista_heroes = [
    "Iron Man", "Captain America", "Thor", "Hulk", "Black Widow",
    "Hawkeye", "Spider-Man", "Black Panther", "Doctor Strange", "Ant-Man",
    "Scarlet Witch", "Vision", "Falcon", "War Machine", "Wolverine"
]

# Funcion recursiva para buscar si "Captain America" esta en la lista
def buscar_heroe(lista, objetivo, indice=0):
    if indice == len(lista):
        return False
    if lista[indice] == objetivo:
        return True
    return buscar_heroe(lista, objetivo, indice + 1)

# Funcion recursiva para listar los superheroes de la lista
def listar_heroes(lista, indice=0):
    if indice == len(lista):
        return
    print(f"  - {lista[indice]}")
    listar_heroes(lista, indice + 1)

print("=" * 60)
print("EJERCICIO 1")
print("=" * 60)

print(f"\nLista de {len(lista_heroes)} superheroes:")
listar_heroes(lista_heroes)

resultado = buscar_heroe(lista_heroes, "Captain America")
print(f"\nCaptain America esta en la lista? -> {resultado}")

resultado2 = buscar_heroe(lista_heroes, "Deadpool")
print(f"Deadpool esta en la lista?        -> {resultado2}")