from collections import deque

cola = deque([
    {"hora": 1100, "app": "Facebook",  "mensaje": "Juan te etiqueto en una foto"},
    {"hora": 1115, "app": "Twitter",   "mensaje": "Nuevo seguidor"},
    {"hora": 1120, "app": "Instagram", "mensaje": "5 nuevos me gusta"},
    {"hora": 1143, "app": "Twitter",   "mensaje": "Tendencia: Python en Buenos Aires"},
    {"hora": 1150, "app": "Facebook",  "mensaje": "Tienes 3 solicitudes pendientes"},
    {"hora": 1200, "app": "Twitter",   "mensaje": "Retweet: Python es el mejor lenguaje"},
    {"hora": 1230, "app": "WhatsApp",  "mensaje": "Mensaje de Maria"},
    {"hora": 1310, "app": "Facebook",  "mensaje": "Comentario en tu publicacion"},
    {"hora": 1510, "app": "Twitter",   "mensaje": "Python: nueva versión disponible"},
    {"hora": 1545, "app": "Instagram", "mensaje": "Nueva historia de Carlos"},
    {"hora": 1557, "app": "Facebook",  "mensaje": "Pedro le gusta tu foto"},
    {"hora": 1610, "app": "Twitter",   "mensaje": "Nuevo mensaje directo"},
])


def eliminar_facebook(cola):
    nueva_cola = deque()
    eliminadas = 0
    while cola:
        notif = cola.popleft()
        if notif["app"] != "Facebook":
            nueva_cola.append(notif)
        else:
            eliminadas += 1
    cola.extend(nueva_cola)
    print(f"Se eliminaron {eliminadas} notificaciones de Facebook.")
    return eliminadas


def mostrar_twitter_python(cola):
    pila = []
    encontradas = 0

    while cola:
        pila.append(cola.popleft())

    print("Notificaciones de Twitter que mencionan 'Python':")
    while pila:
        notif = pila.pop()
        cola.append(notif)
        if notif["app"] == "Twitter" and "Python" in notif["mensaje"]:
            print(f"  {notif['hora']:04d} - {notif['mensaje']}")
            encontradas += 1

    if encontradas == 0:
        print("  Ninguna encontrada.")
    return encontradas


def contar_notificaciones_entre(cola, hora_inicio, hora_fin):
    pila_temp = []
    pila_rango = []

    while cola:
        pila_temp.append(cola.popleft())

    while pila_temp:
        notif = pila_temp.pop()
        cola.append(notif)
        if hora_inicio <= notif["hora"] <= hora_fin:
            pila_rango.append(notif)

    print(f"Notificaciones entre {hora_inicio:04d} y {hora_fin:04d}:")
    for n in pila_rango:
        print(f"  {n['hora']:04d} - {n['app']} - {n['mensaje']}")
    print(f"  Total: {len(pila_rango)}")
    return len(pila_rango)


print("=== a) Eliminar notificaciones de Facebook ===")
eliminar_facebook(cola)

print()
print("=== b) Twitter con 'Python' ===")
mostrar_twitter_python(cola)

print()
print("=== c) Notificaciones entre 11:43 y 15:57 ===")
contar_notificaciones_entre(cola, 1143, 1557)