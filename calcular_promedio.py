def calcular_promedio(cantidad_alumnos):    
    notas = 0
    for nro_alumno in range(cantidad_alumnos):
        notas += float(input(f"Ingrese la nota del alumno nro {nro_alumno + 1}: "))
    promedio = notas / cantidad_alumnos
    return promedio


cantidad_alumnos = int(input("Ingrese la cantidad de alumnos para calcular el promedio: "))
print(f"El promedio calculado para los alumnos es de: {calcular_promedio(cantidad_alumnos)}")
