class Alumno:
     
     def __init__(self, nombre, nota):
          self.nombre=nombre
          self.nota=nota

     def datos(self):
          print(f"--------inicializacion de los datos------")
          print(f"el nombre del estudiante es: {self.nombre}")
          print(f"la nota del estudiante es:", self.nota)


     def resultado(self):
          if self.nota>=14:
               print(f"  El estudiante {self.nombre} paso con una nota: {self.nota}")
          else:
               print(f"  El estudiante {self.nombre} no paso su nota es inferior al minimo: {self.nota}")

r=Alumno("CARLITOS UWU", 17)
r.datos()
r.resultado()