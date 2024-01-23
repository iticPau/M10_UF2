import json
class Vehiculo:
    def __init__(self, marca, modelo, año_fabricacion, color, num_puertas, velocidad_max):
        self.marca = marca
        self.modelo = modelo
        self.año_fabricacion = año_fabricacion
        self.color = color
        self.num_puertas = num_puertas
        self.velocidad_max = velocidad_max

    # Getters
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_año_fabricacion(self):
        return self.año_fabricacion

    def get_color(self):
        return self.color

    def get_num_puertas(self):
        return self.num_puertas

    def get_velocidad_max(self):
        return self.velocidad_max

    # Setters
    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_año_fabricacion(self, año_fabricacion):
        self.año_fabricacion = año_fabricacion

    def set_color(self, color):
        self.color = color

    def set_num_puertas(self, num_puertas):
        self.num_puertas = num_puertas

    def set_velocidad_max(self, velocidad_max):
        self.velocidad_max = velocidad_max

    def parts(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año de fabricacion: {self.año_fabricacion}")
        print(f"Color: {self.color}")
        print(f"Numero de puertas: {self.num_puertas}")
        print(f"Velocidad maxima: {self.velocidad_max}")
    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "año_fabricacion": self.año_fabricacion,
            "color": self.color,
            "num_puertas": self.num_puertas,
            "velocidad_max": self.velocidad_max
        }
vehiculo = Vehiculo("Lamborguini", "Aventador", 2020, "Rojo", 2, 310)
vehiculo.parts()
print(json.dumps(vehiculo.to_dict(), indent=2))