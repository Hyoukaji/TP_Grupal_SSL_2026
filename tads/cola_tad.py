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