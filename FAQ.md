Reflexión del Proyecto POO - Gestión Académica

1. Decisiones de diseño tomadas

Durante el desarrollo del proyecto, se optó por un diseño orientado a objetos con clases bien definidas para representar Usuarios, Estudiantes, Cursos y Evaluaciones. Esto permitió encapsular datos y comportamientos, facilitando la reutilización y el mantenimiento del código.

Se decidió usar métodos y propiedades privadas para proteger los datos sensibles, como el ID del estudiante y las calificaciones, y exponer únicamente métodos seguros para interactuar con ellos.

---

2. Herencia, polimorfismo, encapsulamiento y abstracción

- Herencia:Se creó una clase base Usuario y clases derivadas como Estudiante y Profesor. Esto permitió que las subclases compartieran atributos y métodos comunes sin duplicación de código.  
- Polimorfismo:Se definieron métodos abstractos en la clase base que las subclases implementan según sus necesidades, por ejemplo, mostrar_informacion(). Esto permitió tratar diferentes tipos de usuario de forma uniforme, aumentando la flexibilidad.
- Encapsulamiento:Se definieron atributos privados y métodos públicos para controlar el acceso a la información sensible, como el ID del estudiante o las calificaciones, protegiendo la integridad de los datos.
- Abstracción: Se diseñaron clases y métodos que representan conceptos generales (como `Usuario` o `Evaluacion`) dejando detalles específicos para las subclases. Esto facilita la extensión del sistema sin afectar su estructura principal.

Ventajas obtenidas:
- Menor duplicación de código.
- Código más legible y mantenible.
- Mayor seguridad y control sobre los datos.
- Facilidad para agregar nuevos tipos de usuario y funcionalidades sin modificar código existente.


---

3. Estructuras de datos utilizadas

Las principales estructuras de datos fueron:

- Listas:Para almacenar estudiantes, cursos y evaluaciones. Son dinámicas y fáciles de iterar.  
- Diccionarios:Para registrar calificaciones y permitir acceso rápido mediante ID del estudiante o nombre de la evaluación.  
- Listas anidadas: Para representar tableros de información o agrupamientos, como evaluaciones por curso.

¿Por qué fueron útiles? 
Estas estructuras permiten buscar, modificar y recorrer información de manera eficiente, y se adaptan al crecimiento del sistema sin complicaciones.

---

4. Errores comunes anticipados y controlados

- Conflictos al inscribir estudiantes duplicados: Se verificó si el estudiante ya existía antes de agregarlo.  
- Calificaciones inválidas: Se controló que las notas estén entre 0 y 100.  
- Errores de referencias en listas compartidas: Se evitó modificar directamente listas compartidas sin copiar cuando era necesario.  
- Conflictos de Git: Se usó git pull antes de hacer push para integrar cambios remotos y evitar sobrescribir información.

---

5. Organización del trabajo con Git y GitHub

- Se creó un repositorio remoto en GitHub para centralizar el proyecto.  
- Cada cambio importante se hizo en commits claros, con mensajes descriptivos como "Agregar pseudocódigo" o "Mejorar gestión de evaluaciones".  
- Se resolvieron conflictos mediante git pull y commits de merge, manteniendo la historia de cambios organizada.  
- Esto permitió trabajar de manera segura y conservar versiones anteriores del proyecto.

---

6. Mejoras futuras

Si tuviéra más tiempo, implementaría:

- Interfaz gráfica:Para facilitar la interacción con el sistema.  
- Persistencia en base de datos:Para almacenar estudiantes y calificaciones de manera permanente.  
- Reportes automáticos: Para calcular promedios y generar certificados.  
- Control de usuarios con roles y permisos más avanzados.

---

7. Dificultades encontradas y soluciones

- Merge incompleto en Git: Aprendimos a concluir merges antes de hacer pull o push.  
- Confusión con listas compartidas: Se resolvió usando copias cuando se necesitaba modificar datos sin afectar el original.  
- Validaciones de entradas: Se implementaron múltiples comprobaciones para evitar errores en la inscripción de estudiantes o registro de calificaciones.  
- Gestión de la herencia y métodos abstractos: Se practicó con pequeñas pruebas antes de integrar todo, asegurando que las subclases implementaran correctamente los métodos requeridos.
