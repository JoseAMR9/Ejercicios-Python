import os
class Estudiante:
    def __init__(self, nombre):
            self.__nombre = nombre
            self.__nota = []
    
    def agregar_nota(self, nota):
        self.__nota.append(nota)
    def promedio(self):
        total = 0
        i = 0
        for prom in self.__nota:
            total += prom
            i += 1
        if i == 0:
            return 0
        return total / i
    def mostrar_info(self):
        print(f"\nNombre: {self.__nombre}")
        print(f"Notas: {self.__nota}")
        print(f"Promedio: {self.promedio():.2f}")
    
    def get_nombre(self):
        return self.__nombre

def clean():
    os.system("cls")
def pause():
    input("\nPresione cualquier tecla para continuar...")

estudiantes = []
while True:
    clean()
    print("1.- Agregar estudiante")
    print("2.- Buscar estudiante")
    print("3.- Mostrar estudiante con mayor promedio")
    print("0.- Salir")
    try:
        op = int(input("Elija una opcion: "))
    except:
        print("Invalid option")
        pause()
        continue
    match(op):
        case 1:
            clean()
            nombre = input("\nNombre del estudiante: ")

            existe = False
            for estudiante in estudiantes:
                if estudiante.get_nombre == nombre:
                    existe = True
                    break
            
            if existe == True:
                print("El estudiante ya existe")
            else:
                nuevo_estudiante = Estudiante(nombre)
                estudiantes.append(nuevo_estudiante)

            while True:
                try:
                    nota = float(input("Ingrese la nota: "))

                    if nota < 0 or nota > 20:
                        raise ValueError("\nNota invalida")
                    
                    nuevo_estudiante.agregar_nota(nota)
                except ValueError as e:
                    print(e)
                rpta = input("\nPresione (s) para salir, ENTER para continuar: ")
                if rpta == "s":
                    break
        case 2: 
            nombre = input("\nIngrese el nombre del estudiante: ")
            encontrado = False
            for estudiante in estudiantes:
                if estudiante.get_nombre() == nombre:
                    estudiante.mostrar_info()
                    encontrado = True
                    break
            if encontrado == False:
                print(f"\nEstudiante {nombre} no encontrado")
            pause()
        case 3:
            if len(estudiantes) == 0:
                print("\nNo hay estudiantes registrados")
                pause()
                continue

            mejor_estudiante = estudiantes[0]
            for estudiante in estudiantes:
                if estudiante.promedio() > mejor_estudiante.promedio():
                    mejor_estudiante = estudiante
            
            print(f"El estudiante con mayor promedio es: {mejor_estudiante.get_nombre()}")
            pause()
        case 0:
            break


