import pandas as pd
def limpiar_volun(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #rutina para evaluar textos
    #seleccionar todas las columnas de tipo texto y eliminar las mayusculas yinecesarias
    columnas_textos=["id","descripcion"];
    for columna in columnas_textos:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()
        #limpiar los textos solo con valores esperados
        lugar_esperados=["españa","salon","casa"]
        data_frame_limpio["lugar"]=data_frame_limpio["lugar"].where(
            data_frame_limpio["lugar"].isin(lugar_esperados),
            pd.NA
        )
    #rutina para evaluar numeros
    #evaluar que las columnas numericas si sean numeros
    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
    #evaluar solo valores numericos permitidos 
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]

    #rutina para evaluar fechas
    #evaluemos que una fecha si sea una fecha
    data_frame_limpio["fecha"]=pd.to_datetime(data_frame_limpio["fecha"])
    #reeplazatr una fecha ´por de fecto si el campo llega vacio
    fecha_default=pd.to_datetime("1989-05-28")
    data_frame_limpio["fecha"]=data_frame_limpio["fecha"].fillna(fecha_default)
    #rutina para evaluar novedades
    #rutina para evaluar campos obligatorios que vienen obligatorios
    columnas_obligatorias=["id","lugar","descripcion"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio
