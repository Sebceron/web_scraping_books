import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Lista para guardar los datos
libros = []

# Buscar todos los artículos de libros
for libro in soup.find_all('article', class_='product_pod'):
    titulo = libro.h3.a['title']
    precio = libro.find('p', class_='price_color').text
    disponibilidad = libro.find('p', class_='instock availability').text.strip()

    libros.append({
        'Título': titulo,
        'Precio': precio,
        'Disponibilidad': disponibilidad
    })

# Guardar en CSV
df = pd.DataFrame(libros)
df.to_csv('libros_pagina_1.csv', index=False)

print("Datos de la página 1 guardados correctamente.")
