class Vehiculo:
    def __init__(self, marca, modelo, precio_por_dia, disponible=True):
        self.marca = marca
        self.modelo = modelo
        self.precio_por_dia = precio_por_dia
        self.disponible = disponible

    def informacion(self):
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio x día: ${self.precio_por_dia:.2f}")
        print(f"Disponibilidad: {disponibilidad}")

    def alquilar(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.marca} {self.modelo} ha sido alquilado.")
        else:
            print(f"El vehículo {self.marca} {self.modelo} no está disponible para alquiler.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El vehículo {self.marca} {self.modelo} ha sido devuelto y está disponible para alquiler.")
        else:
            print(f"El vehículo {self.marca} {self.modelo} ya estaba disponible para alquiler.")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, precio_por_dia, tipo_combustible, disponible=True):
        super().__init__(marca, modelo, precio_por_dia, disponible)
        self.tipo_combustible = tipo_combustible

    def informacion(self):
        super().informacion()
        print(f"Tipo de combustible: {self.tipo_combustible}")

# Lo usaríamos asi, aunque se le podría agregar un menú, pero no se si es el objetivo por ahí
vehiculo1 = Vehiculo("Nissan", "Sentra", 45000.0)
vehiculo1.informacion()
vehiculo1.alquilar()
vehiculo1.informacion()
vehiculo1.devolver()
vehiculo1.informacion()

coche1 = Coche("Toyota", "Corolla Cross", 47000.0, "Hibrido")
coche1.informacion()
coche1.alquilar()
coche1.informacion()
coche1.devolver()
coche1.informacion()
