import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

#Importar datos

Employee_data = pd.read_csv('Employee_data.csv')
st.set_page_config(layout="wide")

# •	Código que permita desplegar el logotipo de la empresa en la aplicación web.
image= Image.open('logo_empresa.png')
st.image(image)

# •	Código que contenga las instrucciones para el despliegue de un título y una breve descripción de la aplicación web.

'''
# Análisis de Desempeño de Empleados


Esta aplicación web permite analizar el desempeño de los empleados en función de diversos factores como género, estado civil, horas trabajadas y salario.
'''

# •	Código que permita desplegar un control para seleccionar el género del empleado.
genero = st.sidebar.selectbox(
    "Seleccione el género del empleado:", Employee_data['gender'].unique())
st.sidebar.write(f"Has seleccionado: {genero!r}")
   

# •	Código que permita desplegar un control para seleccionar un rango del puntaje de desempeño del empleado.
optionals = st.sidebar.expander("Seleccione el rango del puntaje de desempeño del empleado", True)

performance_score = optionals.slider(
    "Rango del puntaje de desempeño:",
    min_value=int(Employee_data['performance_score'].min()),
    max_value=int(Employee_data['performance_score'].max()), 
    value=(int(Employee_data['performance_score'].min()), int(Employee_data['performance_score'].max()))
)

# •	Código que permita desplegar un control para seleccionar el estado civil del empleado.
marital_status = st.sidebar.selectbox(
    "Seleccione el estado civil del empleado:", Employee_data['marital_status'].unique())   
st.sidebar.write(f"Has seleccionado: {marital_status!r}")

# •	Código que permita mostrar un gráfico en donde se visualice la distribución de los puntajes de desempeño.
figDPD= px.histogram(Employee_data, x='performance_score', nbins=4, title='Distribución de Puntajes de Desempeño',color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(figDPD)

# •	Código que permita mostrar un gráfico en donde se visualice el promedio de horas trabajadas por el género del empleado.
auxgender_hours = Employee_data.groupby('gender')['average_work_hours'].mean().reset_index()
figHTG= px.bar(auxgender_hours, x='gender', y='average_work_hours', title='Promedio de Horas Trabajadas por Género', color_discrete_sequence=px.colors.qualitative.T10)
st.plotly_chart(figHTG)

# •	Código que permita mostrar un gráfico en donde se visualice la edad de los empleados con respecto al salario de los mismo. scatter plot
figES= px.scatter(Employee_data, x='age', y='salary', title='Edad vs Salario', color='gender', color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(figES)

# •	Código que permita mostrar un gráfico en donde se visualice la relación del promedio de horas trabajadas versus el puntaje de desempeño. scatter plot
figHD= px.scatter(Employee_data, x='average_work_hours', y='performance_score', title='Promedio de Horas Trabajadas vs Puntaje de Desempeño', color='gender', color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(figHD)

# •	Código que permita desplegar una conclusión sobre el análisis mostrado en la aplicación web.
'''
# Conclusión

Las gráficas mostradas permiten observar que:
1. El desempeño de los empleados está concentrado en la calificación 3
2. El promedio de horas trabajadas varía según el género del empleado.
3. Existe una relación entre la edad y el salario de los empleados.
4. El puntaje de desempeño está relacionado con las horas trabajadas.

Estos análisis ayudan a identificar patrones en el desempeño laboral de los empleados.
'''