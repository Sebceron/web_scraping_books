# 📚 Web Scraping de Libros - Proyecto de Portafolio

Este es un proyecto de práctica profesional de Web Scraping utilizando Python. El objetivo es extraer información de libros desde el sitio [books.toscrape.com](https://books.toscrape.com), que está diseñado específicamente para practicar scraping.

---

## 🎯 Objetivo del Proyecto

- Extraer **título**, **precio**, **disponibilidad**, **categoría** y **URL** de cada libro.
- Recolectar datos desde las **50 páginas** del sitio.
- Guardar los resultados en un archivo CSV para su posterior análisis.

---

## 🛠️ Tecnologías Usadas

- `Python 3`
- `requests`
- `BeautifulSoup4`
- `pandas`
- `time`

---

## 📁 Estructura del Proyecto

web_scraping_books/ 
├── 1_scrape_pagina_unica.py 
├── 2_scrape_todas_las_paginas.py 
├── 3_scrape_detalles_categoria.py 
├── libros_con_categoria.csv
├── dashboard.py
└── README.md

---

## 🧪 ¿Cómo correr el proyecto?

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/web_scraping_books.git
cd web_scraping_books

2. Instala las librerías necesarias:
pip install requests beautifulsoup4 pandas

3. Ejecuta el script completo:
python 3_scrape_detalles_categoria.py



## 🧩 Visualización Interactiva

También se desarrolló un mini dashboard en **Streamlit** para explorar los datos de forma visual:

### 🎛️ Funcionalidades del dashboard:
- Filtro por categoría
- Filtro por rango de precios
- Filtro por disponibilidad (en stock / agotado)
- Orden ascendente/descendente por precio
- Visualización de histograma de precios
- Tabla interactiva de libros filtrados

### 🖥️ Cómo correrlo:

```bash
streamlit run dashboard.py


- `Juan_Sebastan_Jimenez_Ceron`
- `sebceron` 