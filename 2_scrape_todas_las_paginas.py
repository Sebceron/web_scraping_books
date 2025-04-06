import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
libros = []


for pagina in range(1, 51):  # Hay 50 páginas
    print(f"Scrapeando página {pagina}...")
    # Construir la URL de la página
    url = base_url.format(pagina)
    # Hacer la solicitud HTTP
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code != 200:
        # Manejar el error de la solicitud
        print(f"Error al acceder a la página {pagina}")
        continue
    
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    

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
    
    time.sleep(1)  # Para no parecer robot agresivo

# Guardar todos los libros en un solo CSV
df = pd.DataFrame(libros)
df.to_csv('libros_todas_las_paginas.csv', index=False)
print("Todos los datos fueron guardados exitosamente.")
