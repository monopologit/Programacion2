Ejercicios de práctica para parcial
Ejercicio N° 1: Sistema de Gestión de Empleados

Imagina que estás desarrollando un sistema de gestión de empleados para una empresa. Tu tarea es implementar un sistema que permita gestionar la información de los empleados y realizar ciertas operaciones sobre ellos.

Crea una clase llamada Empleado que tenga los siguientes atributos:
nombre: una cadena que representa el nombre del empleado.
edad: un número entero que indica la edad del empleado.
salario: un número decimal que indica el salario del empleado.
activo: un valor booleano que indica si el empleado está activo en la empresa.
La clase Empleado debe tener los siguientes métodos:
informacion(): muestra por pantalla la información del empleado, incluyendo el nombre, edad y salario.
activar(): cambia el estado del empleado a activo.
desactivar(): cambia el estado del empleado a inactivo.
Crea una clase derivada llamada Gerente que herede de la clase Empleado. La clase Gerente tiene un atributo adicional:
departamento: una cadena que indica el departamento del que es responsable el gerente.
Sobrescribe el método informacion() en la clase Gerente para incluir el departamento al mostrar la información.
Ejercicio N° 2: Sistema de Gestión de Vehículos

Imagina que estás desarrollando un sistema de gestión de vehículos para una empresa de alquiler de coches. Tu tarea es implementar un sistema que permita gestionar la información de los vehículos y realizar ciertas operaciones sobre ellos.

Crea una clase llamada Vehiculo que tenga los siguientes atributos:
marca: una cadena que representa la marca del vehículo.
modelo: una cadena que indica el modelo del vehículo.
precio_por_dia: un número decimal que indica el precio de alquiler por día del vehículo.
disponible: un valor booleano que indica si el vehículo está disponible para alquiler.
La clase Vehiculo debe tener los siguientes métodos:
informacion(): muestra por pantalla la información del vehículo, incluyendo la marca, modelo y precio por día.
alquilar(): cambia el estado del vehículo a no disponible.
devolver(): cambia el estado del vehículo a disponible.
Crea una clase derivada llamada Coche que herede de la clase Vehiculo. La clase Coche tiene un atributo adicional:
tipo_combustible: una cadena que indica el tipo de combustible del coche (por ejemplo, gasolina, diésel, eléctrico).
Sobrescribe el método informacion() en la clase Coche para incluir el tipo de combustible al mostrar la información.
Ejercicio N° 3: Sistema de Gestión de Productos

Imagina que estás desarrollando un sistema de gestión de productos para una tienda en línea. Tu tarea es implementar un sistema que permita gestionar la información de los productos y realizar ciertas operaciones sobre ellos.

Crea una clase llamada Producto que tenga los siguientes atributos:
nombre: una cadena que representa el nombre del producto.
categoria: una cadena que indica la categoría del producto.
precio: un número decimal que indica el precio del producto.
en_stock: un valor booleano que indica si el producto está en stock.
La clase Producto debe tener los siguientes métodos:
informacion(): muestra por pantalla la información del producto, incluyendo el nombre, categoría y precio.
vender(): cambia el estado del producto a no en stock.
reponer(): cambia el estado del producto a en stock.
Crea una clase derivada llamada ProductoElectronico que herede de la clase Producto. La clase ProductoElectronico tiene un atributo adicional:
garantia: un número entero que indica los meses de garantía del producto electrónico.
Sobrescribe el método informacion() en la clase ProductoElectronico para incluir los meses de garantía al mostrar la información.
Ejercicio N° 4: Sistema de Gestión de Cursos

Imagina que estás desarrollando un sistema de gestión de cursos para una plataforma educativa en línea. Tu tarea es implementar un sistema que permita gestionar la información de los cursos y realizar ciertas operaciones sobre ellos.

Crea una clase llamada Curso que tenga los siguientes atributos:
titulo: una cadena que representa el título del curso.
instructor: una cadena que indica el nombre del instructor del curso.
precio: un número decimal que indica el precio del curso.
disponible: un valor booleano que indica si el curso está disponible para inscripción.
La clase Curso debe tener los siguientes métodos:
informacion(): muestra por pantalla la información del curso, incluyendo el título, instructor y precio.
abrir_inscripciones(): cambia el estado del curso a disponible.
cerrar_inscripciones(): cambia el estado del curso a no disponible.
Crea una clase derivada llamada CursoOnline que herede de la clase Curso. La clase CursoOnline tiene un atributo adicional:
duracion: un número entero que indica la duración del curso en semanas.
Sobrescribe el método informacion() en la clase CursoOnline para incluir la duración al mostrar la información.
