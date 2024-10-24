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



#----------------------------------------------------------------
import pandas as pd
#Crear un data frame(arreglo de datos)
datos = {
    'Nombre':['Andres', 'Carlos', 'Maria', 'Juan', 'Jaime'],
    'Edad':[20,21,25,12,13],
    'Carrera':['Sitemas','Electronica', 'Electronica','Sistemas', 'Sistemas']    
}
"""
"""
#Imputacioón de datos
import pandas as pd
datos = {
    'Nombre':['Andres', 'Carlos', 'Maria', 'Juan', 'Jaime'],
    'Edad':[20,None,25,None,13],
    'Carrera':['Sitemas','Electronica', 'Electronica','Sistemas', 'Sistemas']    
}

#rellenar datos faltantes .fillna con la media de datos
dfnull=pd.DataFrame(datos)
dfnull['Edad'] = dfnull ['Edad'].fillna (dfnull['Edad'].mean())
print(dfnull)
"""
import pandas as pd
df=pd.read_csv('http://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(df.head())

#pERSONAS QUE SOBREVIVIERON
survivor=df[df['Survived']== 1]
print(survivor)
#Personas que sobrevivieron mayor de 60años
survivor_60=df[(df['Survived']== 1)&(df['Age']>60)]
print(survivor_60)

#Promedio de muertos
muertos=df[df['Survived']== 0]
print(muertos)

#Grafica de sobrevivientes por genero
import matplotlib.pyplot as plt
import seaborn as sbn 

sbn.countplot(x='Sex', hue='Survived', data=df)
plt.title('Grafico de sobrevivencia vs edad')
plt.show()
"""
#Base de datos sin valores nulos (dropna)
dfnull=pd.DataFrame(datos)
df_sin_nulos=dfnull.dropna(subset=['Edad'])
print(df_sin_nulos)

"""

"""

dfnull=pd.DataFrame(datos)
#bASE DE DATOS SIN VALORES NULOS
df_sin_nulos=dfnull.dropna(subset=['Edad'])
print(df_sin_nulos)


"""

#----------------------------------------------------------------
#Estudiantes de sistemas de mas de 21 años de edad
#sis_edad=df(df['Carrera']=='Sistemas'])&(df['edad']>21)]

#Imprimir los estudiantes de sistemas
#df=pd.DataFrame(datos)
#Sistemas = df[df['Carrera']=='Sistemas']
#print (Sistemas)
              
#----------------------------------------------------------------
#Promedio de la edad
#df=pd.DataFrame(datos)
#promedio=df['Edad'].mean()
#print(promedio)
#----------------------------------------------------------------
#print(df['Nombre'])
#print(df)
#----------------------------------------------------------------
#cual es el promedio de la edad
#media=df['Edad'].mean()
#print(media)

#----------------------------------------------------------------
#Cual es la nota promedio
#media_cal=df['Nota'].mean()
#print(media_cal)
#calificación >4
#cal_4 = df[df['Nota']>4]
#print(cal_4)
