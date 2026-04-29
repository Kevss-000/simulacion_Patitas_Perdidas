import pandas as pd

def limpiar_usuarios(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #rutina para evaluar textos
    #seleccionar todas las columnas de tipo texto y eliminar sus espacios y poner todo en minuscula
    columnas_texto=["nombre","correo"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()

    #rutina para evaluar correos
    #evaluar que el correo tenga @
    data_frame_limpio=data_frame_limpio[data_frame_limpio["correo"].str.contains("@",na=False)]

    #rutina para evaluar telefonos
    #evaluar que el telefono solo tenga numeros
    data_frame_limpio["telefono"]=data_frame_limpio["telefono"].astype("string")
    data_frame_limpio=data_frame_limpio[data_frame_limpio["telefono"].str.match(r"^\d{10}$",na=False)]

    #rutina para evaluar numeros
    #evaluar que las columnas numericas si son numeros
    data_frame_limpio["id_usuario"]=pd.to_numeric(data_frame_limpio["id_usuario"])

    #rutina para evaluar novedades
    #rutina para evaluar campos obligatorios que vienen vacios
    columnas_obligatorias=["id_usuario","nombre","correo","telefono","contrasena"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio=data_frame_limpio.drop_duplicates(subset=["id_usuario"])

    return data_frame_limpio
