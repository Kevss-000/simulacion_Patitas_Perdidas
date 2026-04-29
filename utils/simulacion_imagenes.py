#simulando datos de la tabla IMAGENES en PYTHON

import random

def generar_imagenes(cantidad):

    listaExtensiones=[".jpg",".png",".jpeg",".webp"]

    listaUrls=["https://mascotas.app/img/","https://cdn.reportes.com/fotos/",
               "https://storage.mascotas.net/uploads/"]

    listaDescripciones=["Foto de la mascota de frente","Imagen tomada en el parque",
                        "Foto enviada por el duenio","Imagen del avistamiento",
                        "Fotografia reciente de la mascota","Captura del momento del encuentro"]

    imagenes=[]

    for i in range(cantidad):
        nombre_archivo=f"mascota_{random.randint(1000,9999)}"
        url=random.choice(listaUrls)+nombre_archivo+random.choice(listaExtensiones)

        imagen={
            "id_imagen": i + 1,
            "url_imagen": url,
            "descripcion": random.choice(listaDescripciones),
            "id_reporte": random.randint(1,25),
        }

        #inyectando errores controlados
        probabilidadError=random.random()

        if probabilidadError<0.1:
            imagen["url_imagen"]=None
        elif probabilidadError<0.2:
            imagen["url_imagen"]=imagen["url_imagen"].replace("https://","")
        elif probabilidadError<0.3:
            imagen["id_reporte"]=None
        elif probabilidadError<0.4:
            imagen["descripcion"]=" "+imagen["descripcion"]+" "

        imagenes.append(imagen)
    return imagenes
