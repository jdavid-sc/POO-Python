class Estudiante:
   def __init__(self, nombre, edad, grado):
       self.nombre = nombre
       self.edad = edad 
       self.grado = grado
       
   def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando')
        
nombre = input("Ingrese su nombre por favor : ")
edad = input("Ingrese su eda por favor : ")
grado = input("Ingrese su grado por favor : ")   
estudiar = input("Quieres estudiar escribe estudiar: ")


while estudiar.lower() != "estudiar":
    estudiar = input("Quieres estudiar escribe estudiar: ")
    print(estudiar)   
    

estudiante1 = Estudiante(nombre, edad, grado)
print(f"""
DATOS DEL ESTUDIANTE
NOMBRE: {nombre}
EDAD: {edad}
GRADO: {grado}
""")
estudiante1.estudiar()