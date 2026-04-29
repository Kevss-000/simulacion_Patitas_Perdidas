#simulando datos de una tabla en PYTHON

import random

def generar_ubicaciones(cantidad): 

    listaNombres=["crear ubicacion","eliminar ubicacion","actualizar ubicacion","consultar ubicacion"]

    listaCiudades=["Bogota","Medellin","Cali","Barranquilla","Cartagena"]

    listaZonas = ["Norte", "Sur", "Centro", "Oriente", "Occidente"]

    ubicaciones=[]

    for i in range(cantidad):
        ubicacion={
            "id_ubicacion": i + 1,
            "ciudad": random.choice(listaCiudades),
            "zona": random.choice(listaZonas),
            "direccion": f"Calle {random.randint(1, 100)} #{random.randint(1, 50)}-{random.randint(1, 50)}",
            "id_reporte": random.randint(1, 50),
            "fecha_reporte": f"2024-{random.randint(1,12)}-{random.randint(1,28)}"
        }

        #inyectando errores controlados
        probabilidadError=random.random()

        if probabilidadError<0.1:
            ubicacion["id_ubicacion"]=random.choice([None,-1,0])
            ubicacion["ciudad"]=None
        elif probabilidadError<0.3:
            ubicacion["zona"]=" "+ubicacion["zona"]+" "
        elif probabilidadError<0.6:
            ubicacion["direccion"]=ubicacion["direccion"].upper()
        elif probabilidadError<0.9:
            ubicacion["id_reporte"]=None

        ubicaciones.append(ubicacion)
    return ubicaciones