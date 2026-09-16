"""
Ejercicio 6 - Tema Lista (Capítulo VIII)
-----------------------------------------
Dada una lista de superhéroes de comics, de los cuales se conoce su nombre,
año de aparición, casa de comic (Marvel o DC) y biografía, implementar las
funciones necesarias para poder realizar las actividades a) a i).

Se implementa una LISTA ENLAZADA SIMPLE (con Nodo y puntero "siguiente"),
tal como se define el TDA Lista en el capítulo del libro.
"""


class Nodo:
    def __init__(self, nombre, anio, casa, biografia):
        self.nombre = nombre
        self.anio = anio
        self.casa = casa
        self.biografia = biografia
        self.siguiente = None


class ListaHeroes:
    def __init__(self):
        self.cabeza = None

    # --- operaciones básicas de la lista enlazada ---
    def insertar(self, nombre, anio, casa, biografia):
        nuevo = Nodo(nombre, anio, casa, biografia)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def buscar(self, nombre):
        actual = self.cabeza
        while actual is not None:
            if actual.nombre.lower() == nombre.lower():
                return actual
            actual = actual.siguiente
        return None

    # a) eliminar el nodo que contiene la información de un superhéroe
    def eliminar_nodo(self, nombre):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.nombre.lower() == nombre.lower():
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                print(f"-> Se eliminó a '{nombre}' de la lista.")
                return True
            anterior = actual
            actual = actual.siguiente
        print(f"-> No se encontró a '{nombre}'.")
        return False

    # b) mostrar el año de aparición de un superhéroe puntual
    def mostrar_anio(self, nombre):
        nodo = self.buscar(nombre)
        if nodo:
            print(f"-> {nodo.nombre} apareció en el año {nodo.anio}.")
            return nodo.anio
        print(f"-> No se encontró a '{nombre}'.")
        return None

    # c) cambiar la casa de un superhéroe
    def cambiar_casa(self, nombre, nueva_casa):
        nodo = self.buscar(nombre)
        if nodo:
            nodo.casa = nueva_casa
            print(f"-> Ahora {nodo.nombre} pertenece a {nueva_casa}.")
            return True
        print(f"-> No se encontró a '{nombre}'.")
        return False

    # d) mostrar nombre de superhéroes cuya biografía menciona una palabra
    def buscar_por_palabra_en_biografia(self, palabra):
        encontrados = []
        actual = self.cabeza
        while actual is not None:
            if palabra.lower() in actual.biografia.lower():
                encontrados.append(actual.nombre)
            actual = actual.siguiente
        print(f"-> Superhéroes cuya biografía menciona '{palabra}': {encontrados}")
        return encontrados

    # e) mostrar nombre y casa de superhéroes con aparición anterior a un año
    def anteriores_a(self, anio_limite):
        resultado = []
        actual = self.cabeza
        while actual is not None:
            if actual.anio < anio_limite:
                resultado.append((actual.nombre, actual.casa))
            actual = actual.siguiente
        print(f"-> Aparecidos antes de {anio_limite}: {resultado}")
        return resultado

    # f) mostrar la casa a la que pertenecen ciertos superhéroes
    def mostrar_casa_de(self, nombres):
        for nombre in nombres:
            nodo = self.buscar(nombre)
            if nodo:
                print(f"-> {nodo.nombre} pertenece a {nodo.casa}.")
            else:
                print(f"-> No se encontró a '{nombre}'.")

    # g) mostrar toda la información de ciertos superhéroes
    def mostrar_info_de(self, nombres):
        for nombre in nombres:
            nodo = self.buscar(nombre)
            if nodo:
                print(f"-> Nombre: {nodo.nombre} | Año: {nodo.anio} | "
                      f"Casa: {nodo.casa} | Biografía: {nodo.biografia}")
            else:
                print(f"-> No se encontró a '{nombre}'.")

    # h) listar los superhéroes que comienzan con determinadas letras
    def listar_que_comienzan_con(self, letras):
        letras = [l.upper() for l in letras]
        resultado = []
        actual = self.cabeza
        while actual is not None:
            if actual.nombre[0].upper() in letras:
                resultado.append(actual.nombre)
            actual = actual.siguiente
        print(f"-> Superhéroes que comienzan con {letras}: {resultado}")
        return resultado

    # i) determinar cuántos superhéroes hay de cada casa de comic
    def contar_por_casa(self):
        conteo = {}
        actual = self.cabeza
        while actual is not None:
            conteo[actual.casa] = conteo.get(actual.casa, 0) + 1
            actual = actual.siguiente
        print(f"-> Cantidad de superhéroes por casa: {conteo}")
        return conteo

    def mostrar_todos(self):
        actual = self.cabeza
        while actual is not None:
            print(f"  * {actual.nombre} ({actual.casa}, {actual.anio})")
            actual = actual.siguiente


if __name__ == "__main__":
    lista = ListaHeroes()
    lista.insertar("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor curativo.")
    lista.insertar("Linterna Verde", 1940, "DC", "Porta un anillo de poder alimentado por fuerza de voluntad.")
    lista.insertar("Dr. Strange", 1963, "Marvel", "Hechicero supremo, antes cirujano; usa una capa mágica.")
    lista.insertar("Capitana Marvel", 1968, "Marvel", "Ex piloto militar con poderes cósmicos, viste un traje ajustado.")
    lista.insertar("Mujer Maravilla", 1941, "DC", "Princesa amazona con lazo de la verdad y armadura dorada.")
    lista.insertar("Flash", 1940, "DC", "Corre a velocidades sobrehumanas gracias a la Fuerza de Velocidad.")
    lista.insertar("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia, usa una armadura élite.")
    lista.insertar("Batman", 1939, "DC", "Detective y vigilante que combate el crimen en Gotham.")
    lista.insertar("Superman", 1938, "DC", "Kryptoniano con superfuerza y visión de calor.")

    print("=== Lista inicial ===")
    lista.mostrar_todos()

    print("\n=== a) Eliminar a Linterna Verde ===")
    lista.eliminar_nodo("Linterna Verde")

    print("\n=== b) Año de aparición de Wolverine ===")
    lista.mostrar_anio("Wolverine")

    print("\n=== c) Cambiar la casa de Dr. Strange a Marvel ===")
    lista.cambiar_casa("Dr. Strange", "Marvel")

    print("\n=== d) Biografía menciona 'traje' o 'armadura' ===")
    encontrados_traje = set(lista.buscar_por_palabra_en_biografia("traje"))
    encontrados_armadura = set(lista.buscar_por_palabra_en_biografia("armadura"))
    print(f"-> Unión (traje o armadura): {encontrados_traje | encontrados_armadura}")

    print("\n=== e) Aparecidos antes de 1963 ===")
    lista.anteriores_a(1963)

    print("\n=== f) Casa de Capitana Marvel y Mujer Maravilla ===")
    lista.mostrar_casa_de(["Capitana Marvel", "Mujer Maravilla"])

    print("\n=== g) Info completa de Flash y Star-Lord ===")
    lista.mostrar_info_de(["Flash", "Star-Lord"])

    print("\n=== h) Comienzan con B, M o S ===")
    lista.listar_que_comienzan_con(["B", "M", "S"])

    print("\n=== i) Cantidad por casa ===")
    lista.contar_por_casa()