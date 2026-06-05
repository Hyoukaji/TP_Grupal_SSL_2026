# TP_Grupal_SSL_2026
Trabajo Grupal para Sintaxis y Semántica de los Lenguajes, primer cuatrimestre del año 2026 

El script se hará en Python


El siguiente es el enunciado del trabajo:

2) Propuesta de Enunciado: Sistema de Gestión de Trabajos de
Impresión
Consigna: Desarrollar una aplicación de consola para un centro de impresión que
gestione la cola de trabajos enviados por los usuarios. Cada trabajo de impresión deberá
registrar los siguientes datos: ID de Trabajo (Job ID), Nombre del Documento, Tipo
de Formato (ej: PDF, Imagen, Texto), Cantidad de Páginas, Nivel de Prioridad, y
Fecha y Hora de envío. El sistema debe presentar un menú interactivo con las
siguientes operaciones:
1. Recepción de Documentos:
Implementar la función para agregar nuevos trabajos a la cola, respetando estrictamente
el orden de llegada. Se deberán ingresar todos los datos: ID, nombre, formato, páginas,
prioridad, fecha y hora de envío.
2. Cambio de Prioridad Individual:
Permitir la actualización del nivel de prioridad de un trabajo específico (por ejemplo, si
un cliente paga un servicio "Express"), identificándolo mediante su ID de Trabajo.
3. Procesar Impresión (Atención de la Cola):
Implementar la opción para retirar de la cola el trabajo que se encuentra al frente (el
primero en llegar), simulando que la impresora ha comenzado a procesarlo.
4. Visualización de la Cola de Impresión:
Diseñar una función que muestre todos los trabajos pendientes en la cola, desplegando
de manera ordenada y clara cada uno de sus atributos.
Sintaxis y Semántica del Lenguaje – 2026 3
5. Reajuste Masivo por Fecha:
Dado un mes ingresado por el usuario, actualizar la prioridad a "Baja" para todos los
trabajos cuya fecha de envío corresponda a ese mes (útil para tareas de mantenimiento
sobre archivos viejos que quedaron en cola).
6. Filtrado por Formato y Franja Horaria:
 a) Cancelación por Formato: Eliminar de la cola todos los trabajos cuyo Tipo
de Formato coincida con el valor ingresado por el usuario (ej: eliminar todos
los archivos "Imagen" por falta de tinta a color).
 b) Generación de Sub-Cola Horaria: Crear una nueva Cola con los trabajos
cuya hora de envío se encuentre dentro de un intervalo definido por el usuario
(ej: trabajos enviados en el turno mañana), e imprimir su contenido
automáticamente.