from tads.trabajo_tad import *
from tads.cola_tad import *
from datetime import datetime, time

cola_impresion = crearCola()

def ingreso(cola_impresion):
    print("\nNUEVO TRABAJO DE IMPRESIÓN")

    trabajo = crearTrabajo()

    jobID = input("ID de Trabajo: ")
    nom = input("Nombre del Documento: ")
    fmt = input("Tipo de Formato (PDF/Imagen/Texto): ")
    pag = int(input("Cantidad de Páginas: "))
    pri = input("Nivel de Prioridad: ")
    fecha = datetime.now().time()

    cargarTrabajo(trabajo, jobID, nom, fmt, pag, pri, fecha)

    encolar(cola_impresion, trabajo)

    print("Trabajo agregado a la cola de impresión.")



def cambiarPrioridad(cola_impresion):
    if not esVacia(cola_impresion):
        jobID = input("Ingrese el ID del trabajo para cambiar su prioridad: ")
        nuevaPri = input("Ingrese la nueva prioridad: ")
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        copiarCola(cola_impresion,cola_aux)
        while not esVacia(cola_aux):
            trabajo_actual = desencolar(cola_aux)
            if verJobID(trabajo_actual) == jobID:
                modPrioridad(trabajo_actual, nuevaPri)
                print("Prioridad del trabajo actualizada.")
            encolar(cola_aux2, trabajo_actual)
        while not esVacia(cola_aux2):
                    copiaTrabajo = desencolar(cola_aux2)
                    encolar(cola_aux,copiaTrabajo)
        copiarCola(cola_impresion,cola_aux)
    else:
        print("La cola está vacía")


def procesarImpresion(cola_impresion):
    impresion = desencolar(cola_impresion)
    print("Impresión procesada: ", verNombre(impresion))



def visualizacionCola(cola_impresion):
    if not esVacia(cola_impresion):
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        copiarCola(cola_impresion,cola_aux)
        while not esVacia(cola_aux):
                copiaTrabajo = desencolar(cola_aux)
                print("Id del trabajo: ", verJobID(copiaTrabajo))
                print("Nombre del trabajo: ", verNombre(copiaTrabajo))
                print("Formato del trabajo: ", verFormato(copiaTrabajo))
                print("Cantidad del páginas del trabajo: ", verPaginas(copiaTrabajo))
                print("Nivel de Prioridad del trabajo: ", verPrioridad(copiaTrabajo))
                print("Fecha y Hora del trabajo: ", verFecha(copiaTrabajo))

                encolar(cola_aux2,copiaTrabajo)
        while not esVacia(cola_aux2):
                copiaTrabajo = desencolar(cola_aux2)
                encolar(cola_aux,copiaTrabajo)
        copiarCola(cola_impresion,cola_aux)
    else:
        print("La cola está vacía")


def reajusteMasivoPorFechas(cola_impresion):
    if not esVacia(cola_impresion):
        mes = int(input("Ingrese un mes para comenzar el reajuste: "))
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        copiarCola(cola_impresion,cola_aux)
        while not esVacia(cola_aux):
                copiaTrabajo = desencolar(cola_aux)
                if (verFecha(copiaTrabajo) == mes): #Chekear bien como hacemos la comparación según la librería de fechas
                    modPrioridad(copiaTrabajo,"baja")
                encolar(cola_aux2,copiaTrabajo)
        while not esVacia(cola_aux2):
                copiaTrabajo = desencolar(cola_aux2)
                encolar(cola_aux,copiaTrabajo)
        copiarCola(cola_impresion,cola_aux)
    else:
        print("La cola está vacía")


def filtradoPorFormato(cola_impresion):# Revisar bien la condicion
    if not esVacia(cola_impresion):
        formato = int(input("Ingrese un formato para comenzar la purga: "))
        cola_aux = crearCola()
        cola_aux2 = crearCola()
        copiarCola(cola_impresion,cola_aux)
        while not esVacia(cola_aux):
                copiaTrabajo = desencolar(cola_aux)
                if (verFormato(copiaTrabajo) != formato): 
                    encolar(cola_aux2,copiaTrabajo)
        while not esVacia(cola_aux2):
                copiaTrabajo = desencolar(cola_aux2)
                encolar(cola_aux,copiaTrabajo)
        copiarCola(cola_impresion,cola_aux)
    else:
        print("La cola está vacía")

def filtradoPorFranjaHorario(cola_impresion,segundaCola):#Falta terminar
    if not esVacia(cola_impresion):
         opcion = int(input("Ingrese una de las opciones para filtrar por franja horaria: "))
         horaInicio = 0
         horaFin = 0
         match opcion:
            case 1:#Chekear bien como hacemos la comparación según la librería de fechas
                print("Elegiste la opción 1: Mañana")
                horaInicio = 8
                horaFin = 12
            case 2:
                print("Elegiste la opción 2: Tarde")
                horaInicio = 12
                horaFin = 18
            case 3:
                print("Elegiste la opción 3: Noche")
                horaInicio = 18
                horaFin = 22
         cola_aux = crearCola()
         cola_aux2 = crearCola()
         copiarCola(cola_impresion,cola_aux)
         while not esVacia(cola_aux):
            copiaTrabajo = desencolar(cola_aux)
            if (verFecha(copiaTrabajo) >= horaInicio and verFecha(copiaTrabajo) < horaFin): 
                encolar(cola_aux2,copiaTrabajo)
         while not esVacia(cola_aux2):
                copiaTrabajo = desencolar(cola_aux2)
                encolar(segundaCola,copiaTrabajo)
         copiarCola(segundaCola,cola_aux)
        
    else:
        print("La cola está vacía")
        