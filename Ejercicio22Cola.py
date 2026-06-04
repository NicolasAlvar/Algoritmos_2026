from collections import deque

# Las bitacoras se almacenan en pilas (la ultima mision es la primera en salir)
# Cada mision: (planeta, capturado, recompensa)

pila_boba = deque()
pila_boba.append(("Tatooine",     "Greedo",          5000))
pila_boba.append(("Hoth",         "Rebel Soldier",   3000))
pila_boba.append(("Bespin",       "Han Solo",        250000))
pila_boba.append(("Coruscant",    "Doctor Evazan",   8000))
pila_boba.append(("Jabba Palace", "Lando Calrissian",15000))

pila_din = deque()
pila_din.append(("Nevarro",   "Mythrol",      5000))
pila_din.append(("Arvala-7",  "El Nino",      0))
pila_din.append(("Sorgan",    "Klatooinian",  2000))
pila_din.append(("Maldo Kreis","Qin",         12000))
pila_din.append(("Trask",     "Qin (again)",  9000))


print("=" * 60)
print("a) Planetas visitados en orden de mision (del fondo a la cima)")
print("=" * 60)

print("\nBoba Fett:")
for mision in pila_boba:
    print(f"  {mision[0]}")

print("\nDin Djarin (The Mandalorian):")
for mision in pila_din:
    print(f"  {mision[0]}")


print("\n" + "=" * 60)
print("b) Total de creditos recaudados y quien obtuvo mayor fortuna")
print("=" * 60)

total_boba = sum(m[2] for m in pila_boba)
total_din  = sum(m[2] for m in pila_din)

print(f"\n  Boba Fett           : {total_boba} creditos galacticos")
print(f"  Din Djarin          : {total_din} creditos galacticos")

ganador = "Boba Fett" if total_boba > total_din else "Din Djarin"
print(f"\n  Mayor fortuna       : {ganador}")


print("\n" + "=" * 60)
print("c) Numero de mision en la que Boba Fett capturo a Han Solo")
print("   (posicion desde el fondo de la pila, empezando en 1)")
print("=" * 60)

for i, mision in enumerate(pila_boba, 1):
    if "Han Solo" in mision[1]:
        print(f"\n  Mision numero {i} (capturado en: {mision[0]})")
        break


print("\n" + "=" * 60)
print("d) Cantidad de capturas por cazarrecompensas")
print("=" * 60)

print(f"\n  Boba Fett  : {len(pila_boba)} capturas")
print(f"  Din Djarin : {len(pila_din)} capturas")