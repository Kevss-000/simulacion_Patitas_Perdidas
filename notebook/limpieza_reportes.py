import pandas as pd

def limpiar_reportes(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #rutina para evaluar textos
    #seleccionar todas las columnas de tipo texto y eliminar sus espacios y poner todo en minuscula
    columnas_texto=["tipo_reporte","estado"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()

    #limpiar los textos solo con valores esperados
    tipos_esperados=["perdido","encontrado"]
    data_frame_limpio["tipo_reporte"]=data_frame_limpio["tipo_reporte"].where(
        data_frame_limpio["tipo_reporte"].isin(tipos_esperados),
        pd.NA
        )

    estados_esperados=["activo"]
    data_frame_limpio["estado"]=data_frame_limpio["estado"].where(
        data_frame_limpio["estado"].isin(estados_esperados),
        pd.NA
        )

    #rutina para evaluar numeros
    #evaluar que las columnas numericas si son numeros
    data_frame_limpio["id_reporte"]=pd.to_numeric(data_frame_limpio["id_reporte"])
    data_frame_limpio["id_usuario"]=pd.to_numeric(data_frame_limpio["id_usuario"])

    #rutina para evaluar fechas
    #evaluemos que una fecha si sea una fecha
    data_frame_limpio["fecha"]=pd.to_datetime(data_frame_limpio["fecha"])

    #reemplazar una fecha por defecto si el campo llega vacio
    fecha_default=pd.to_datetime("1998-11-04")
    data_frame_limpio["fecha"]=data_frame_limpio["fecha"].fillna(fecha_default)

    #rutina para evaluar novedades
    #rutina para evaluar campos obligatorios que vienen vacios
    columnas_obligatorias=["id_reporte","tipo_reporte","estado","id_usuario"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio
