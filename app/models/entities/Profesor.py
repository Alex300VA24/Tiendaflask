class Profesor:
    
    def __init__(self, id, apellidos, nombres, titulo):
        self.id = id
        self.apellidos = apellidos
        self.nombre = nombres
        self.titulo = titulo
    
    def nombre_completo(self):
        return f'{self.apellidos}, {self.nombre}'
        