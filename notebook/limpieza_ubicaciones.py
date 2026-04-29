import pandas as pd

def limpiar_ubicaciones(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #rutina para evaluar textos 
    #seleccionar todas las columnas de tipo texto y eliminar sus espacios y poner todo en minuscula
    columnas_texto=["zona","ciudad"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()

    #limpiar los textos solo con valores esperados
    ubicaciones_esperados=["norte","sur","centro","oriente","occidente"]
    data_frame_limpio["zona"]=data_frame_limpio["zona"].where(
        data_frame_limpio["zona"].isin(ubicaciones_esperados),
        pd.NA
        )
    
    #rutina para evaluar numeros
    #evaluar que las columnas numericas si son numeros
    data_frame_limpio["id_ubicacion"]=pd.to_numeric(data_frame_limpio["id_ubicacion"])
    data_frame_limpio["id_reporte"]=pd.to_numeric(data_frame_limpio["id_reporte"])

    #evaluar solo valores numericos permitidos
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id_ubicacion"]>0]

    #rutina para evaluar fechas
    #evaluemos que una fecha si sea una fecha
    data_frame_limpio["fecha_reporte"]=pd.to_datetime(data_frame_limpio["fecha_reporte"])

    #reemplazar una fecha por defecto si el campo llega vacio
    fecha_default=pd.to_datetime("1998-11-04")
    data_frame_limpio["fecha_reporte"]=data_frame_limpio["fecha_reporte"].fillna(fecha_default)

    #rutina para evaluar novedades
    #rutina para evaluar campos obligatorios que vienen vacios
    columnas_obligatorias=["id_ubicacion","ciudad","zona","direccion","id_reporte"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio
