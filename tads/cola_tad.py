def crearCola():
    cola = []
    return cola

def esVacia(cola):
    return len(cola) == 0

def encolar(cola, trabajo):
    cola.append(trabajo)

def desencolar(cola):
    if not esVacia(cola):
        return cola.pop(0)
    else:
        return None
    
def tamanio(cola):
    return len(cola)

def copiarCola(cola_llena, cola_vacia):
    cola_aux = crearCola()
    if not esVacia(cola_vacia):
        while not esVacia(cola_vacia):
            desencolar(cola_vacia)
    
    while not esVacia(cola_llena):
        elemento = desencolar(cola_llena)
        encolar(cola_vacia, elemento)
        encolar(cola_aux, elemento)
        
    while not esVacia(cola_aux):
        elemento = desencolar(cola_aux)
        encolar(cola_llena, elemento)


