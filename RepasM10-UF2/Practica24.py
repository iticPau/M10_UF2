import json
def mostrar_json():
    # Leer el JSON desde el archivo.
    with open("Libros.json", "r") as archivo:
        data = json.load(archivo)
    Json_string = json.dumps(data, indent=1)
    print("JSON leido:")
    print(Json_string)

def main():
    mostrar_json()
if __name__ == "__main__":
    main()
