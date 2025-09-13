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


