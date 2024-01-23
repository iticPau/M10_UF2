import json
def crearguardar_json():
    # Crear una lista de diccionarios con la información de los libros
    libros = [
        {"Titulo": "Superman", "Portada": "SupermanCover", "Año": 2022, "Paginas": 200},
        {"Titulo": "Batman", "Portada": "BatmanCover", "Año": 2021, "Paginas": 150},
        {"Titulo": "Spiderman", "Portada": "SpidermanCover", "Año": 2020, "Paginas": 300},
        {"Titulo": "Xmen", "Portada": "XMenCover", "Año": 2019, "Paginas": 180},
    ]
    Data = {"Books": libros}
    Json_string = json.dumps(Data, indent=2)
    print("ARXIVO JSON  :")
    print(Json_string)
    with open("Libros.json", "w") as archivo:
        json.dump(Data, archivo, indent=2)
def main():
    crearguardar_json()
if __name__ == "__main__":
    main()