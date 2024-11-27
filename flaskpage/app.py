from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, UABC 2024!</p>"

@app.route("/saludo")
def saludoatodos():
    return "<center>Saludos a todos los que me lean</center>"

@app.route("/about")
def sobremi():
    return "<marquee><h1> orquidea.rivera@uabc.edu.mx </h1></marquee>"

@app.route("/mineria")
def mineria():
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    # Modificación del script para adaptarlo al archivo Excel proporcionado
    # Cargar el archivo Excel y la hoja "Principal"
    data_excel = pd.ExcelFile('Copia de bourdain_travel_places1.xlsx')
    data = data_excel.parse("Principal")

    # Limpieza y preparación básica de datos
    data = data[['show', 'season', 'ep', 'city_or_area (codigo postal)', 'did_he_like_it']]
    data = data.rename(columns={
        'city_or_area (codigo postal)': 'city_or_area',
        'did_he_like_it': 'liked'
    })

    # Asegurar que las columnas tienen los tipos correctos
    data['liked'] = data['liked'].astype('int')  # Convertir "liked" a entero si no lo es

    # Análisis básico: Lugares visitados por temporada
    places_per_season = data.groupby('season').size()

    # Visualización: Lugares visitados por temporada
    plt.figure(figsize=(10, 6))
    places_per_season.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Cantidad de Lugares Visitados por Temporada', fontsize=14)
    plt.xlabel('Temporada', fontsize=12)
    plt.ylabel('Cantidad de Lugares', fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    # Análisis: Porcentaje de lugares que le gustaron
    liked_percentage = data['liked'].value_counts(normalize=True) * 100

    # Visualización: Porcentaje de lugares que le gustaron o no
    plt.figure(figsize=(8, 6))
    liked_percentage.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral'], labels=['Sí', 'No'],
                          startangle=90)
    plt.title('Porcentaje de Lugares que le Gustaron a Bourdain', fontsize=14)
    plt.ylabel('')
    plt.show()
    plt.savefig('C:/Users/2177/datapy/flaskpage/static/images/grafica.png')

    # Mostrar la gráfica
    plt.show()
    return render_template("grafica.html")

@app.route("/grafica")
def grafica():
    import pandas as pd
    import matplotlib.pyplot as plt

    # Cargar el archivo Excel
    archivo_excel = 'C:/Users/2177/datapy/flaskpage/NASCAR.xlsx'  # Cambia esto si el archivo está en otra ubicación
    df = pd.read_excel(archivo_excel)

    # 1. Cantidad total de puntos por cada fabricante
    points_by_manufacturer = df.groupby('MFR')['Points'].sum()

    # 2. Piloto con el mayor puntaje acumulado en la temporada
    top_driver = df.loc[df['Acumulado'].idxmax()]

    # 3. Promedio de puntos obtenidos por los pilotos
    average_points = df['Points'].mean()

    # 4. Cantidad total de puntos por piloto
    points_by_driver = df.groupby('Driver')['Points'].sum()

    # 5. Número de pilotos diferentes que han ganado al menos una carrera
    drivers_with_wins = df[df['Wins'] > 0]['Driver'].nunique()

    # Mostrar resultados calculados
    print("Cantidad total de puntos por fabricante:\n", points_by_manufacturer)
    print("\nPiloto con el mayor puntaje acumulado en la temporada:\n", top_driver)
    print("\nPromedio de puntos obtenidos por los pilotos:\n", average_points)
    print("\nCantidad total de puntos por piloto:\n", points_by_driver)
    print("\nNúmero de pilotos diferentes que han ganado al menos una carrera:\n", drivers_with_wins)

    # Graficar resultados

    # Configuración de subgráficas
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Análisis de Puntos de Pilotos NASCAR', fontsize=18)

    # Gráfica de puntos por fabricante
    axs[0, 0].bar(points_by_manufacturer.index, points_by_manufacturer.values, color='skyblue')
    axs[0, 0].set_title('Cantidad Total de Puntos por Fabricante')
    axs[0, 0].set_xlabel('Fabricante')
    axs[0, 0].set_ylabel('Total de Puntos')

    # Gráfica de puntos por piloto
    axs[0, 1].bar(points_by_driver.index, points_by_driver.values, color='salmon')
    axs[0, 1].set_title('Cantidad Total de Puntos por Piloto')
    axs[0, 1].set_xlabel('Piloto')
    axs[0, 1].set_ylabel('Total de Puntos')
    axs[0, 1].tick_params(axis='x', rotation=45)

    # Gráfica de promedio de puntos por piloto (texto)
    axs[1, 0].text(0.5, 0.5, f'Promedio de Puntos por Piloto: {average_points:.2f}',
                   ha='center', va='center', fontsize=14)
    axs[1, 0].set_axis_off()  # Ocultar ejes

    # Gráfica de número de pilotos con al menos una victoria (texto)
    axs[1, 1].text(0.5, 0.5, f'Número de Pilotos con al Menos una Victoria: {drivers_with_wins}',
                   ha='center', va='center', fontsize=14)
    axs[1, 1].set_axis_off()  # Ocultar ejes

    # Ajuste de diseño
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Guardar la grafica en un archivo (En este caso, PNG)
    plt.savefig('C:/Users/2177/datapy/flaskpage/static/images/grafica.png')

    # Mostrar la gráfica
    plt.show()
    return render_template("grafica.html")



