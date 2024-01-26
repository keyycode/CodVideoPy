class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
        
    def estudiar(self):
        print(f'{self.nombre} esta estudiando')
       
nombre=input("Escriba su nombre\n")
edad=input("Escriba su edad\n")
grado= input("Escriba su grado\n")

estudiante= Estudiante(nombre,edad,grado)

print(f"\nDatos del estudiante:\n\n{estudiante.nombre}\n{estudiante.edad}\n{estudiante.grado}")
estudiante.estudiar()




