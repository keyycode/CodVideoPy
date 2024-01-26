class Animal:
    def comer(self):
        print("El animal esta comiendo")
        
class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
        
    def comer(self):
        print("El ave esta comiendo")
        
        
class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")
     
    def comer(self):
        print("El mamifero esta comiendo")
        
class Murcielago(Mamifero,Ave):
    pass

murcielago= Murcielago()
murcielago.amamantar()
murcielago.volar()
murcielago.comer()


