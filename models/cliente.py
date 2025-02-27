class Cliente:
    def __init__(self, nombre, email, apellido, dni):
        self.nombre = nombre
        self.email = email
        self.apellido = apellido
        self.dni = dni

    def __repr__(self):
        return f"Cliente( nombre='{self.nombre}', email='{self.email}', apellido='{self.apellido}', dni='{self.dni}')"