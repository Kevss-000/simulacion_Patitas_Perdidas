#simulando datos de la tabla REPORTES en PYTHON

import random

def generar_reportes(cantidad):

    listaTipos=["perdido","encontrado"]

    listaEstados=["activo"]

    reportes=[]

    for i in range(cantidad):
        reporte={
            "id_reporte": i + 1,
            "tipo_reporte": random.choice(listaTipos),
            "fecha": f"2026-{random.randint(1,12)}-{random.randint(1,28)}",
            "estado": random.choice(listaEstados),
            "id_usuario": random.randint(1,20),
        }

        #inyectando errores controlados
        probabilidadError=random.random()

        if probabilidadError<0.1:
            reporte["tipo_reporte"]=random.choice(["urgente","spam","prueba"])
        elif probabilidadError<0.2:
            reporte["fecha"]=None
        elif probabilidadError<0.3:
            reporte["estado"]=random.choice(["borrador","pendiente","ACTIVO",""])
        elif probabilidadError<0.4:
            reporte["id_usuario"]=None

        reportes.append(reporte)
    return reportes
