import pandas as pd

from utils.simulacion_usuarios import generar_simulacion
from notebook.limpieza_usuarios import limpiar_simulasiones
from notebook.limpieza_ubicaciones import limpiar_simulaciones
from utils.simulacion_ubicaciones import generar_ubicaciones

from notebook.limpieza_usuarios import limpiar_usuarios
from notebook.limpieza_mascotas import limpiar_mascotas
from notebook.limpieza_reportes import limpiar_reportes
from notebook.limpieza_imagenes import limpiar_imagenes

usuarios=generar_usuarios(20)
usuarios=limpiar_usuarios(pd.DataFrame(usuarios))
print(usuarios)

mascotas=generar_mascotas(30)
mascotas=limpiar_mascotas(pd.DataFrame(mascotas))
print(mascotas)

reportes=generar_reportes(25)
reportes=limpiar_reportes(pd.DataFrame(reportes))
print(reportes)

imagenes=generar_imagenes(40)
imagenes=limpiar_imagenes(pd.DataFrame(imagenes))
print(imagenes)