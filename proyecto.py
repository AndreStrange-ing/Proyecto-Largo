from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, id_usuario):
        # Encapsulamiento, atributos protegidos
        self._nombre = nombre
        self._id_usuario = id_usuario
        print(f"Usuario creado: {self._nombre}")

    @abstractmethod
    def mostrar_info(self):
        # Polimorfismo, se implementará distinto en cada subclase
        pass

    # Getter y Setter para encapsulamiento
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_id(self):
        return self._id_usuario

    def __del__(self):
        print(f"Usuario eliminado: {self._nombre}")


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