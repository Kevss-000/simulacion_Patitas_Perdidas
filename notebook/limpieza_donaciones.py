import pandas as pd

def limpiar_donaciones(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #Rutina para evaluar textos
    #Seleccionar todas las columnas de tipo texto y eliminar sus espacio y poner todo en miniscula
    columnas_texto=["desdonaciones"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()

    #Limpiar los textos solo con valores esperados
    descripciones_esperadas=["esterilizacion","corte uñas","vacunacion"]
    data_frame_limpio["desdonaciones"]=data_frame_limpio["desdonaciones"].where(data_frame_limpio["desdonaciones"].isin(descripciones_esperadas),pd.NA)

    #Rutina para evaluar números
    #Evaluar que las columnas numericas si son numeros
    data_frame_limpio["idusuarios"]=pd.to_numeric(data_frame_limpio["idusuarios"], errors='coerce')
    data_frame_limpio["montodonaciones"]=pd.to_numeric(data_frame_limpio["montodonaciones"], errors='coerce')

    #Evaluar solo valores numericos permitidos
    data_frame_limpio=data_frame_limpio[data_frame_limpio["idusuarios"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["montodonaciones"]>100000]

    #Rutina para evaluar fechas
    #Evaluemos que una fecha si es una fecha
    data_frame_limpio["fecdonaciones"]=pd.to_datetime(data_frame_limpio["fecdonaciones"], errors='coerce')

    #Remplazar una fecha por defecto si el campo llega vacio
    fecha_default=pd.to_datetime("2026-01-01")
    data_frame_limpio["fecdonaciones"]=data_frame_limpio["fecdonaciones"].fillna(fecha_default)

    #Rutina para evaluar booleanos
    #Mapear el activo asumiendo valores lógicos booleanos
    data_frame_limpio["activo"]=pd.to_numeric(data_frame_limpio["activo"], errors='coerce').fillna(0).astype(bool)

    #Rutina para evaluar novedades
    #Rutina para evaluar campos obligatorios que vienen vacios
    columnas_obligatorias=["idusuarios","desdonaciones","montodonaciones","activo"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio

if __name__ == "__main__":
    # Prueba del script importando la simulación
    import sys
    import os
    
    # Asegurar que utils puede ser importado
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils.simulacion_donaciones import generar_simulacion
    
    simulaciones = generar_simulacion(10)
    df_sucio = pd.DataFrame(simulaciones)
    
    print("--- Datos Sucios Originales (Simulación) ---")
    print(df_sucio.head())
    
    df_limpio = limpiar_simulasion(df_sucio)
    
    print("\n--- Datos Limpios ---")
    print(df_limpio.head())
