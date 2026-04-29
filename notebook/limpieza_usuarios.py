import pandas as pd

def limpiar_simulasiones(data_frame_sucio):

    data_frame_limpio = data_frame_sucio.copy()

    # -----------------------------
    # rutina para evaluar textos
    # seleccionar todas las columnas de tipo texto y eliminar mayúsculas innecesarias
    # -----------------------------
    columnas_textos = [
        "idusuario", "nomusuario", "dirusuario",
        "telusuario", "correousuario", "contrausuario", "activo"
    ]

    for columna in columnas_textos:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

    # limpiar los textos solo con valores esperados
    valores_activo = ["si", "no"]
    data_frame_limpio["activo"] = data_frame_limpio["activo"].where(
        data_frame_limpio["activo"].isin(valores_activo),
        pd.NA
    )

    ciudades_esperadas = ["bello", "medellin", "itagui", "envigado"]
    data_frame_limpio["dirusuario"] = data_frame_limpio["dirusuario"].where(
        data_frame_limpio["dirusuario"].isin(ciudades_esperadas),
        pd.NA
    )

    # -----------------------------
    # rutina para evaluar numeros
    # evaluar que las columnas numericas si sean numeros
    # -----------------------------
    data_frame_limpio["idusuario"] = pd.to_numeric(data_frame_limpio["idusuario"], errors="coerce")
    data_frame_limpio = data_frame_limpio[data_frame_limpio["idusuario"] > 0]

    data_frame_limpio["telusuario"] = pd.to_numeric(data_frame_limpio["telusuario"], errors="coerce")
    data_frame_limpio = data_frame_limpio[
        (data_frame_limpio["telusuario"] >= 3000000000) &
        (data_frame_limpio["telusuario"] <= 3999999999)
    ]

    # -----------------------------
    # rutina para evaluar fechas
    # evaluemos que una fecha si sea una fecha
    # -----------------------------
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"], errors="coerce")

    # reemplazar una fecha por defecto si llega vacía
    fecha_default = pd.to_datetime("1989-05-28")
    data_frame_limpio["fecha"] = data_frame_limpio["fecha"].fillna(fecha_default)

    # -----------------------------
    # rutina para evaluar campos obligatorios
    # -----------------------------
    columnas_obligatorias = ["idusuario", "nomusuario", "correousuario", "contrausuario", "telusuario"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio