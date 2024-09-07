class Celular:
    def __init__(self, marca, modelo, camara) :
        self.marca  = marca
        self.modelo = modelo
        self.camara = camara
        
    def hacerLlamada(self):
        print(f'Estas haciendo una llamada desde tu {self.marca}')

celular1 = Celular("apple", "A21", "88MP")
celular2 = Celular("SAMSUNG", "A25", "98MP")
celular1.hacerLlamada()
print(celular1.camara)