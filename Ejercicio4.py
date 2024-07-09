class Curso:
    def __init__(self, titulo, instructor, precio, disponible=False):
        self.titulo = titulo
        self.instructor = instructor
        self.precio = precio
        self.disponible = disponible

    def informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Instructor: {self.instructor}")
        print(f"Precio: {self.precio:.2f}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")

    def abrir_inscripciones(self):
        self.disponible = True

    def cerrar_inscripciones(self):
        self.disponible = False


class CursoOnline(Curso):
    def __init__(self, titulo, instructor, precio, duracion, disponible=False):
        super().__init__(titulo, instructor, precio, disponible)
        self.duracion = duracion

    def informacion(self):
        super().informacion()
        print(f"Duración: {self.duracion} semanas")


# Sería algo así y con un lenguaje recordado :)
curso1 = Curso("Logo Básico", "Carlos Gongora", 49999.99)
curso1.informacion()
curso1.abrir_inscripciones()
curso1.informacion()

print()

curso_online1 = CursoOnline("Logo Avanzado", "Alberto Gongora", 52999.99, 8)
curso_online1.informacion()
curso_online1.cerrar_inscripciones()
curso_online1.informacion()
