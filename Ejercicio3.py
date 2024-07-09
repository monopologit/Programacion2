class Producto:
    def __init__(self, nombre, categoria, precio, en_stock=True):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.en_stock = en_stock

    def informacion(self):
        estado = "en stock" if self.en_stock else "sin stock"
        print(f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio:.2f}, Estado: {estado}")

    def vender(self):
        self.en_stock = False

    def reponer(self):
        self.en_stock = True

class ProductoElectronico(Producto):
    def __init__(self, nombre, categoria, precio, garantia, en_stock=True):
        super().__init__(nombre, categoria, precio, en_stock)
        self.garantia = garantia

    def informacion(self):
        estado = "en stock" if self.en_stock else "sin stock"
        print(f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio:.2f}, Estado: {estado}, Garantía: {self.garantia} meses")
# Crear un producto
producto1 = Producto("Pantalon", "Ropa", 49999.99)
producto1.informacion()  # Mostrar info del producto
producto1.vender()  # Cambiar el estado a sin stock
producto1.informacion()  # Mostrar info del producto después de vender
producto1.reponer()  # Cambiar el estado a en stock
producto1.informacion()  # Mostramos la info del producto después de reponer

# Crear un producto electrónico
producto_electronico1 = ProductoElectronico("Tablet", "Electrónica", 99999.99, 6)
producto_electronico1.informacion()  # Mostramos info del producto electrónico
producto_electronico1.vender()  # Cambiamos el estado a sin stock
producto_electronico1.informacion()  # Mostramos la info del producto electrónico después de vender
producto_electronico1.reponer()  # Cambio el estado a en stock
producto_electronico1.informacion()  # Mostramos la info del producto electrónico después de reponer
