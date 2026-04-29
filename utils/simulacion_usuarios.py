import random
import string
from datetime import datetime, timedelta

def generar_simulacion(numeroSimulaciones):

    fecha_base = datetime(2026, 1, 2)

    simulaciones = []

    for i in range(numeroSimulaciones):
        simulacion = {
            "idusuario": str(random.randint(1000, 9999)),
            "nomusuario": random.choice(["Kevin", "Ana", "Luis", "Maria", "Carlos"]),
            "dirusuario": random.choice(["Bello", "Medellin", "Itagui", "Envigado"]),
            "telusuario": str(random.randint(3000000000, 3999999999)),
            "correousuario": f"user{i}@correo.com",
            "contrausuario": ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
            "activo": random.choice(["SI", "NO"]),
            "fecha": fecha_base + timedelta(days=random.randint(0, 60))
        }

        # Inyectando errores controlados
        probabilidadError = random.random()
        if probabilidadError < 0.15:
            simulacion["idusuario"] = None
        elif probabilidadError < 0.25:
            simulacion["idusuario"] = "-10"  
            simulacion["fecha"] = None
        elif probabilidadError < 0.70:
            simulacion["telusuario"] = "12345"  
        elif probabilidadError < 0.55:
            simulacion["dirusuario"] = "Bogota"
        elif probabilidadError < 0.40:
            simulacion["nomusuario"] = "   " + simulacion["nomusuario"].upper() + "   "

        simulaciones.append(simulacion)

    return simulaciones
