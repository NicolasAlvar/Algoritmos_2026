from collections import deque
 
naves_datos = [
    ("Millennium Falcon",   34.37,  4,      6),
    ("Death Star",          120000, 342953, 843342),
    ("X-wing",              12.5,   1,      0),
    ("TIE Fighter",         6.4,    1,      0),
    ("Star Destroyer",      1600,   47060,  0),
    ("Executor",            19000,  279144, 38000),
    ("AT-AT",               20.6,   5,      40),
    ("AT-ST",               2.0,    2,      0),
    ("AT-TE",               13.2,   6,      36),
    ("AT-RT",               3.2,    1,      0),
    ("Slave 1",             21.5,   1,      6),
    ("Imperial Shuttle",    20.0,   6,      20),
    ("Y-wing",              14.0,   2,      0),
    ("A-wing",              9.6,    1,      0),
    ("B-wing",              16.9,   1,      0),
    ("Sand Crawler",        36.8,   46,     30),
    ("Sail Barge",          30.0,   26,     500),
    ("Naboo Fighter",       11.0,   1,      0),
    ("Republic Cruiser",    115.0,  9,      16),
    ("Jedi Starfighter",    8.0,    1,      0),
]
 
cola = deque()
for nombre, largo, tripulacion, pasajeros in naves_datos:
    cola.append({
        "nombre":      nombre,
        "largo":       largo,
        "tripulacion": tripulacion,
        "pasajeros":   pasajeros,
    })
 
naves = list(cola)
 
def mostrar(nave):
    print(f"  Nombre      : {nave['nombre']}")
    print(f"  Largo       : {nave['largo']} m")
    print(f"  Tripulacion : {nave['tripulacion']}")
    print(f"  Pasajeros   : {nave['pasajeros']}")
 
 
print("=" * 60)
print("a) Por nombre (asc) y por largo (desc)")
print("=" * 60)
 
print("\nPor nombre (ascendente):")
for n in sorted(naves, key=lambda x: x["nombre"]):
    print(f"  {n['nombre']}")
 
print("\nPor largo (descendente):")
for n in sorted(naves, key=lambda x: x["largo"], reverse=True):
    print(f"  {n['nombre']:<25} {n['largo']} m")
 
 
print("\n" + "=" * 60)
print("b) Halcon Milenario y Estrella de la Muerte")
print("=" * 60)
 
for buscar in ["Millennium Falcon", "Death Star"]:
    nave = next((n for n in naves if buscar.lower() in n["nombre"].lower()), None)
    if nave:
        print(f"\n{nave['nombre']}:")
        mostrar(nave)
 
 
print("\n" + "=" * 60)
print("c) Cinco naves con mayor cantidad de pasajeros")
print("=" * 60)
 
for i, n in enumerate(sorted(naves, key=lambda x: x["pasajeros"], reverse=True)[:5], 1):
    print(f"  {i}. {n['nombre']:<25} {n['pasajeros']} pasajeros")
 
 
print("\n" + "=" * 60)
print("d) Nave con mayor tripulacion")
print("=" * 60)
 
mostrar(max(naves, key=lambda x: x["tripulacion"]))
 
 
print("\n" + "=" * 60)
print("e) Naves que comienzan con AT")
print("=" * 60)
 
for n in naves:
    if n["nombre"].upper().startswith("AT"):
        print(f"  {n['nombre']}")
 
 
print("\n" + "=" * 60)
print("f) Naves con seis o mas pasajeros")
print("=" * 60)
 
for n in naves:
    if n["pasajeros"] >= 6:
        print(f"  {n['nombre']:<25} {n['pasajeros']} pasajeros")
 
 
print("\n" + "=" * 60)
print("g) Nave mas pequena y nave mas grande")
print("=" * 60)
 
print("\nMas pequena:")
mostrar(min(naves, key=lambda x: x["largo"]))
print("\nMas grande:")
mostrar(max(naves, key=lambda x: x["largo"]))