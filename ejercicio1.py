# Definición de las clases Empleado y Gerente

class Empleado:
    def __init__(self, nombre, edad, salario, activo=True):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.activo = activo

    def informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}, Activo: {self.activo}")

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, activo, departamento):
        super().__init__(nombre, edad, salario, activo)
        self.departamento = departamento

    def informacion(self):
        super().informacion()
        print(f"Departamento: {self.departamento}")

# Definición de las funciones de gestión
empleados = []
gerentes = {}

departamentos = ["Ventas", "Logistica", "Calidad", "Recursos Humanos", "Produccion", "Ingeniería", "Mantenimiento"]

def agregar_empleado():
    nombre = input("Nombre del empleado: ")
    edad = int(input("Edad del empleado: "))
    salario = float(input("Salario del empleado: "))
    empleado = Empleado(nombre, edad, salario)
    empleados.append(empleado)
    print("Empleado agregado exitosamente.")

def quitar_empleado():
    nombre = input("Nombre del empleado a quitar: ")
    for empleado in empleados:
        if empleado.nombre == nombre:
            empleados.remove(empleado)
            print("Empleado quitado exitosamente.")
            return
    print("Empleado no encontrado.")

def listar_empleados():
    if empleados:
        for empleado in empleados:
            empleado.informacion()
    else:
        print("No hay empleados.")

def mostrar_menu_departamentos():
    print("\nSeleccione el departamento:")
    for i, depto in enumerate(departamentos, 1):
        print(f"{i}. {depto}")
    opcion = int(input("Ingrese el número del departamento: "))
    if 1 <= opcion <= len(departamentos):
        return departamentos[opcion - 1]
    else:
        print("Opción no válida.")
        return None

def reasignar_gerente(gerente_antiguo):
    nuevo_departamento = mostrar_menu_departamentos()
    if nuevo_departamento is None:
        return
    if nuevo_departamento in gerentes:
        print(f"El departamento {nuevo_departamento} ya tiene un gerente.")
    else:
        gerente_antiguo.departamento = nuevo_departamento
        gerentes[nuevo_departamento] = gerente_antiguo
        print(f"Gerente reasignado al departamento {nuevo_departamento} exitosamente.")

def agregar_gerente():
    nombre = input("Nombre del gerente: ")
    edad = int(input("Edad del gerente: "))
    salario = float(input("Salario del gerente: "))
    departamento = mostrar_menu_departamentos()
    if departamento is None:
        return
    if departamento in gerentes:
        reemplazar = input(f"El departamento {departamento} ya tiene un gerente. ¿Reemplazar? (si/no): ")
        if reemplazar.lower() == 'si':
            accion = input("¿Desea cambiar al antiguo gerente a otro departamento o quitarlo? (cambiar/quitar): ")
            if accion.lower() == 'cambiar':
                gerente_antiguo = gerentes.pop(departamento)
                reasignar_gerente(gerente_antiguo)
            elif accion.lower() == 'quitar':
                gerentes.pop(departamento)
            else:
                print("Acción no válida.")
                return
        else:
            return
    gerente = Gerente(nombre, edad, salario, True, departamento)
    gerentes[departamento] = gerente
    print("Gerente agregado exitosamente.")

def quitar_gerente():
    print("\nSeleccione el departamento del gerente a quitar:")
    departamento = mostrar_menu_departamentos()
    if departamento is None:
        return
    if departamento in gerentes:
        gerente = gerentes[departamento]
        accion = input("¿Desea reasignar al gerente a otro departamento? (si/no): ")
        if accion.lower() == 'si':
            reasignar_gerente(gerente)
        del gerentes[departamento]
        print("Gerente quitado exitosamente.")
    else:
        print("Departamento no encontrado o sin gerente.")

def listar_gerentes():
    if gerentes:
        for gerente in gerentes.values():
            gerente.informacion()
    else:
        print("No hay gerentes.")

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú de Gestión de Empleados y Gerentes ---")
        print("1. Agregar Empleado")
        print("2. Quitar Empleado")
        print("3. Listar Empleados")
        print("4. Agregar Gerente")
        print("5. Quitar Gerente")
        print("6. Listar Gerentes")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_empleado()
        elif opcion == '2':
            quitar_empleado()
        elif opcion == '3':
            listar_empleados()
        elif opcion == '4':
            agregar_gerente()
        elif opcion == '5':
            quitar_gerente()
        elif opcion == '6':
            listar_gerentes()
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del menú
menu()



