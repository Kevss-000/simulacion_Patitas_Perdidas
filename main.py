import pandas as pd

from utils.simulacion_usuarios import generar_usuarios
from notebook.limpieza_usuarios import limpiar_usuarios
from notebook.limpieza_ubicaciones import limpiar_ubicaciones
from utils.simulacion_ubicaciones import generar_ubicaciones
from utils.simulacion_mascotas import generar_mascotas
from notebook.limpieza_mascotas import limpiar_mascotas
from utils.simulacion_reportes import generar_reportes
from notebook.limpieza_reportes import limpiar_reportes
from utils.simulacion_imagenes import generar_imagenes
from notebook.limpieza_imagenes import limpiar_imagenes
from utils.simulacion_donaciones import generar_donaciones
from notebook.limpieza_donaciones import limpiar_donaciones
from utils.simulacion_volun import generar_volun
from notebook.limpieza_volun import limpiar_volun

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

ubicaciones=generar_ubicaciones(15)
ubicaciones=limpiar_ubicaciones(pd.DataFrame(ubicaciones))      
print(ubicaciones)

donaciones=generar_donaciones(50)
donaciones=limpiar_donaciones(pd.DataFrame(donaciones))     
print(donaciones)

volun=generar_volun(20)
volun=limpiar_volun(pd.DataFrame(volun)) 
print(volun)

