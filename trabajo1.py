nombre1=input("Ingrese el primer nombre del alumno: ")
nombre2=input("Ingrese el segundo nombre del alumno: ")
nombre3=input("Ingrese el tercer nombre del alumno (presione Enter si no tiene): ")
apellido1=input("Ingrese el primer apellido del alumno: ")
apellido2=input("Ingrese el segundo apellido del alumno: ")
nombrecompleto=f"{nombre1} {nombre2} {nombre3} {apellido1} {apellido2}".strip()

asignaturas=[
    "Artes Visuales",
    "Ciencias Naturales",
    "Educacion Fisica y Salud",
    "Historia Geografia y Ciencias Sociales",
    "Ingles",
    "Lenguaje y Comunicacion",
    "Matematicas",
    "Musica"
]
resultados={}
for asignatura in asignaturas:
    notas=[]
    for i in range(4):
        while True:
            try:
                nota=float(input(f"Ingrese la nota {i+1} de {asignatura} (entre 2.0 y 7.0): "))
                if 2.0 <= nota <= 7.0:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 2.0 y 7.0. Intentelo de nuevo.")
            except ValueError:
                print("Valor invalido. Por favor ingrese un numero.")
    promedio=sum(notas) / len(notas)
    resultados[asignatura]=promedio
print("\nResultados:")
for asignatura, promedio in resultados.items():
    print(f"{asignatura}: {promedio:.2f}")
while True:
    try:
        asistencia=float(input("Ingrese el porcentaje de asistencia del alumno: "))
        if 0 <= asistencia <= 100:
            if asistencia <= 69:
                print(f"{nombrecompleto} no pasa el curso debido a baja asistencia.")
            else:
                print(f"{nombrecompleto} pasa el curso.")
            break
        else:
            print("La asistencia debe estar entre 0 y 100. Intentelo de nuevo.")
    except ValueError:
        print("Valor invalido. Por favor ingrese un numero.")