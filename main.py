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