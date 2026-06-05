# =====================================================================
# SISTEMA DE GESTIÓN DE TRABAJOS DE IMPRESIÓN
# 
# Justificación de diseño: Se importan las primitivas de 'cola_tad' y 
# 'trabajo_tad' para garantizar el encapsulamiento. El programa principal 
# (main.py) NUNCA accede directamente a los índices de las estructuras, 
# interactuando exclusivamente a través de los selectores y modificadores, 
# respetando así la barrera de abstracción.
# =====================================================================

from tads.trabajo_tad import *
from tads.cola_tad import *
from datetime import datetime, time
from datos_prueba import cargarDatosEjemplo


# =====================================================================
# PUNTO 1: RECEPCIÓN DE DOCUMENTOS (OPCIÓN 1 DEL MENÚ)
# =====================================================================

def ingreso(cola_impresion):
    print("\nNUEVO TRABAJO DE IMPRESIÓN")

    # 1. Se crea una instancia vacía del TAD Trabajo para alojar los datos.
    trabajo = crearTrabajo()

    # 2. Se solicitan los datos al usuario por teclado.
    jobID = input("ID de Trabajo: ")
    nom = input("Nombre del Documento: ")
    fmt = input("Tipo de Formato (PDF/Imagen/Texto): ")
    pag = int(input("Cantidad de Páginas: "))
    pri = input("Nivel de Prioridad: ")
    fecha = datetime.now() 

    # 3. Se encapsulan los datos ingresados dentro de la estructura del TAD Trabajo.
    cargarTrabajo(trabajo, jobID, nom, fmt, pag, pri, fecha)

    # 4. Se inserta el trabajo al final de la cola principal, respetando 
    # el principio FIFO (First In, First Out / Primero en entrar, primero en salir).
    encolar(cola_impresion, trabajo)

    print("Trabajo agregado a la cola de impresión.")


# =====================================================================
# PUNTO 2: CAMBIO DE PRIORIDAD INDIVIDUAL (OPCIÓN 2 DEL MENÚ)
# =====================================================================

def cambiarPrioridad(cola_impresion):
    print("\n" + "="*40)
    print("   PROCESO: CAMBIO DE PRIORIDAD INDIVIDUAL")
    print("="*40 + "\n")
    
    # 1. Se verifica que haya elementos para procesar.
    if not esVacia(cola_impresion):
        jobID = input("-> Ingrese el ID del trabajo a modificar: ")
        nuevaPri = input("-> Ingrese la nueva prioridad: ")
        print("")
        
        # 2. Se instancian colas auxiliares para no perder los datos de la cola original durante la búsqueda.
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        
        # 3. Se hace una copia de seguridad de la cola principal en la primera auxiliar.
        copiarCola(cola_impresion, cola_aux)
        
        encontrado = False
        # 4. Se recorre la copia desencolando elemento por elemento.
        while not esVacia(cola_aux):
            trabajo_actual = desencolar(cola_aux)
            
            # 5. Se usa el selector (getter) 'verJobID' para comparar el ID actual con el buscado.
            if verJobID(trabajo_actual) == jobID:
                # 6. Si hay coincidencia, se usa el modificador (setter) para cambiar la prioridad.
                modPrioridad(trabajo_actual, nuevaPri)
                print("[OK] Prioridad del trabajo actualizada en el sistema.")
                encontrado = True
                
            # 7. Se guarda el elemento (modificado o no) en una segunda cola auxiliar para no perderlo.
            encolar(cola_aux2, trabajo_actual)
            
        # 8. Se reconstruye la primera cola auxiliar pasando los elementos de la segunda.
        while not esVacia(cola_aux2):
            encolar(cola_aux, desencolar(cola_aux2))
            
        # 9. Finalmente, se pisa la cola original con la cola auxiliar que ya contiene el dato actualizado.
        copiarCola(cola_aux, cola_impresion) 
        
        if not encontrado:
            print("[!] No se encontró ningún trabajo con el ID ingresado.")
    else:
        print("[!] La cola está vacía. No hay trabajos para modificar.")
    print("\n" + "="*40)


# =====================================================================
# PUNTO 3: PROCESAR IMPRESIÓN (OPCIÓN 3 DEL MENÚ)
# =====================================================================

def procesarImpresion(cola_impresion):
    print("\n" + "="*40)
    print("   ACCIÓN: PROCESAR PRÓXIMA IMPRESIÓN")
    print("="*40)
    
    # 1. Se verifica que la estructura no esté vacía para evitar errores en tiempo de ejecución (Underflow).
    if not esVacia(cola_impresion):
        # 2. Se extrae el elemento que está en el frente de la cola (el más antiguo).
        impresion = desencolar(cola_impresion)
        
        # 3. Se accede al nombre del documento extraído usando su selector.
        print(f"\n[IMPRIMIENDO] -> Documento: '{verNombre(impresion)}' enviado a la bandeja de salida.")
    else:
        print("\n[!] No hay trabajos pendientes en la cola.")
    print("\n" + "="*40)


# =====================================================================
# PUNTO 4: VISUALIZACIÓN DE LA COLA (OPCIÓN 4 DEL MENÚ)
# =====================================================================

def visualizacionGeneral(cola_a_mostrar, nombre_de_la_cola):
    print("\n" + "="*40)
    print(f"   VISUALIZACIÓN: {nombre_de_la_cola.upper()}")
    print("="*40)
    
    if not esVacia(cola_a_mostrar):
        # 1. Se crean estructuras auxiliares de tránsito temporal.
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        
        # 2. Se copia la cola original a mostrar para no vaciarla por accidente durante los prints.
        copiarCola(cola_a_mostrar, cola_aux)
        
        # 3. Se vacía la cola auxiliar temporal leyendo cada trabajo.
        while not esVacia(cola_aux):
            trabajo = desencolar(cola_aux)
            
            # 4. Se usan los selectores del TAD Trabajo para acceder a cada propiedad protegida.
            print(f"\n  > [JOB ID]:         {verJobID(trabajo)}")
            print(f"    Documento:        {verNombre(trabajo)}")
            print(f"    Formato:          {verFormato(trabajo)}")
            print(f"    Páginas:          {verPaginas(trabajo)}")
            print(f"    Prioridad:        {verPrioridad(trabajo)}")
            print(f"    Fecha y Hora:     {verFecha(trabajo).strftime('%d/%m/%Y %H:%M:%S')}")
            print("  " + "-"*35)

            # 5. Se pasa el trabajo a la segunda auxiliar para resguardarlo.
            encolar(cola_aux2, trabajo)
            
        # 6. Se reconstruyen los datos (por convención de la lógica implementada) pasándolos de aux2 a aux, y de aux a la original.
        while not esVacia(cola_aux2):
            encolar(cola_aux, desencolar(cola_aux2))
        copiarCola(cola_aux, cola_a_mostrar) 
    else:
        print(f"\n[!] La {nombre_de_la_cola.lower()} está vacía.")
        
    print("\n" + "="*40)


# =====================================================================
# PUNTO 5: REAJUSTE MASIVO POR FECHAS (OPCIÓN 5 DEL MENÚ)
# =====================================================================

def reajusteMasivoPorFechas(cola_impresion):
    print("\n" + "="*40)
    print("   PROCESO: REAJUSTE MASIVO POR MES")
    print("="*40 + "\n")
    
    if not esVacia(cola_impresion):
        try:
            mes = int(input("-> Ingrese el número de mes (1-12), los correspondientes trabajos cambiarán su prioridad a 'baja': "))
            print("")
        except ValueError:
            print("\n[ERROR] Por favor, ingrese un número válido.")
            print("\n" + "="*40)
            return
            
        # 1. Preparación de las colas de respaldo.
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        copiarCola(cola_impresion, cola_aux)
        
        contador = 0
        # 2. Iteración sobre todos los elementos para evaluar la condición de fecha.
        while not esVacia(cola_aux):
            copiaTrabajo = desencolar(cola_aux)
            
            # 3. Se evalúa si el mes del objeto datetime devuelto por verFecha() coincide con el input.
            if verFecha(copiaTrabajo).month == mes:
                # 4. En caso afirmativo, se sobrescribe la prioridad a 'baja'.
                modPrioridad(copiaTrabajo, "baja")
                contador += 1
                
            # 5. El trabajo se guarda en la segunda auxiliar, haya sido modificado o no.
            encolar(cola_aux2, copiaTrabajo)
            
        # 6. Proceso de restauración de la cola original con los elementos ya actualizados.
        while not esVacia(cola_aux2):
            encolar(cola_aux, desencolar(cola_aux2))
        copiarCola(cola_aux, cola_impresion)
        
        print(f"[OK] Reajuste completado. Se modificaron {contador} trabajos a prioridad 'baja'.")
    else:
        print("[!] La cola está vacía.")
    print("\n" + "="*40)


# =====================================================================
# PUNTO 6A: FILTRADO POR FORMATO (OPCIÓN 6 DEL MENÚ)
# =====================================================================

def filtradoPorFormato(cola_impresion):
    if not esVacia(cola_impresion):
        print("\n--- FORMATOS DISPONIBLES PARA CANCELACIÓN ---")
        print("1. PDF")
        print("2. Imagen")
        print("3. Texto")
        
        try:
            opcion = int(input("Seleccione el formato que desea eliminar (1-3): "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return

        formato_a_eliminar = ""

        # 1. Mapeo de la opción ingresada al string correspondiente del formato.
        match opcion:
            case 1:
                formato_a_eliminar = "PDF"
            case 2:
                formato_a_eliminar = "Imagen"
            case 3:
                formato_a_eliminar = "Texto"

        if formato_a_eliminar == "":
            print("Opción inválida. Volviendo al menú principal.")
            return

        print(f"\nIniciando la purga de archivos tipo: {formato_a_eliminar}...")

        # 2. Inicialización de colas de tránsito.
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        copiarCola(cola_impresion, cola_aux)
        
        # 3. Lógica central del filtrado: evaluar qué elementos sobreviven.
        while not esVacia(cola_aux):
            trabajo = desencolar(cola_aux)
            
            # 4. Si el formato del trabajo NO ES igual al que queremos eliminar...
            if verFormato(trabajo).upper() != formato_a_eliminar.upper():
                # 5. ...entonces se guarda (sobreviven). Si son iguales, el 'if' se ignora y el trabajo 
                # se pierde (se elimina).
                encolar(cola_aux2, trabajo)
        
        # 6. Reconstrucción de la cola original, ahora solo con los elementos que sobrevivieron al filtro.
        while not esVacia(cola_aux2):
            encolar(cola_aux, desencolar(cola_aux2))
        copiarCola(cola_aux,cola_impresion)
        
        print(f"Purga completada. Se eliminaron todos los trabajos '{formato_a_eliminar}'.")
    else:
        print("La cola está vacía.")


# =====================================================================
# PUNTO 6B: FILTRADO POR FRANJA HORARIA (OPCIÓN 7 DEL MENÚ)
# =====================================================================

def filtradoPorFranjaHorario(cola_impresion, segundaCola):
    if not esVacia(cola_impresion):
        
        # 1. Se vacía la sub-cola de resultados anteriores para evitar acumular basura en memoria.
        while not esVacia(segundaCola):
            desencolar(segundaCola)

        print("\n--- FRANJAS HORARIAS ---")
        print("1. Mañana (08:00 a 11:59)")
        print("2. Tarde  (12:00 a 17:59)")
        print("3. Noche  (18:00 a 21:59)")
        
        try:
            opcion = int(input("Ingrese una opción (1-3): "))
        except ValueError:
            print("Opción inválida.")
            return

        horaInicio = 0
        horaFin = 0

        # 2. Definición de los límites de las franjas horarias.
        match opcion:
            case 1:
                horaInicio, horaFin = 8, 12
            case 2:
                horaInicio, horaFin = 12, 18
            case 3:
                horaInicio, horaFin = 18, 22
            case _:
                print("Opción inválida.")
                return

        # 3. Estructuras auxiliares para recorrer la cola principal sin perderla.
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        copiarCola(cola_impresion, cola_aux)
        
        # 4. Proceso de duplicación selectiva.
        while not esVacia(cola_aux):
            trabajo = desencolar(cola_aux)
            
            # 5. Se extrae solamente la propiedad '.hour' de la fecha del trabajo.
            hora_envio = verFecha(trabajo).hour 
            
            # 6. Si la hora de envío se encuentra dentro del rango seleccionado...
            if horaInicio <= hora_envio < horaFin:
                # 7. ...se inserta una referencia de este trabajo en la nueva sub-cola.
                encolar(segundaCola, trabajo)
                
            # 8. De todas formas, se guarda en la auxiliar para no perderlo de la cola principal.
            encolar(cola_aux2, trabajo)
        
        # 9. Restauración de la cola principal intacta.
        while not esVacia(cola_aux2):
            encolar(cola_aux, desencolar(cola_aux2))
        copiarCola(cola_aux, cola_impresion) 
        
        # 10. Lógica de impresión temporal para mostrar el resultado de la sub-cola generada,
        # utilizando nuevamente el mecanismo de vaciar y re-encolar para lectura.
        print("\n=== CONTENIDO DE LA SUB-COLA GENERADA ===")
        if esVacia(segundaCola):
            print("No se encontraron trabajos en esa franja horaria.")
        else:
            cola_aux_sub = crearCola()
            cola_aux_sub2 = crearCola()
            
            while not esVacia(segundaCola):
                t = desencolar(segundaCola)
                print(f"ID: {verJobID(t)} | Doc: {verNombre(t)} | Hora: {verFecha(t).strftime('%H:%M:%S')}")
                encolar(cola_aux_sub, t)
                
            while not esVacia(cola_aux_sub):
                encolar(cola_aux_sub2, desencolar(cola_aux_sub))
                
            while not esVacia(cola_aux_sub2):
                encolar(segundaCola, desencolar(cola_aux_sub2))
                
    else:
        print("La cola está vacía")


# =====================================================================
# PROCESO ADICIONAL: VACIAR COLA COMPLETA
# =====================================================================
def vaciarColaEspecifica(cola, nombre_cola):
    print("\n" + "="*40)
    print(f"   ACCIÓN: VACIAR {nombre_cola.upper()}")
    print("="*40)
    
    if not esVacia(cola):
        contador = 0
        while not esVacia(cola):
            desencolar(cola)
            contador += 1
        print(f"\n[OK] {nombre_cola} vaciada por completo. Se eliminaron {contador} elementos.")
    else:
        print(f"\n[!] La {nombre_cola} ya se encontraba vacía.")
    print("\n" + "="*40)


# =====================================================================
# PROGRAMA PRINCIPAL (Menú Interactivo)
# =====================================================================

def menu():
    
    cola_impresion = crearCola()
    segunda_cola = crearCola() # Creamos una segunda cola global para la opción 6b
    
    while True:
        print("\n" + "="*40)
        print("   SISTEMA DE GESTIÓN DE IMPRESIÓN")
        print("="*40)
        print("1. Recepción de Documentos")
        print("2. Cambio de Prioridad Individual")
        print("3. Procesar Impresión")
        print("4. Visualización de la Cola Principal (Cola 1)")
        print("5. Reajuste Masivo por Fecha")
        print("6. Cancelación por Formato (Filtrar)")
        print("7. Generación de Sub-Cola Horaria")
        print("8. Visualización de la Sub-Cola (Cola 2)")
        print("9. Vaciar Cola Principal (Cola 1)")
        print("10. Vaciar Sub-Cola Horaria (Cola 2)")
        print("11. [TEST] Cargar datos de ejemplo")
        print("12. Salir")
        print("="*40)
        
        try:
            opcion = int(input("Seleccione una opción (1-12): "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        match opcion:
            case 1:
                ingreso(cola_impresion)
            case 2:
                cambiarPrioridad(cola_impresion)
            case 3:
                procesarImpresion(cola_impresion)
            case 4:
                visualizacionGeneral(cola_impresion, "Cola Principal (Cola 1)")
            case 5:
                reajusteMasivoPorFechas(cola_impresion)
            case 6:
                filtradoPorFormato(cola_impresion)
            case 7:
                filtradoPorFranjaHorario(cola_impresion, segunda_cola)
            case 8:
                visualizacionGeneral(segunda_cola, "Sub-Cola Horaria (Cola 2)")
            case 9:
                vaciarColaEspecifica(cola_impresion, "Cola Principal")
            case 10:
                vaciarColaEspecifica(segunda_cola, "Sub-Cola Horaria")
            case 11:
                cargarDatosEjemplo(cola_impresion)
            case 12:
                print("\nSaliendo del sistema... ¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")

# Esta línea le dice a Python que ejecute el menú apenas abre el archivo
if __name__ == "__main__":
    menu()