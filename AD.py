#manejo de datos
#lista
#obtener la posision de un dato en un arreglo
"""
datos = [35,4,5,455,455,7545,4455]
print (datos[5])

#agregar datos
datos.append(7)
print (datos)
#Cambiar un valor de datos
datos[3]=6
print (datos)
sumary_line

"""

#----------------------------------------------------------------
import pandas as pd
#Crear un data frame(arreglo de datos)
datos = {
    'Nombre':['Andres', 'Carlos', 'Maria', 'Juan'],
    'Edad':[20,21,25,12],
    'Nota':[3.5,3.0,4.5,3.9]
}
df=pd.DataFrame(datos)
#print(df)

#cual es el promedio de la edad
media=df['Edad'].mean()
#print(media)

#Cual es la nota promedio
media_cal=df['Nota'].mean()
print(media_cal)
#calificación >4
cal_4 = df[df['Nota']>4]
print(cal_4)