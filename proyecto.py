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
        for ev in self.__evaluaciones:
            if ev.get_titulo().lower() == evaluacion.get_titulo().lower():
                print(f"Ya existe una evaluación con el título '{evaluacion.get_titulo()}'.")
                return False
        self.__evaluaciones.append(evaluacion)
        return True
    
    def eliminar_evaluacion(self, titulo):
        for ev in self.__evaluaciones:
            if ev.get_titulo().lower() == titulo.lower():
                self.__evaluaciones.remove(ev)
                print(f"Evaluacion '{titulo}' eliminada con éxito.")
                return True
        print(f"No se encontró una evaluación con el título '{titulo}'.")
        return False

    def esta_inscrito(self, id_estudiante): #control de duplicados, si ya esta esta estudiante en la lista
        for est in self.__estudiantes:
            if est.get_id() == id_estudiante:
                return True
        return False 
    
    def consultar_evaluaciones(self):
        if not self.__evaluaciones:
            print("No hay evaluaciones para este curso.")
            return
        print(f"\nEvaluaciones del curso {self.__nombre} (Sección {self.__codigo}):")
        for ev in self.__evaluaciones:
            print(f"- {ev}")

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
        print(f"Se creo evaluacion: {self.__titulo}")

    def __str__(self):
        return f"{self.__tipo}: {self.__titulo}"
    
    def asignar_calificacion(self, id_estudiante, nota):
        self.__calificaciones[id_estudiante] = nota
        print(f"Calificacion asignada a estudiante {id_estudiante} -> {nota}")

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_tipo(self):
        return self.__tipo

    def get_calificaciones(self):
        return self.__calificaciones.copy()

    def __del__(self):
        print(f"Se elimino evaluacion: {self.__titulo}")


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
        
        if seccion in self.__cursos:  #Evitar duplicados 2.0
            print("Ya existe un curso con esa sección.")
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

    def consultar_evaluaciones(self):
        seccion = input("Ingrese la seccion del curso: ")
        if seccion not in self.__cursos:
            print("Curso no encontrado.")
            return

        curso = self.__cursos[seccion]
        curso.consultar_evaluaciones()

    def consultar_calificaciones(self):
        seccion = input("Ingrese la sección del curso: ")
        if seccion not in self.__cursos:
            print("Curso no encontrado.")
            return
        
        curso = self.__cursos[seccion]
        evaluaciones = curso.get_evaluaciones()
        if not evaluaciones:
            print("No hay evaluaciones registradas en este curso.")
            return

        print("\nEvaluaciones disponibles:")
        for i, ev in enumerate(evaluaciones, start=1):
            print(f"{i}. {ev}")

        try:
            opcion = int(input("Seleccione el número de la evaluación: "))
            if opcion < 1 or opcion > len(evaluaciones):
                print("Opción inválida.")
                return
        except ValueError:
            print("Entrada inválida.")
            return

        evaluacion = evaluaciones[opcion - 1]
        calificaciones = evaluacion.get_calificaciones()

        if not calificaciones:
            print("No hay calificaciones registradas en esta evaluación.")
            return

        print(f"\nCalificaciones para {evaluacion.get_titulo()} ({evaluacion.get_tipo()}):")
        for id_est, nota in calificaciones.items():
            estudiante = self.__usuarios.get(id_est)
            nombre = estudiante.get_nombre() if estudiante else "Desconocido"
            print(f"- {nombre} (ID: {id_est}) -> {nota}")
    
    def menu_consultas(self):
        acciones = {
            "1": self.consultar_cursos,
            "2": self.consultar_usuarios,
            "3": self.consultar_estudiantes_por_curso,
            "4": self.consultar_evaluaciones,
            "5": self.consultar_calificaciones
        }
        while True:
            print("\nMenu de consultas")
            print("1. Consultar cursos")
            print("2. Consultar usuarios")
            print("3. Consultar estudiantes por curso")
            print("4. Consultar evaluaciones por curso")
            print("5. Consultar calificacion")
            print("0. Volver")
            opcion = input("Seleccione una opción: ")

            if opcion == "0":
                break
            elif opcion in acciones:
                acciones[opcion]()  #puntero a función
            else:
                print("Opcion invalida.")

#-------------------------------------------------------------
    def crear_evaluacion(self):
        seccion = input("Ingrese la seccion del curso: ")
        if seccion not in self.__cursos:
            print("Curso no encontrado.")
            return

        curso = self.__cursos[seccion]
        titulo = input("Ingrese el titulo de la evaluacion: ")
        tipo = input("Ingrese el tipo de evaluación (examen, tarea, etc.): ")

        evaluacion = Evaluacion(titulo, tipo)
        if curso.agregar_evaluacion(evaluacion):
            print("Evaluación creada exitosamente.")

    def eliminar_evaluacion(self):
        seccion = input("Ingrese la sección del curso: ")
        if seccion not in self.__cursos:
            print("Curso no existe.")
            return

        curso = self.__cursos[seccion]
        titulo = input("Cual es el titulo de la evaluacion a eliminar: ")
        curso.eliminar_evaluacion(titulo)
  
    def registrar_calificacion(self):
        seccion = input("Ingrese la sección del curso: ")
        if seccion not in self.__cursos:
            print("Curso no encontrado.")
            return
        
        curso = self.__cursos[seccion]
        evaluaciones = curso.get_evaluaciones()
        if not evaluaciones:
            print("No hay evaluaciones registradas en este curso.")
            return

        print("\nEvaluaciones disponibles:")
        for i, ev in enumerate(evaluaciones, start=1):
            print(f"{i}. {ev}")
        
        try:
            opcion = int(input("Seleccione el número de la evaluación: "))
            if opcion < 1 or opcion > len(evaluaciones):
                print("Opción inválida.")
                return
        except ValueError:
            print("Entrada inválida.")
            return

        evaluacion = evaluaciones[opcion - 1]

        id_estudiante = input("Ingrese el ID del estudiante: ")
        if id_estudiante not in self.__usuarios or not isinstance(self.__usuarios[id_estudiante], Estudiante):
            print("Estudiante no válido.")
            return

        if not curso.esta_inscrito(id_estudiante):
            print("El estudiante no está inscrito en este curso.")
            return

        try:
            nota = float(input("Ingrese la calificación: "))
        except ValueError:
            print("La calificación debe ser un número.")
            return

        evaluacion.asignar_calificacion(id_estudiante, nota)


    def menu_evaluaciones(self):
        acciones = {
            "1": self.crear_evaluacion,
            "2": self.eliminar_evaluacion,
            "3": self.registrar_calificacion
        }
        while True:
            print("\nAdministrador de evaluaciones")
            print("1. Crear evaluación")
            print("2. Eliminar evaluacion")
            print("3. Registrar calificacion a evaluacion")
            print("0. Volver")
            opcion = input("Seleccione una opción: ")

            if opcion == "0":
                break
            elif opcion in acciones:
                acciones[opcion]()  # puntero a función
            else:
                print("Opción inválida.")
#---------------------------------------------------------
    def reporte_promedio_por_estudiante(self):
        codigo = input("Ingrese el código/sección del curso: ")
        if codigo not in self.__cursos:
            print("Curso no encontrado.")
            return

        curso = self.__cursos[codigo]
        estudiantes = curso.get_estudiantes()
        evaluaciones = curso.get_evaluaciones()

        if not estudiantes:
            print("No hay estudiantes inscritos en este curso.")
            return
        if not evaluaciones:
            print("No hay evaluaciones en este curso.")
            return

        print(f"\nPromedio por estudiante en {curso.get_nombre()} ({curso.get_codigo()})")
        for est in estudiantes:
            suma = 0
            conteo = 0
            for ev in evaluaciones:
                calificaciones = ev.get_calificaciones()
                if est.get_id() in calificaciones:
                    suma += calificaciones[est.get_id()]
                    conteo += 1
            if conteo > 0:
                promedio = suma / conteo
                print(f"{est.get_nombre()} (ID: {est.get_id()}): {promedio:.2f}")
            else:
                print(f"{est.get_nombre()} (ID: {est.get_id()}): Sin calificaciones registradas")

    def reporte_promedio_curso(self):
        codigo = input("Ingrese la seccion del curso: ")
        if codigo not in self.__cursos:
            print("Curso no encontrado.")
            return

        curso = self.__cursos[codigo]
        evaluaciones = curso.get_evaluaciones()

        if not evaluaciones:
            print("No hay evaluaciones en este curso.")
            return

        suma_total = 0
        conteo_total = 0

        for ev in evaluaciones:
            for nota in ev.get_calificaciones().values():
                suma_total += nota
                conteo_total += 1

        if conteo_total == 0:
            print("No hay calificaciones registradas en este curso.")
            return

        promedio_curso = suma_total / conteo_total
        print(f"\nPromedio general del curso {curso.get_nombre()} ({curso.get_codigo()}): {promedio_curso:.2f}")
    
    def reporte_top_estudiantes(self):
        codigo = input("Ingrese el código/sección del curso: ")
        if codigo not in self.__cursos:
            print("Curso no encontrado.")
            return
            
        curso = self.__cursos[codigo]
        estudiantes = curso.get_estudiantes()
        evaluaciones = curso.get_evaluaciones()
        
        if not estudiantes or not evaluaciones:
            print("No hay estudiantes o evaluaciones en este curso.")
            return
                
        promedios = {}
        for est in estudiantes:
            suma, conteo = 0, 0
            for ev in evaluaciones:
                calificaciones = ev.get_calificaciones()
                if est.get_id() in calificaciones:
                    suma += calificaciones[est.get_id()]
                    conteo += 1
            if conteo > 0:
                promedios[est] = suma / conteo
                
        if not promedios:
            print("No hay calificaciones registradas.")
            return
        
        top = []
        promedios_items = list(promedios.items())
        while len(top) < 3 and promedios_items:
            max_est = promedios_items[0]
            for item in promedios_items:
                if item[1] > max_est[1]:
                    max_est = item
            top.append(max_est)
            promedios_items.remove(max_est)
            
        print(f"\nTop 3 estudiantes estrellitas en {curso.get_nombre()} ")
        for est, prom in top:
            print(f"{est.get_nombre()} (ID: {est.get_id()}): {prom:.2f}")



    def menu_reportes(self):
        acciones = {
            "1": self.reporte_promedio_por_estudiante,
            "2": self.reporte_promedio_curso,
            "3": self.reporte_top_estudiantes
        }
        while True:
            print("\nMenú de reportes")
            print("1. Promedio por estudiante")
            print("2. Promedio general del curso")
            print("3. Mejores 3 estudiantes por curso")
            print("0. Volver")
            opcion = input("Seleccione una opción: ")

            if opcion == "0":
                break
            elif opcion in acciones:
                acciones[opcion]()  # puntero a función
            else:
                print("Opción invalida.")

#---------------------------------------------------------
    def __del__(self):
        print("Apagando... Aqui ya no me quedo")

#---------------------------------------------------------

def main():
    menu = SistemaColegio()

    acciones = {
        "1": menu.registrar_usuario,
        "2": menu.menu_cursos,
        "3": menu.inscribir_estudiante_curso,
        "4": menu.menu_consultas,
        "5": menu.menu_evaluaciones,
        "6": menu.menu_reportes
    }

    while True:
        print("\nEliga una de las siguientes opciones: ")
        print("1. Registrar usuarios")
        print("2. Administrar cursos")
        print("3. Inscribir estudiante al curso")
        print("4. Consultas de informacion")
        print("5. Administrar evaluaciones")
        print("6. Reportes de notas")
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