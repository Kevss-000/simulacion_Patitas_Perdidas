import pandas as pd

from utils.simulacion_usuarios import generar_simulacion
from notebook.limpieza_usuarios import limpiar_simulasiones

simulaciones = generar_simulacion(20)

simulaciones_ordenadas = pd.DataFrame(simulaciones)
simulaciones_limpias = limpiar_simulasiones(simulaciones_ordenadas)
print(simulaciones_limpias)