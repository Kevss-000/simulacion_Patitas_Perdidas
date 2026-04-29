#simulando datos de la tabla USUARIOS en PYTHON

import random

def generar_usuarios(cantidad):

    listaNombres=["Carlos Perez","Ana Gomez","Luis Martinez","Maria Lopez",
                  "Jorge Rodriguez","Sofia Hernandez","Andres Torres","Valentina Diaz",
                  "Felipe Vargas","Isabella Mora","Samuel Castro","Daniela Rios"]

    listaDominios=["gmail.com","hotmail.com","yahoo.com","outlook.com"]

    usuarios=[]

    for i in range(cantidad):
        nombre=random.choice(listaNombres)
        primer_nombre=nombre.split()[0].lower()
        correo=f"{primer_nombre}{random.randint(1,99)}@{random.choice(listaDominios)}"
        telefono=f"3{random.randint(100000000,199999999)}"
        contrasena=f"Pass{random.randint(1000,9999)}!"

        usuario={
            "id_usuario": i + 1,
            "nombre": nombre,
            "correo": correo,
            "telefono": telefono,
            "contrasena": contrasena,
        }

        #inyectando errores controlados
        probabilidadError=random.random()

        if probabilidadError<0.1:
            usuario["correo"]=usuario["correo"].replace("@","")
        elif probabilidadError<0.2:
            usuario["correo"]=None
        elif probabilidadError<0.3:
            usuario["telefono"]="TEL-"+usuario["telefono"][:5]+"XX"
        elif probabilidadError<0.4:
            usuario["nombre"]=None

        usuarios.append(usuario)
    return usuarios
