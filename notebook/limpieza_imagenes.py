import pandas as pd

def limpiar_imagenes(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #rutina para evaluar textos
    #seleccionar todas las columnas de tipo texto y eliminar sus espacios
    columnas_texto=["url_imagen","descripcion"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip()

    #limpiar urls que no tienen protocolo http
    data_frame_limpio=data_frame_limpio[data_frame_limpio["url_imagen"].str.startswith("http",na=False)]

    #rutina para evaluar numeros
    #evaluar que las columnas numericas si son numeros
    data_frame_limpio["id_imagen"]=pd.to_numeric(data_frame_limpio["id_imagen"])
    data_frame_limpio["id_reporte"]=pd.to_numeric(data_frame_limpio["id_reporte"])

    #rutina para evaluar novedades
    #rutina para evaluar campos obligatorios que vienen vacios
    columnas_obligatorias=["id_imagen","url_imagen","id_reporte"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio
