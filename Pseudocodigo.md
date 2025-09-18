Pseudocodigo y principales funciones del sistema

Función InscribirEstudiante(nombre, id_estudiante, curso)
    Si estudiante ya existe en la lista de estudiantes
        Mostrar "El estudiante ya está inscrito"
        Retornar
    FinSi

    Crear nuevoEstudiante con nombre, id_estudiante, curso
    Agregar nuevoEstudiante a listaEstudiantes

    Mostrar "Estudiante inscrito exitosamente"
FinFunción


Función CrearEvaluacion(nombre_evaluacion, curso, fecha, peso)
    Si curso no existe en listaCursos
        Mostrar "El curso no existe"
        Retornar
    FinSi

    Crear nuevaEvaluacion con nombre_evaluacion, curso, fecha, peso
    Agregar nuevaEvaluacion a listaEvaluaciones

    Mostrar "Evaluación creada exitosamente"
FinFunción


Función RegistrarCalificacion(id_estudiante, nombre_evaluacion, calificacion)
    Si estudiante no existe en listaEstudiantes
        Mostrar "Estudiante no encontrado"
        Retornar
    FinSi

    Si evaluacion no existe en listaEvaluaciones
        Mostrar "Evaluación no encontrada"
        Retornar
    FinSi

    Si calificacion < 0 o calificacion > 100
        Mostrar "Calificación inválida"
        Retornar
    FinSi

    Registrar calificacion en el registro del estudiante para la evaluación
    Mostrar "Calificación registrada correctamente"
FinFunción

