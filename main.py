from tads.trabajo_tad import *
from tads.cola_tad import *
from datetime import datetime, time

cola_impresion = crearCola()

def ingreso():
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


# Consultar
def cambiarPrioridad():
    jobID = input("Ingrese el ID del trabajo para cambiar su prioridad: ")
    nuevaPri = input("Ingrese la nueva prioridad: ")

    for i in range(tamanio(cola_impresion)):
        trabajo_actual = desencolar(cola_impresion)
        if verJobID(trabajo_actual) == jobID:
            modPrioridad(trabajo_actual, nuevaPri)
            print("Prioridad del trabajo actualizada.")
        encolar(cola_impresion, trabajo_actual)

# Consultar si debería pasar por referencia la cola, o si la cola es global por que es una sola
def procesarImpresion():
    impresion = desencolar(cola_impresion)
    print("Impresión procesada: ", verNombre(impresion))



def visualizacionCola():
    if not esVacia(cola_impresion):
        for i in range(tamanio(cola_impresion)):
                copiaTrabajo = copiarTrabajoEnI(cola_impresion,i)
                print("Id del trabajo: ", verJobID(copiaTrabajo))
                print("Nombre del trabajo: ", verNombre(copiaTrabajo))
                print("Formato del trabajo: ", verFormato(copiaTrabajo))
                print("Cantidad del páginas del trabajo: ", verPaginas(copiaTrabajo))
                print("Nivel de Prioridad del trabajo: ", verPrioridad(copiaTrabajo))
                print("Fecha y Hora del trabajo: ", verFecha(copiaTrabajo))
    else:
        print("La cola está vacía")


def reajusteMasivoPorFechas():
    if not esVacia(cola_impresion):
        mes = int(input("Ingrese un mes para comenzar el reajuste: "))
        for i in range(tamanio(cola_impresion)):
                copiaTrabajo = copiarTrabajoEnI(cola_impresion,i)
                if (verFecha(cola_impresion) == mes): #Chekear bien como hacemos la comparación según la librería de fechas
                    modPrioridad(copiaTrabajo,"baja")
    else:
        print("La cola está vacía")


def filtradoPorFormatoYFranjaHoraria():
    if not esVacia(cola_impresion):
        formato = int(input("Ingrese un formato para comenzar la purga: "))
        for i in range(tamanio(cola_impresion)):
                copiaTrabajo = copiarTrabajoEnI(cola_impresion,i)
                if (verFormato(cola_impresion) == formato): #Chekear bien como hacemos la comparación según la librería de fechas
                    modPrioridad(copiaTrabajo)
    else:
        print("La cola está vacía")
        