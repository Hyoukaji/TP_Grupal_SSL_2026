from tads.trabajo_tad import *
from tads.cola_tad import *
from datetime import datetime, time
from datos_prueba import cargarDatosEjemplo

# =====================================================================
# PUNTO 1: RECEPCIÓN DE DOCUMENTOS (OPCIÓN 1 DEL MENÚ)
# =====================================================================

def ingreso(cola_impresion):
    print("\nNUEVO TRABAJO DE IMPRESIÓN")

    trabajo = crearTrabajo()

    jobID = input("ID de Trabajo: ")
    nom = input("Nombre del Documento: ")
    fmt = input("Tipo de Formato (PDF/Imagen/Texto): ")
    pag = int(input("Cantidad de Páginas: "))
    pri = input("Nivel de Prioridad: ")
    fecha = datetime.now() 

    cargarTrabajo(trabajo, jobID, nom, fmt, pag, pri, fecha)

    encolar(cola_impresion, trabajo)

    print("Trabajo agregado a la cola de impresión.")

# =====================================================================
# PUNTO 2: CAMBIO DE PRIORIDAD INDIVIDUAL (OPCIÓN 2 DEL MENÚ)
# =====================================================================

def cambiarPrioridad(cola_impresion):
    print("\n" + "="*40)
    print("   PROCESO: CAMBIO DE PRIORIDAD INDIVIDUAL")
    print("="*40 + "\n")
    
    if not esVacia(cola_impresion):
        jobID = input("-> Ingrese el ID del trabajo a modificar: ")
        nuevaPri = input("-> Ingrese la nueva prioridad: ")
        print("")
        
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        copiarCola(cola_impresion, cola_aux)
        
        encontrado = False
        while not esVacia(cola_aux):
            trabajo_actual = desencolar(cola_aux)
            if verJobID(trabajo_actual) == jobID:
                modPrioridad(trabajo_actual, nuevaPri)
                print("[OK] Prioridad del trabajo actualizada en el sistema.")
                encontrado = True
            encolar(cola_aux2, trabajo_actual)
            
        while not esVacia(cola_aux2):
            encolar(cola_aux, desencolar(cola_aux2))
        copiarCola(cola_aux, cola_impresion) # Devolvemos los elementos a la cola original
        
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
    
    if not esVacia(cola_impresion):
        impresion = desencolar(cola_impresion)
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
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        copiarCola(cola_a_mostrar, cola_aux)
        
        while not esVacia(cola_aux):
            trabajo = desencolar(cola_aux)
            
            print(f"\n  > [JOB ID]:         {verJobID(trabajo)}")
            print(f"    Documento:        {verNombre(trabajo)}")
            print(f"    Formato:          {verFormato(trabajo)}")
            print(f"    Páginas:          {verPaginas(trabajo)}")
            print(f"    Prioridad:        {verPrioridad(trabajo)}")
            print(f"    Fecha y Hora:     {verFecha(trabajo).strftime('%d/%m/%Y %H:%M:%S')}")
            print("  " + "-"*35)

            encolar(cola_aux2, trabajo)
            
        while not esVacia(cola_aux2):
            encolar(cola_aux, desencolar(cola_aux2))
        copiarCola(cola_aux, cola_a_mostrar) # Devolvemos los elementos a la cola original aunque no es necesario porque no la modificamos, pero lo hacemos para mantener la estructura de las funciones anteriores
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
            mes = int(input("-> Ingrese el número de mes (1-12): "))
            print("")
        except ValueError:
            print("\n[ERROR] Por favor, ingrese un número válido.")
            print("\n" + "="*40)
            return
            
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        copiarCola(cola_impresion, cola_aux)
        
        contador = 0
        while not esVacia(cola_aux):
            copiaTrabajo = desencolar(cola_aux)
            if verFecha(copiaTrabajo).month == mes:
                modPrioridad(copiaTrabajo, "baja")
                contador += 1
            encolar(cola_aux2, copiaTrabajo)
            
        while not esVacia(cola_aux2):
            encolar(cola_aux, desencolar(cola_aux2))
        copiarCola(cola_aux, cola_impresion)# Devolvemos los elementos a la cola original
        
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

        # Creamos dos colas auxiliares para manejar el filtrado sin perder datos
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        
        # Copiamos la original a la primera auxiliar
        copiarCola(cola_impresion, cola_aux)
        
        # Vaciamos cola_aux pasando a cola_aux2 SOLO los que NO se eliminan
        while not esVacia(cola_aux):
            trabajo = desencolar(cola_aux)
            if verFormato(trabajo).upper() != formato_a_eliminar.upper():
                encolar(cola_aux2, trabajo)
        
        # Reconstruimos cola_aux con los elementos filtrados
        while not esVacia(cola_aux2):
            encolar(cola_aux, desencolar(cola_aux2))
            
        copiarCola(cola_aux,cola_impresion)# Devolvemos los elementos a la cola original
        
        print(f"Purga completada. Se eliminaron todos los trabajos '{formato_a_eliminar}'.")
    else:
        print("La cola está vacía.")


# =====================================================================
# PUNTO 6B: FILTRADO POR FRANJA HORARIA (OPCIÓN 7 DEL MENÚ)
# =====================================================================

def filtradoPorFranjaHorario(cola_impresion, segundaCola):
    if not esVacia(cola_impresion):
        # Vaciamos la segundaCola por si tenía datos de ejecuciones anteriores
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

        match opcion:
            case 1:
                horaInicio, horaFin = 8, 12
            case 2:
                horaInicio, horaFin = 12, 18
            case 3:
                horaInicio, horaFin = 18, 22
            case _:
                print("Opción no válida.")
                return

        cola_aux = crearCola()
        cola_aux2 = crearCola()
        
        copiarCola(cola_impresion, cola_aux)
        
        while not esVacia(cola_aux):
            trabajo = desencolar(cola_aux)
            hora_envio = verFecha(trabajo).hour 
            
            if horaInicio <= hora_envio < horaFin:
                encolar(segundaCola, trabajo)
                
            encolar(cola_aux2, trabajo)
        
        while not esVacia(cola_aux2):
            encolar(cola_aux, desencolar(cola_aux2))
            
        copiarCola(cola_aux, cola_impresion)# Devolvemos los elementos a la cola original aunque no es necesario porque no la modificamos, pero lo hacemos para mantener la estructura de las funciones anteriores
        
        # --- IMPRESIÓN AUTOMÁTICA DE LA SUB-COLA (CORREGIDA) ---
        print("\n=== CONTENIDO DE LA SUB-COLA GENERADA ===")
        if esVacia(segundaCola):
            print("No se encontraron trabajos en esa franja horaria.")
        else:
            cola_aux_sub = crearCola()
            cola_aux_sub2 = crearCola()
            
            # Pasamos de segundaCola a la aux_sub para leer e imprimir
            while not esVacia(segundaCola):
                t = desencolar(segundaCola)
                print(f"ID: {verJobID(t)} | Doc: {verNombre(t)} | Hora: {verFecha(t).strftime('%H:%M:%S')}")
                encolar(cola_aux_sub, t)
                
            # Pasamos de aux_sub a aux_sub2
            while not esVacia(cola_aux_sub):
                encolar(cola_aux_sub2, desencolar(cola_aux_sub))
                
            # Devolvemos de aux_sub2 a segundaCola de forma limpia y exacta
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
        