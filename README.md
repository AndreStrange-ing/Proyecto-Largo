Sistema de Gestión de Colegio "Aquí me Quedo"

Descripción
Este sistema permite gestionar un colegio de manera sencilla, incluyendo:

- Registro y administración de usuarios (Estudiantes y       Catedráticos).

- Gestión de cursos y evaluaciones.

- Inscripción de estudiantes en cursos.

- Registro y consulta de calificaciones.

- Generación de reportes de notas, incluyendo promedio y top de estudiantes.

--------------------------------------------------------------

Requisitos

- Python 3.8 o superior.

- No requiere librerías externas.

--------------------------------------------------------------

Instrucciones de Uso
Ejecución

Ejecuta el archivo principal:
python nombre_del_archivo.py

Eliga una de las siguientes opciones:
1. Registrar usuarios
2. Administrar cursos
3. Inscribir estudiante al curso
4. Consultas de informacion
5. Administrar evaluaciones
6. Reportes de notas
0. Salir

--------------------------------------------------------------

Menús y Funcionalidades
1. Registrar usuarios
Esta es la funcion principal y de la cual depende todo el sistema

Permite registrar:

Estudiantes → ID único y nombre.

Catedráticos → ID único y nombre.

El sistema evita IDs duplicados.

2️. Administrar cursos

Opciones:

1. Crear curso

Nombre del curso.

Sección (ID único de curso).

ID del catedrático responsable.

Evita duplicar secciones.

Eliminar curso

Ingresa la sección del curso a eliminar.

3️. Inscribir estudiante al curso

Se requiere ID del estudiante y sección del curso.

El sistema verifica duplicados.

Inscripción bidireccional: estudiante → curso y curso → estudiante.

4️. Consultas de información

Opciones:

Consultar cursos → Muestra todos los cursos y catedráticos.

Consultar usuarios → Lista todos los estudiantes y catedráticos registrados.

Consultar estudiantes por curso → Muestra los estudiantes inscritos en un curso específico.

Consultar evaluaciones por curso → Lista todas las evaluaciones de un curso.

Consultar calificación → Permite seleccionar una evaluación y ver las calificaciones registradas.

5️. Administrar evaluaciones

Opciones:

Crear evaluación

Selecciona la sección del curso.

Ingresa título y tipo de evaluación (examen, tarea, etc.).

Evita títulos duplicados dentro del mismo curso.

Eliminar evaluación

Selecciona la sección del curso.

Ingresa el título de la evaluación a eliminar.

Registrar calificación

Selecciona el curso y la evaluación.

Ingresa ID del estudiante y calificación (0-100).

El sistema verifica que el estudiante esté inscrito.

6️. Reportes de notas

Opciones:

Promedio por estudiante → Muestra el promedio de cada estudiante en un curso.

Promedio general del curso → Muestra el promedio total de todos los estudiantes en un curso.

Mejores 3 estudiantes por curso → Muestra los 3 estudiantes con mejor promedio.

Nota: Puedes ampliar con otros reportes, por ejemplo, calificaciones bajas por umbral.

--------------------------------------------------------------

Características Técnicas

Encapsulamiento: todos los atributos privados están protegidos.

Polimorfismo: método mostrar_info() implementado diferente para estudiantes y catedráticos.

Control de duplicados: IDs, secciones de cursos y títulos de evaluaciones son únicos.

Reportes y estadísticas: promedio por estudiante, promedio general del curso y top 3 estudiantes.

--------------------------------------------------------------

Ejemplo de Uso

1. Registrar catedrático y estudiantes.
2. Crear un curso y asignarle un catedrático.
3. Inscribir estudiantes en el curso.
4. Crear evaluaciones y registrar calificaciones.
5. Consultar calificaciones o generar reportes de promedios y top estudiantes.

------------------------------------

Autor

Sistema desarrollado por Andre Herrera a.k.a AndreStrange.