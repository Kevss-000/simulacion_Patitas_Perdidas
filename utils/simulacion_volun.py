import random

from datetime import datetime,timedelta

def generar_volun(numeroSimulaciones):

    lugares=["españa","salon","casa"]
    descripcion=["peludo con canas","super juegueton","no apto para niños"]
    fecha=datetime(2026,1,2)

    simulaciones=[]
    for _ in range(numeroSimulaciones):

        simulacion={
            "id":random.randint(1,20),
            "lugar":random.choice(lugares),
            "descripcion":random.choice(descripcion),
            "fecha":fecha+timedelta(days=random.randint(0,60))
        }

        #Inyectando errores controlados 
        probabilidadError=random.random()
        if(probabilidadError<0.2):
            simulacion["id"]=None
        elif(probabilidadError<0.5):
            simulacion["descripcion"]=random.choice(["feo","muy pelion",None])
        elif(probabilidadError<0.9):
            simulacion["fecha"]=None

        simulaciones.append(simulacion)
    return simulaciones
