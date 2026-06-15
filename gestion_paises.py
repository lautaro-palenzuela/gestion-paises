import csv


class CountryManager:
    def __init__(self):
        self.countries = []

    def load_from_file(self, file_name):
        with open(file_name, encoding="utf-8-sig", newline="") as f:
            rows = list(csv.reader(f))
        header = [c.strip().lower() for c in rows[0]]
        self.countries = []
        for row in rows[1:]:
            if not row or all(not c.strip() for c in row):
                continue
            self.countries.append({
                "nombre": row[header.index("nombre")].strip(),
                "poblacion": int(row[header.index("poblacion")].strip()),
                "superficie": int(row[header.index("superficie")].strip()),
                "continente": row[header.index("continente")].strip().title(),
            })
        return self.countries

    def add_country(self, nombre, poblacion, superficie, continente):
        if not nombre or not continente:
            raise ValueError("Nombre y continente no pueden estar vacíos")
        self.countries.append({
            "nombre": nombre.strip(),
            "poblacion": int(poblacion),
            "superficie": int(superficie),
            "continente": continente.strip().title(),
        })

    def update_country(self, nombre, poblacion=None, superficie=None):
        for country in self.countries:
            if country["nombre"].lower() == nombre.lower():
                if poblacion is not None:
                    country["poblacion"] = int(poblacion)
                if superficie is not None:
                    country["superficie"] = int(superficie)
                return country
        raise ValueError("País no encontrado")

    def search_country(self, texto):
        return [c for c in self.countries if texto.lower() in c["nombre"].lower()]

    def filter_by_continent(self, continente):
        return [c for c in self.countries if c["continente"].lower() == continente.lower()]

    def filter_by_population_range(self, min_p=None, max_p=None):
        return [c for c in self.countries if (min_p is None or c["poblacion"] >= min_p) and (max_p is None or c["poblacion"] <= max_p)]

    def filter_by_surface_range(self, min_s=None, max_s=None):
        return [c for c in self.countries if (min_s is None or c["superficie"] >= min_s) and (max_s is None or c["superficie"] <= max_s)]

    def sort_countries(self, field="nombre", reverse=False):
        return sorted(self.countries, key=lambda c: c[field], reverse=reverse)
    
    def sort_countries_manual(self, field="nombre", reverse=False):
        # Copia de la lista para no modificar la original directamente
        result = self.countries.copy()
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Obtener los valores a comparar según el campo
                a = result[j][field]
                b = result[j + 1][field]
                # Si son strings, comparar en minúsculas para orden alfabético correcto
                if isinstance(a, str):
                    a = a.lower()
                    b = b.lower()
                # Determinar si deben intercambiarse
                if (a > b and not reverse) or (a < b and reverse):
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result

    def get_country_with_max_population(self):
        return max(self.countries, key=lambda c: c["poblacion"])

    def get_country_with_min_population(self):
        return min(self.countries, key=lambda c: c["poblacion"])

    def get_average_population(self):
        return sum(c["poblacion"] for c in self.countries) / len(self.countries)

    def get_average_surface(self):
        return sum(c["superficie"] for c in self.countries) / len(self.countries)

    def get_countries_per_continent(self):
        counts = {}
        for c in self.countries:
            counts[c["continente"]] = counts.get(c["continente"], 0) + 1
        return counts
    
    def save_to_file(self, file_name="paises.csv"):
        with open(file_name, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "poblacion", "superficie", "continente"])
            for c in self.countries:
                writer.writerow([c["nombre"], c["poblacion"], c["superficie"], c["continente"]])


def show(countries):
    if not countries:
        print("No se encontraron resultados.")
        return
    for c in countries:
        print(f"- {c['nombre']} | Población: {c['poblacion']} | Superficie: {c['superficie']} | Continente: {c['continente']}")


def main():
    manager = CountryManager()
    try:
        manager.load_from_file("paises.csv")
    except FileNotFoundError:
        print("Archivo paises.csv no encontrado. Se creará uno nuevo al guardar datos.")
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        print("Se iniciará con una lista vacía.")

    while True:
        print("\n1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar por continente")
        print("5. Filtrar por población")
        print("6. Filtrar por superficie")
        print("7. Ordenar")
        print("8. Estadísticas")
        print("9. Salir")
        option = input("Elija una opción: ")

        if option == "1":
            try:
                nombre = input("Nombre: ")
                poblacion = input("Población: ")
                superficie = input("Superficie: ")
                continente = input("Continente: ")
                manager.add_country(nombre, poblacion, superficie, continente)
                print("País agregado")
            except ValueError as e:
                print(f"Error: {e}. Asegurate de que población y superficie sean números enteros.")

        elif option == "2":
            try:
                nombre = input("Nombre: ")
                pob_input = input("Nueva población (vacío para no cambiar): ")
                sup_input = input("Nueva superficie (vacío para no cambiar): ")
                nueva_pob = int(pob_input) if pob_input.strip() else None
                nueva_sup = int(sup_input) if sup_input.strip() else None
                manager.update_country(nombre, nueva_pob, nueva_sup)
                print("País actualizado")
            except ValueError:
                print("Error: Población y superficie deben ser números enteros válidos.")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "3":
            show(manager.search_country(input("Texto a buscar: ")))

        elif option == "4":
            show(manager.filter_by_continent(input("Continente: ")))

        elif option == "5":
            try:
                min_p = input("Mínima (opcional): ")
                max_p = input("Máxima (opcional): ")
                min_val = int(min_p) if min_p.strip() else None
                max_val = int(max_p) if max_p.strip() else None
                show(manager.filter_by_population_range(min_val, max_val))
            except ValueError:
                print("Error: Los rangos deben ser números enteros.")

        elif option == "6":
            try:
                min_s = input("Mínima (opcional): ")
                max_s = input("Máxima (opcional): ")
                min_val = int(min_s) if min_s.strip() else None
                max_val = int(max_s) if max_s.strip() else None
                show(manager.filter_by_surface_range(min_val, max_val))
            except ValueError:
                print("Error: Los rangos deben ser números enteros.")

        elif option == "7":
            field = input("Campo (nombre/poblacion/superficie): ").strip().lower()
            reverse = input("Descendente? s/n: ").lower() == "s"
            show(manager.sort_countries_manual(field, reverse))

        elif option == "8":
            print("Mayor población:", manager.get_country_with_max_population()["nombre"])
            print("Menor población:", manager.get_country_with_min_population()["nombre"])
            print("Promedio población:", manager.get_average_population())
            print("Promedio superficie:", manager.get_average_surface())
            print("Por continente:", manager.get_countries_per_continent())

        elif option == "9":
            manager.save_to_file()
            print("Datos guardados. ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
