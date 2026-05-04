def crearTrabajo():
    trabajo = ["", "", "", 0, "", None]
    return trabajo

def cargarTrabajo(trabajo, jobID, nom, fmt, pag, pri, fecha):
    trabajo[0] = jobID
    trabajo[1] = nom
    trabajo[2] = fmt
    trabajo[3] = pag
    trabajo[4] = pri
    trabajo[5] = fecha
    return trabajo

def verJobID(trabajo):
    return trabajo[0]

def verNombre(trabajo):
    return trabajo[1]

def verFormato(trabajo):
    return trabajo[2]

def verPaginas(trabajo):
    return trabajo[3]

def verPrioridad(trabajo):
    return trabajo[4]

def verFecha(trabajo):
    return trabajo[5]

def modPrioridad(trabajo, nuevaPri):
    trabajo[4] = nuevaPri