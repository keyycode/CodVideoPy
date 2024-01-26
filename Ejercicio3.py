class Personaje():
    def __init__(self,nombre, fuerza,velocidad):
        self.nombre=nombre
        self.fuerza=fuerza
        self.velocidad=velocidad
        
    def __repr__(self) -> str:
        return f"{self.nombre}(Fuerza:{self.fuerza},Velocidad={self.velocidad})"
    
    def __add__(self,otroPersonaje):
        nuevoNombre= f"{self.nombre}-{otroPersonaje.nombre}"
        nuevaFuerza=round(((self.fuerza+otroPersonaje.fuerza)/2)**1.5)
        nuevaVelocidad=round(((self.velocidad+otroPersonaje.velocidad)/2)**1.5)
        return Personaje(nuevoNombre,nuevaFuerza,nuevaVelocidad)
    


goku=Personaje("Goku",100,100)
vegeta=Personaje("Vegeta",99,99)
goten=Personaje("Goten",99,98)
thrunks= Personaje("Thrunks",99,99)
gogeta= goku +vegeta
gotenks=goten + thrunks
print(gogeta)
print(gotenks)
