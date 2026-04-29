import pandas as pd

def limpiar_mascotas(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #rutina para evaluar textos
    #seleccionar todas las columnas de tipo texto y eliminar sus espacios y poner todo en minuscula
    columnas_texto=["nombre","tipo","raza"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()

    #limpiar los textos solo con valores esperados
    tipos_esperados=["perro","gato","conejo","ave"]
    data_frame_limpio["tipo"]=data_frame_limpio["tipo"].where(
        data_frame_limpio["tipo"].isin(tipos_esperados),
        pd.NA
        )

    #rutina para evaluar numeros
    #evaluar que las columnas numericas si son numeros
    data_frame_limpio["id_mascota"]=pd.to_numeric(data_frame_limpio["id_mascota"])
    data_frame_limpio["id_usuario"]=pd.to_numeric(data_frame_limpio["id_usuario"])

    #rutina para evaluar novedades
    #rutina para evaluar campos obligatorios que vienen vacios
    columnas_obligatorias=["id_mascota","nombre","tipo","raza","id_usuario"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio
