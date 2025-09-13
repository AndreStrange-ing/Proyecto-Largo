from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, id_usuario):
        # Encapsulamiento, atributos privados
        self.__nombre = nombre
        self.__id_usuario = id_usuario
        print(f"Usuario creado: {self.__nombre}")

    @abstractmethod
    def mostrar_info(self):
        # Polimorfismo, se implementará distinto en cada subclase
        pass

    # Getters y setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_id(self):
        return self.__id_usuario

    def __del__(self):
        print(f"Usuario eliminado: {self.__nombre}")


class Estudiante(Usuario):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre, id_usuario) 
        self._cursos = []  # Encapsulamiento
        print(f"Estudiante registrado: {self._nombre}")

    def mostrar_info(self):
        # Polimorfismo
        return f"Estudiante: {self._nombre} (ID: {self._id_usuario})"

    def inscribir_curso(self, curso):
        self._cursos.append(curso)

    def __del__(self):
        print(f"Estudiante eliminado: {self._nombre}")

class Catedratico(Usuario):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre, id_usuario)  # Constructor padre
        self._cursos_daods = []  # Encapsulamiento
        print(f"Catedratico registrado: {self._nombre}")

    def mostrar_info(self):
        # Polimorfismo
        return f"Catedratico: {self._nombre} (ID: {self._id_usuario})"

    def asignar_curso(self, curso):
        self._cursos_daods.append(curso)

    def __del__(self):
        print(f"Catedratico eliminado: {self._nombre}")

class Curso:
    def __init__(self, nombre, codigo, catedratico):
        self._nombre = nombre
        self._codigo = codigo
        self._catedratico = catedratico
        self._estudiantes = []
        self._evaluaciones = []
        print(f"Curso creado: {self._nombre}")

    def __str__(self):
        return f"Curso: {self._nombre} ({self._codigo}) - Catedratico: {self._catedratico.get_nombre()}"

    def __del__(self):
        print(f"Curso eliminado: {self._nombre}")

class Evaluacion:
    def __init__(self, titulo, tipo):
        self._titulo = titulo
        self._tipo = tipo
        self._calificaciones = {} 
        print(f"Evaluación creada: {self._titulo}")

    def __str__(self):
        return f"{self._tipo}: {self._titulo}"

    def __del__(self):
        print(f"Evaluación eliminada: {self._titulo}")

class Sistema_Colegio:
    def __init__(self):
        self._usuarios = {}  # Encapsulamiento
        self._cursos = {}
        print("Bienvenido al sistema del colegio 'Aqui me Quedo' ")

    def crear_curso(self):
        nombre = input("Ingrese el nombre del curso: ")
        codigo = input("Ingrese el código del curso: ")
        id_catedratico = input("ID del catedratico: ")

        if id_catedratico not in self._usuarios or not isinstance(self._usuarios[id_catedratico], Catedratico):
            print("Catedratico no válido.")
            return

        catedratico = self._usuarios[id_catedratico]
        curso = Curso(nombre, codigo, catedratico)
        self._cursos[codigo] = curso
        catedratico.asignar_curso(curso)
        print("Curso creado con exito.")

    def registrar_usuario(self):
        tipo = input("Seleccione '1' para registrar a un estudiante o '2' para un categratico: ")
        nombre = input("Nombre: ")
        id_usuario = input("ID unico: ")

        if id_usuario in self._usuarios:
            print("El ID ya esta registrado.")
            return

        if tipo == "1":
            self._usuarios[id_usuario] = Estudiante(nombre, id_usuario)
        elif tipo == "2":
            self._usuarios[id_usuario] = Catedratico(nombre, id_usuario)
        else:
            print("Opción invalida.")
            return

        print("Usuario registrado con exito.")

    def consultar_cursos(self):
        if not self._cursos:
            print("No hay cursos registrados.")
            return
        for curso in self._cursos.values():
            print(curso)

    def __del__(self):
        print("Apagando... Aqui ya no me quedo")

def main():
    sistema = Sistema_Colegio()

    acciones = {
        "1": sistema.crear_curso,
        "2": sistema.registrar_usuario,
        "3": sistema.consultar_cursos,
        "0": exit
    }

    while True:
        print("\nEliga una de las siguientes opciones: ")
        print("1. Crear curso")
        print("2. Registrar usuario")
        print("3. Consultar cursos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        accion = acciones.get(opcion)

        if accion:
            accion()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()