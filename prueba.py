import random

# Parámetros para el generador de instancias
n = 10  # Número de asignaturas
m = 5   # Número de salas
d = 5   # Días de la semana
h = 7   # Bloques horarios por día

# Generación de la prioridad de las asignaturas
def generar_prioridades(n):
    prioridades = []
    for i in range(n):
        if random.random() < 0.2:  # Aproximadamente el 20% son indispensables
            prioridades.append(random.randint(6, 10))  # Prioridad entre 6 y 10
        else:
            prioridades.append(random.randint(1, 5))  # Prioridad entre 1 y 5
    return prioridades

# Generación del número de bloques requeridos por asignatura
def generar_bloques_asignaturas(n):
    bloques = []
    for i in range(n):
        bloques.append(random.choices([1, 2], weights=[0.65, 0.35])[0])  # 65% un bloque, 35% dos bloques
    return bloques

# Generación de las capacidades de las salas
def generar_capacidades_salas(m):
    return [random.randint(20, 45) for _ in range(m)]

# Generación del interés en las asignaturas
def generar_interes_asignaturas(n):
    return [random.randint(10, 40) for _ in range(n)]

# Generación de la disponibilidad de bloques para cada profesor
def generar_disponibilidad_profesores(n, d, h):
    return [[[random.randint(0, 1) for _ in range(h)] for _ in range(d)] for _ in range(n)]

# Exportar datos para MiniZinc
def exportar_datos_mzn(prioridades, bloques_asignaturas, capacidades_salas, interes_asignaturas, disponibilidad_profesores):
    with open('instancia2.dzn', 'w') as f:
        f.write(f"n = {n};\n")
        f.write(f"m = {m};\n")
        f.write(f"h = {h};\n")
        f.write(f"d = {d};\n")
        f.write("p = " + str(prioridades) + ";\n")
        f.write("b = " + str(bloques_asignaturas) + ";\n")
        f.write("c = " + str(capacidades_salas) + ";\n")
        f.write("i = " + str(interes_asignaturas) + ";\n")
        f.write("r = " + str(disponibilidad_profesores) + ";\n")


# Generar instancias
prioridades = generar_prioridades(n)
bloques_asignaturas = generar_bloques_asignaturas(n)
capacidades_salas = generar_capacidades_salas(m)
interes_asignaturas = generar_interes_asignaturas(n)
disponibilidad_profesores = generar_disponibilidad_profesores(n, d, h)

# Mostrar la instancia generada
print("Prioridades:", prioridades)
print("Bloques requeridos por asignatura:", bloques_asignaturas)
print("Capacidades de salas:", capacidades_salas)
print("Interés en asignaturas:", interes_asignaturas)
print("Disponibilidad de profesores:", disponibilidad_profesores)

exportar_datos_mzn(prioridades, bloques_asignaturas, capacidades_salas, interes_asignaturas, disponibilidad_profesores)







