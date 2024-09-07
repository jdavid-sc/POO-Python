class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        ("Hola estoy hlando ")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, materias):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.materias = materias
        
class PersonaNormal(Persona, Estudiante):
    def __init__(self, nombre, edad, nacionalidad, identicicion ):
        super().__init__(nombre, edad, nacionalidad)
        self.identificacion = identicicion