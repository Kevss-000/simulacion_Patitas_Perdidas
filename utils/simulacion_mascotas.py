#simulando datos de la tabla MASCOTAS en PYTHON

import random

def generar_mascotas(cantidad):

    listaNombres=["Max","Luna","Coco","Milo","Bella","Rocky","Nala","Thor","Kira","Simba"]

    listaTipos=["perro","gato","conejo","ave"]

    listaRazas={
        "perro": ["labrador","bulldog","golden retriever","poodle","beagle"],
        "gato": ["siames","persa","bengali","mestizo","angora"],
        "conejo": ["angora","enano","belier","rex"],
        "ave": ["canario","periquito","loro","cacatua"],
    }

    listaDescripciones=["Muy jugueton y amigable","Tranquilo, le gusta dormir",
                        "Activo y curioso","Timido pero carinoso",
                        "Le encanta salir a pasear","Sociable con otros animales"]

    mascotas=[]

    for i in range(cantidad):
        tipo=random.choice(listaTipos)

        mascota={
            "id_mascota": i + 1,
            "nombre": random.choice(listaNombres),
            "tipo": tipo,
            "raza": random.choice(listaRazas[tipo]),
            "descripcion": random.choice(listaDescripciones),
            "id_usuario": random.randint(1,20),
        }

        #inyectando errores controlados
        probabilidadError=random.random()

        if probabilidadError<0.1:
            mascota["tipo"]=random.choice(["dragon","unicornio","planta","robot"])
        elif probabilidadError<0.2:
            mascota["raza"]=None
        elif probabilidadError<0.3:
            mascota["id_usuario"]=None
        elif probabilidadError<0.4:
            mascota["nombre"]=" "+mascota["nombre"]+" "

        mascotas.append(mascota)
    return mascotas
