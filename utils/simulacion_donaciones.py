import random

from datetime import datetime,timedelta

def generar_donaciones(numeroSimulaciones):

    descripciones=["esterilizacion","corte uñas","vacunacion"]
    estados_activos=[True, False]
    montos=[350000,100000,250000]
    fechaInicio=datetime(2026,1,2)

    simulaciones=[]
    for _ in range(numeroSimulaciones):

        simulacion={
            "idusuarios":random.randint(0,200),
            "desdonaciones":random.choice(descripciones),
            "montodonaciones":random.choice(montos),
            "activo":random.choice(estados_activos),
            "fecdonaciones":fechaInicio+timedelta(days=random.randint(0,60))
        }

        #Inyectando errores controlados 
        probabilidadError=random.random()
        if(probabilidadError<0.2):
            simulacion["idusuarios"]=None
        elif(probabilidadError<0.4):
            simulacion["desdonaciones"]=random.choice(["clase de python","clase de ingles"])
        elif(probabilidadError<0.5):
            simulacion["montodonaciones"]=random.choice([0,-10000,None])
        elif(probabilidadError<0.8):
            simulacion["activo"]=random.choice([" ", "Error", None])
        elif(probabilidadError<0.9):
            simulacion["fecdonaciones"]=None

        simulaciones.append(simulacion)
    return simulaciones

if __name__ == "__main__":
    # Generar una simulación de prueba y mostrar los primeros 5 registros
    simulaciones_prueba = generar_simulacion(5)
    print("--- Resultados de la Simulación ---")
    for sim in simulaciones_prueba:
        print(sim)
