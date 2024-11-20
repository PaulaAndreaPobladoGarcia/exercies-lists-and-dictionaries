#Ejercicio 7
#Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
#| Lista de la compra |        |
#| :----------------- | -----: |
#| Artículo 1         | Precio |
#| Artículo 2         | Precio |
#| Artículo 3         | Precio |
#| …                  |      … |
#| Total              |  Coste |

import json

def exericisesSeven():
    archivo = "exercisesFourDict"
    try:
        with open(archivo, "r") as f:
            cesta = json.load(f)
    except FileNotFoundError:
        cesta = {}  

    while True:
        articulo = input("Introduce el nombre del artículo: ")
        
        try:
            precio = float(input(f"Introduce el precio del {articulo}: "))
        except ValueError:
            print("Por favor, introduce un precio válido.")
            continue

