class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def imprimirDatosPersona(self):
        print(f"Datos de la persona:\nNombre:{self.nombre}\nEdad:{self.edad}")
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado
        
    def imprimirDatosEstudiante(self):
        print(f"Grado:{self.grado}")
        

estudiante=Estudiante("Keila",27,"Segundo Semestre")
estudiante.imprimirDatosPersona()
estudiante.imprimirDatosEstudiante()
        
        
        
     
    


