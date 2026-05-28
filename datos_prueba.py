from tads.trabajo_tad import *
from tads.cola_tad import *
from datetime import datetime

def cargarDatosEjemplo(cola_impresion):
    # Lista de datos hardcodeados para automatizar la carga
    # Año 2026, Mes 5 (Mayo), variando las horas para las franjas
    trabajos_ficticios = [
        {"id": "101", "nom": "Reporte_Anual.pdf", "fmt": "PDF", "pag": 15, "pri": "Alta", "hora": 9},    # Mañana
        {"id": "102", "nom": "Flyer_Final.png", "fmt": "Imagen", "pag": 1, "pri": "Media", "hora": 10},  # Mañana
        {"id": "103", "nom": "Tesis_Version3.docx", "fmt": "Texto", "pag": 84, "pri": "Alta", "hora": 14}, # Tarde
        {"id": "104", "nom": "Captura_Error.jpg", "fmt": "Imagen", "pag": 2, "pri": "Baja", "hora": 16},  # Tarde
        {"id": "105", "nom": "Contrato_Alquiler.pdf", "fmt": "PDF", "pag": 8, "pri": "Alta", "hora": 19},  # Noche
    ]
    
    for t in trabajos_ficticios:
        trabajo = crearTrabajo()
        # Creamos el objeto datetime forzando la hora especificada para el testeo
        fecha_ficticia = datetime(2026, 5, 28, t["hora"], 0, 0)
        
        cargarTrabajo(trabajo, t["id"], t["nom"], t["fmt"], t["pag"], t["pri"], fecha_ficticia)
        encolar(cola_impresion, trabajo)
        
    print(f"\n[OK] Se cargaron {len(trabajos_ficticios)} trabajos de prueba exitosamente.")