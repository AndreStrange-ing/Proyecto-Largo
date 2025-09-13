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
        self.__cursos = []  # Atributo privado
        print(f"Estudiante registrado: {self.get_nombre()}")

    def mostrar_info(self):
        # Polimorfismo
        return f"Estudiante: {self.get_nombre()} (ID: {self.get_id()})"

    def inscribir_curso(self, curso):
        self.__cursos.append(curso)

    def get_cursos(self):
        return self.__cursos[:]  # Devolvemos copia segura

    def __del__(self):
        print(f"Estudiante eliminado: {self.get_nombre()}")


class Catedratico(Usuario):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre, id_usuario)
        self.__cursos_dictados = []  # Atributo privado
        print(f"Catedratico registrado: {self.get_nombre()}")

    def mostrar_info(self):
        # Polimorfismo
        return f"Catedratico: {self.get_nombre()} (ID: {self.get_id()})"

    def asignar_curso(self, curso):
        self.__cursos_dictados.append(curso)

    def get_cursos_dictados(self):
        return self.__cursos_dictados[:]

    def __del__(self):
        print(f"Catedratico eliminado: {self.get_nombre()}")


class Curso:
    def __init__(self, nombre, codigo, catedratico):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__catedratico = catedratico
        self.__estudiantes = []
        self.__evaluaciones = []
        print(f"Curso creado: {self.__nombre}")

    def __str__(self):
        return f"Curso: {self.__nombre} ({self.__codigo}) - Catedratico: {self.__catedratico.get_nombre()}"

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_codigo(self):
        return self.__codigo

    def get_catedratico(self):
        return self.__catedratico

    def get_estudiantes(self):
        return self.__estudiantes[:]

    def get_evaluaciones(self):
        return self.__evaluaciones[:]

    def __del__(self):
        print(f"Curso eliminado: {self.__nombre}")

class Evaluacion:
    def __init__(self, titulo, tipo):
        self.__titulo = titulo
        self.__tipo = tipo
        self.__calificaciones = {}  # {id_estudiante: nota}
        print(f"Evaluación creada: {self.__titulo}")

    def __str__(self):
        return f"{self.__tipo}: {self.__titulo}"

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_tipo(self):
        return self.__tipo

    def get_calificaciones(self):
        return self.__calificaciones.copy()

    def __del__(self):
        print(f"Evaluación eliminada: {self.__titulo}")


class SistemaColegio:
    def __init__(self):
        self.__usuarios = {}  # Atributo privado
        self.__cursos = {}
        print("Bienvenido al sistema del colegio 'Aqui me Quedo' ")

    def crear_curso(self):
        nombre = input("Ingrese el nombre del curso: ")
        codigo = input("Ingrese el código del curso: ")
        id_catedratico = input("ID del catedratico: ")

        if id_catedratico not in self.__usuarios or not isinstance(self.__usuarios[id_catedratico], Catedratico):
            print("Catedratico no válido.")
            return

        catedratico = self.__usuarios[id_catedratico]
        curso = Curso(nombre, codigo, catedratico)
        self.__cursos[codigo] = curso
        catedratico.asignar_curso(curso)
        print("Curso creado con exito.")

    def registrar_usuario(self):
        tipo = input("Seleccione '1' para registrar a un estudiante o '2' para un catedratico: ")
        nombre = input("Nombre: ")
        id_usuario = input("ID unico: ")

        if id_usuario in self.__usuarios:
            print("El ID ya esta registrado.")
            return

        if tipo == "1":
            self.__usuarios[id_usuario] = Estudiante(nombre, id_usuario)
        elif tipo == "2":
            self.__usuarios[id_usuario] = Catedratico(nombre, id_usuario)
        else:
            print("Opción invalida.")
            return

        print("Usuario registrado con exito.")

    def consultar_cursos(self):
        if not self.__cursos:
            print("No hay cursos registrados.")
            return
        for curso in self.__cursos.values():
            print(curso)

    # Getters
    def get_usuarios(self):
        return self.__usuarios.copy()

    def get_cursos(self):
        return self.__cursos.copy()

    def __del__(self):
        print("Apagando... Aqui ya no me quedo")

def main():
    sistema = SistemaColegio()

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