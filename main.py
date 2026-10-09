# Sistema de calificaciones

nombres = []
calificaciones = []

# Registrar los datos de 5 estudiantes
def registrar_estudiantes():
    for i in range(5):
        nombre = input("Nombre del estudiante " + str(i + 1) + ": ")
        while nombre.strip() == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Nombre del estudiante " + str(i + 1) + ": ")

        nombres.append(nombre)
        
        while True:
            try:
                nota = int(input("Calificación de " + nombre + ": "))
                if 0 <= nota <= 100:
                    calificaciones.append(nota)
                    break
                print("La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Debes introducir un número entero.")


# Mostrar las calificaciones
def mostrar_calificaciones():
    print("\nCalificaciones:")
    for i in range(len(nombres)):
        print(nombres[i], "-", calificaciones[i])


# Mostrar el resumen de las notas
def mostrar_resumen():
    suma = 0
    aprobados = 0
    reprobados = 0

    for nota in calificaciones:
        suma += nota
        if nota >= 70:
            aprobados += 1
        else:
            reprobados += 1

    print("\nPromedio:", suma / len(calificaciones))
    print("Más alta:", max(calificaciones))
    print("Más baja:", min(calificaciones))
    print("Aprobados:", aprobados)
    print("Reprobados:", reprobados)


# Modificar una calificación
def modificar_calificacion():
    print("\nEstudiantes:")

    for i in range(len(nombres)):
        print(i, "-", nombres[i], "-", calificaciones[i])

    while True:
        try:
            posicion = int(input(
                "\nPosición del estudiante a modificar (0 a 4): "
            ))

            if 0 <= posicion < len(calificaciones):
                break

            print("La posición debe estar entre 0 y 4.")

        except ValueError:
            print("Debes introducir un número entero.")

    print("\nEstudiante seleccionado:", nombres[posicion])
    print("Calificación actual:", calificaciones[posicion])

    while True:
        try:
            nueva = int(input("Nueva calificación: "))

            if 0 <= nueva <= 100:
                calificaciones[posicion] = nueva
                print("\nCalificación modificada correctamente.")
                print("Estudiante:", nombres[posicion])
                print("Nueva calificación:", calificaciones[posicion])
                break

            print("La calificación debe estar entre 0 y 100.")

        except ValueError:
            print("Debes introducir un número entero.")

# Programa principal
registrar_estudiantes()

mostrar_calificaciones()

print("\nPrimer estudiante:", nombres[0], "-", calificaciones[0])

mostrar_resumen()

modificar_calificacion()

print("\nCalificaciones actualizadas:")
mostrar_calificaciones()

mostrar_resumen()