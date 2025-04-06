import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# URL base para las páginas de libros
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
# URL base para los detalles del libro
base_book_url = 'https://books.toscrape.com/catalogue/'

# Lista para guardar los datos
libros = []

# Iterar sobre las páginas
for pagina in range(1, 51):
    print(f"Scrapeando página {pagina}...")
    url = base_url.format(pagina)
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code != 200:
        print(f"Error en la página {pagina}")
        continue

    # Parsear el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    for libro in soup.find_all('article', class_='product_pod'):
        titulo = libro.h3.a['title']
        precio = libro.find('p', class_='price_color').text
        disponibilidad = libro.find('p', class_='instock availability').text.strip()
        
        # Obtener el enlace al detalle del libro
        relative_link = libro.h3.a['href'] 
        link_limpio = relative_link.replace('../../../', '')  # Limpiar el enlace relativo para obtener la URL completa        
        full_book_url = base_book_url + link_limpio # Construir la URL completa del libro

        # Scraping dentro del detalle del libro para obtener categoría
        detalle_response = requests.get(full_book_url) # Hacer la solicitud HTTP
        if detalle_response.status_code == 200: # Verificar si la solicitud fue exitosa
            detalle_soup = BeautifulSoup(detalle_response.text, 'html.parser') # Parsear el contenido HTML
            breadcrumb = detalle_soup.find('ul', class_='breadcrumb') # Buscar la categoría
            categoria = breadcrumb.find_all('li')[2].text.strip()  # Obtener la categoría # El índice 2 es la categoría # El índice 0 es "Home" y el índice 1 es "Books"

        else: # Si no se puede acceder a la página de detalles, asignar 'Desconocida'
            categoria = 'Desconocida' # Manejar el error de la solicitud

        # Agregar los datos a la lista
        libros.append({
            'Título': titulo,
            'Precio': precio,
            'Disponibilidad': disponibilidad,
            'Categoría': categoria,
            'URL': full_book_url 
        })

    time.sleep(1) # Para no parecer un robot agresivo

# Guardar todo en CSV
df = pd.DataFrame(libros)
df.to_csv('libros_con_categoria.csv', index=False) 
print("Scraping completado y datos guardados.")
