import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de página
st.set_page_config(
    page_title="Dashboard de Libros",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar y limpiar datos
df = pd.read_csv('libros_con_categoria.csv', encoding='utf-8', on_bad_lines='skip')

# Limpieza avanzada de precios
df['Precio'] = df['Precio'].astype(str) # Asegurarse de que los precios son cadenas
df['Precio'] = df['Precio'].str.replace(r'[^\d.]', '', regex=True) # Eliminar caracteres no numéricos
df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce') # Convertir a numérico

# Crear columna "En Stock" para filtros
df['En Stock'] = df['Disponibilidad'].str.contains('In stock', case=False, na=False)

# Título principal
st.title("📚 Dashboard Interactivo de Libros Scrapeados")
st.markdown("Explora los datos extraídos con Web Scraping desde [books.toscrape.com](https://books.toscrape.com)")

# Sidebar: Filtros avanzados
st.sidebar.header("🎛️ Filtros")
categorias = ['Todas'] + sorted(df['Categoría'].unique().tolist())
categoria_sel = st.sidebar.selectbox("Categoría:", categorias)

rango_precio = st.sidebar.slider(
    "Rango de precios (£)",
    float(df['Precio'].min()),
    float(df['Precio'].max()),
    (float(df['Precio'].min()), float(df['Precio'].max()))
)

disponibilidad = st.sidebar.radio("Disponibilidad:", ["Todos", "Solo en stock", "Solo agotados"])

orden_precio = st.sidebar.radio("Ordenar por precio:", ["Ninguno", "Ascendente", "Descendente"])

# Aplicar filtros
if categoria_sel != 'Todas':
    df = df[df['Categoría'] == categoria_sel]

df = df[(df['Precio'] >= rango_precio[0]) & (df['Precio'] <= rango_precio[1])]

if disponibilidad == "Solo en stock":
    df = df[df['En Stock'] == True]
elif disponibilidad == "Solo agotados":
    df = df[df['En Stock'] == False]

if orden_precio == "Ascendente":
    df = df.sort_values(by='Precio', ascending=True)
elif orden_precio == "Descendente":
    df = df.sort_values(by='Precio', ascending=False)

# Métricas resumen
st.markdown("## 📊 Resumen General")
col1, col2, col3 = st.columns(3)
col1.metric("📦 Total de Libros", len(df))
col2.metric("💷 Precio Promedio", f"{df['Precio'].mean():.2f} £")
col3.metric("✅ Libros en Stock", df['En Stock'].sum())

# Gráfico de distribución de precios con Plotly
st.markdown("### 💸 Distribución Interactiva de Precios")

fig = px.histogram(
    df,
    x='Precio',
    nbins=20,
    title='Distribución de precios de libros',
    labels={'Precio': 'Precio (£)'},
    color_discrete_sequence=['indigo']
)

fig.update_layout(
    bargap=0.1,
    template='plotly_white',
    xaxis_title='Precio (£)',
    yaxis_title='Cantidad de libros'
)

st.plotly_chart(fig, use_container_width=True)



# Tabla de resultados
st.markdown("### 📚 Tabla de libros filtrados")
st.dataframe(df[['Título', 'Precio', 'Categoría', 'Disponibilidad', 'URL']].reset_index(drop=True))

# Footer
st.markdown("---")
st.caption("Desarrollado por Juan Sebastián Jiménez Cerón · Proyecto de portafolio en Python · 2025")



"""run dashboard: streamlit run dashboard.py""" # Ejecutar el script en la terminal
