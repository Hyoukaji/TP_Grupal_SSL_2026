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

# Consultar si con esto me ahorro el problema de la 2) y la 5)
def copiarTrabajoEnI(cola,i):
    if not esVacia(cola):
        return cola[i]
    else:
        return None