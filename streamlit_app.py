import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
data = pd.read_csv('IMDB-Movie-Data.csv')

# Título de la aplicación
st.title('Explorador de Películas')

# Selección de género
genre = st.sidebar.selectbox('Seleccione el género', data['Genre'].unique())
filtered_data_by_genre = data[data['Genre'].str.contains(genre)]

# Mostrar datos filtrados por género
st.write(f"Datos filtrados por género: {genre}")
st.dataframe(filtered_data_by_genre)

# Gráfico de ingresos de las películas seleccionadas con Plotly
st.write(f"Ingresos de películas de género {genre}")
fig = px.bar(filtered_data_by_genre, x='Title', y='Revenue (Millions)', title="Ingresos por Película")
st.plotly_chart(fig)

# Filtro de año
year_range = st.sidebar.slider("Seleccione el rango de años", int(data['Year'].min()), int(data['Year'].max()), (2010, 2020))
filtered_data_by_year = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]
st.write(f"Datos filtrados por año: {year_range}")
st.dataframe(filtered_data_by_year)
