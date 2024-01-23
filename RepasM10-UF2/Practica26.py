import json

class Usuario:
    def __init__(self, nombre, apellido, edad, correo, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_edad(self):
        return self.edad

    def get_correo(self):
        return self.correo

    def get_telefono(self):
        return self.telefono

    def get_direccion(self):
        return self.direccion

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_edad(self, edad):
        self.edad = edad

    def set_correo(self, correo):
        self.correo = correo

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_direccion(self, direccion):
        self.direccion = direccion

    def saludo(self):
        print(f"Nombre: {self.nombre}, apellidos: {self.apellido} y edad {self.edad} años.")
        print(f"Email: {self.correo}")
        print(f"Telefono: {self.telefono}")
        print(f"Direccion: {self.direccion}")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "email": self.correo,
            "telefono": self.telefono,
            "direccion": self.direccion
        }
usuario = Usuario("Pau", "Insa", 19, "pauinsa@ejemplo.com", "123456789", "Poble sec")
usuario.saludo()
print(json.dumps(usuario.to_dict(), indent=2))
