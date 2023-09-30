#Diccionario de alumnos y edades
estudiantes = {}

#Inicio de programa
print('''Bienvenido al programa de inscripción de estudiantes.
Ingrese los nombres y las edades de cada alumno para registrar sus datos.
Al momento de querer conocer la lista total, ingrese un asterisco (*) en el apartado "Nombre del estudiante"
para conocer la lista.''')
print()

#Ingreso de datos
while True:
    estudiante = str(input(f"Nombre del estudiante: "))
    if estudiante == "*":
        print()
        print(f"Estudiantes mayores de edad:")
        print()
        for nombres, edades in estudiantes.items():
            if edades >= 18:
                print(f"Estudiante: {nombres}. Edad: {edades}")
        print()
        print(f"Estudiantes menores de edad:")
        print()
        for nombres, edades in estudiantes.items():
            if edades < 18:
                print(f"Estudiante: {nombres}. Edad: {edades}")
        break

    edad = int(input(f"Edad: "))

    estudiantes[estudiante] = edad