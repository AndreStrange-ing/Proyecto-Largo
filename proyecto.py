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

    def esta_inscrito(self, codigo_curso): #verificacion de duplicados
        for curso in self.__cursos:
            if curso.get_codigo() == codigo_curso:
                return True
        return False
    
    def inscribir_curso(self, curso): #true si se agrego false si ya esta inscrito
        if self.esta_inscrito(curso.get_codigo()):
            return False
        self.__cursos.append(curso)
        return True

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
        return f"Curso: {self.__nombre} - Seccion: ({self.__codigo}) - Catedratico: {self.__catedratico.get_nombre()}"
    #Metodos controlados para encapsulamiento y control de duplicados
    def inscribir_estudiante(self, estudiante):
        if self.esta_inscrito(estudiante.get_id()):
            return False
        self.__estudiantes.append(estudiante)
        return True

    def agregar_evaluacion(self, evaluacion):
        self.__evaluaciones.append(evaluacion)

    def esta_inscrito(self, id_estudiante): #control de duplicados, si ya esta esta estudiante en la lista
        for est in self.__estudiantes:
            if est.get_id() == id_estudiante:
                return True
        return False 

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
        self.__calificaciones = {} 
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
#------------------------------------------------------------
    def crear_curso(self):
        nombre = input("Ingrese el nombre del curso: ")
        seccion = input("Ingrese la seccion del curso: ")
        id_catedratico = input("ID del catedratico: ")

        if id_catedratico not in self.__usuarios or not isinstance(self.__usuarios[id_catedratico], Catedratico):
            print("Catedratico no válido.")
            return

        catedratico = self.__usuarios[id_catedratico]
        curso = Curso(nombre, seccion, catedratico)
        self.__cursos[seccion] = curso
        catedratico.asignar_curso(curso)
        print("Curso creado con exito.")

    def eliminar_curso(self):
        seccion = input("Ingrese la sección del curso a eliminar: ")
        if seccion not in self.__cursos:
            print("Curso no encontrado.")
            return
        del self.__cursos[seccion]
        print("Curso eliminado con éxito.")

    def menu_cursos(self):
        acciones = {
            "1": self.crear_curso,
            "2": self.eliminar_curso,
        }
        while True:
            print("\nAdministrador de cursos")
            print("1. Crear curso")
            print("2. Eliminar curso")
            print("0. Volver")
            opcion = input("Seleccione una opción: ")

            if opcion == "0":
                break
            elif opcion in acciones:
                acciones[opcion]()  #puntero a función
            else:
                print("Opción inválida.")
#------------------------------------------------------------------
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
#---------------------------------------------------------

    def inscribir_estudiante_curso(self):
        id_estudiante = input("Ingrese el ID del estudiante para su inscripcion: ")

        # Validar existencia y tipo
        if id_estudiante not in self.__usuarios or not isinstance(self.__usuarios[id_estudiante], Estudiante):
            print("ID de estudiante no válido.")
            return

        seccion = input("Ingrese la sección del curso: ").strip()
        # Validar curso
        if seccion not in self.__cursos:
            print("Sección de curso no válida.")
            return

        estudiante = self.__usuarios[id_estudiante]
        curso = self.__cursos[seccion]

        # Verificar duplicado antes de intentar inscribir
        if estudiante.esta_inscrito(curso.get_codigo()) or curso.esta_inscrito(estudiante.get_id()):
            print(f"El estudiante {estudiante.get_nombre()} (ID: {estudiante.get_id()}) ya está inscrito en {curso.get_nombre()} (Sección {curso.get_codigo()}).")
            return
    
        # Inscribir estudiante en ambos lados
        agregado_est = estudiante.inscribir_curso(curso)
        agregado_cur = curso.inscribir_estudiante(estudiante)

        if agregado_est and agregado_cur:
            print(f"Estudiante {estudiante.get_nombre()} (ID: {estudiante.get_id()}) inscrito en {curso.get_nombre()} (Sección {curso.get_codigo()}) exitosamente.")
        else:
            print("no se pudo completar la inscripción.")
#--------------------------------------------------
    def consultar_cursos(self):
        if not self.__cursos:
            print("No hay cursos registrados.")
            return
        for curso in self.__cursos.values():
            print(curso)

    def consultar_usuarios(self):
        if not self.__usuarios:
            print("No hay usuarios registrados.")
            return
        for usuario in self.__usuarios.values():
            print(usuario.mostrar_info())

    def consultar_estudiantes_por_curso(self):
        seccion = input("Ingrese la sección del curso: ")
        if seccion not in self.__cursos:
            print("Curso no encontrado.")
            return
        curso = self.__cursos[seccion]
        estudiantes = curso.get_estudiantes()
        if not estudiantes:
            print("No hay estudiantes inscritos en este curso.")
        else:
            for est in estudiantes:
                print(est.mostrar_info())
    
    def menu_consultas(self):
        acciones = {
            "1": self.consultar_cursos,
            "2": self.consultar_usuarios,
            "3": self.consultar_estudiantes_por_curso,
        }
        while True:
            print("\nMenu de consultas")
            print("1. Consultar cursos")
            print("2. Consultar usuarios")
            print("3. Consultar estudiantes por curso")
            print("0. Volver")
            opcion = input("Seleccione una opción: ")

            if opcion == "0":
                break
            elif opcion in acciones:
                acciones[opcion]()  #puntero a función
            else:
                print("Opcion invalida.")

#-----------------------------------------
  
    def __del__(self):
        print("Apagando... Aqui ya no me quedo")

def main():
    menu = SistemaColegio()

    acciones = {
        "1": menu.registrar_usuario,
        "2": menu.menu_cursos,
        "3": menu.inscribir_estudiante_curso,
        "4": menu.menu_consultas,
    }

    while True:
        print("\nEliga una de las siguientes opciones: ")
        print("1. Registrar usuarios")
        print("2. Administrar cursos")
        print("3. Inscribir estudiante al curso")
        print("4. Consultas de informacion")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "0":
            break
        elif opcion in acciones:
            acciones[opcion]()  
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()