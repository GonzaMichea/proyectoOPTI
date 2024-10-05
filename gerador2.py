import random

def generar_asignaturas_b1(num_asignaturas):
    prioridades = []
    bloques_necesarios = []
    num_alumnos = []
    for i in range(num_asignaturas):
        es_indispensable = (i % 5 == 0)  # 1 de cada 5 asignaturas es indispensable
        prioridad = random.randint(6, 10) if es_indispensable else random.randint(1, 5)
        prioridades.append(prioridad)
        
        # El 65% tendrá 1 bloque, el 35% tendrá 2 bloques
        bloque = 1 if random.random() < 0.65 else 2
        bloques_necesarios.append(bloque)
        
        alumnos = random.randint(10, 40)  # Cantidad de alumnos entre 10 y 40
        num_alumnos.append(alumnos)
        
    return prioridades, bloques_necesarios, num_alumnos

def generar_salas_a1(num_salas):
    capacidades = []
    for i in range(num_salas):
        capacidad = random.randint(20, 45)  # Capacidad entre 20 y 45
        capacidades.append(capacidad)
    return capacidades

def generar_restricciones_profesor(num_profesores, min_bloques=7, max_bloques=21):
    restricciones = []
    total_bloques = 35  # 7 bloques por día * 5 días
    for profesor in range(num_profesores):
        num_bloques_restringidos = random.randint(min_bloques, max_bloques)
        bloques_restringidos = random.sample(range(total_bloques), num_bloques_restringidos)
        restricciones.append(bloques_restringidos)
    return restricciones

def guardar_instancia_en_txt(num_asignaturas, num_salas, num_profesores, num_bloques,
                             prioridades, bloques_necesarios, num_alumnos, capacidades, restricciones,
                             nombre_archivo="instancia.txt"):
    with open(nombre_archivo, "w") as f:
        f.write(f"num_asignaturas = {num_asignaturas};\n")
        f.write(f"num_salas = {num_salas};\n")
        f.write(f"num_profesores = {num_profesores};\n")
        f.write(f"num_bloques = {num_bloques};\n\n")
        
        f.write("prioridad = [")
        f.write(", ".join(str(p) for p in prioridades))
        f.write("];\n")
        
        f.write("R = [")
        f.write(", ".join(str(b) for b in bloques_necesarios))
        f.write("];\n")
        
        f.write("num_alumnos = [")
        f.write(", ".join(str(n) for n in num_alumnos))
        f.write("];\n")
        
        f.write("capacidad = [")
        f.write(", ".join(str(c) for c in capacidades))
        f.write("];\n")
        
        f.write("restricciones = [\n")
        for restriccion in restricciones:
            bloques_str = ", ".join(str(b) for b in restriccion)
            f.write(f"  {{{bloques_str}}},\n")
        f.write("];\n")

# Generar instancias específicas
num_asignaturas = 10  # Puedes cambiar este valor a 43 si lo necesitas
num_salas = 3
num_profesores = 10
num_bloques = 35  # 7 bloques por día * 5 días

prioridades, bloques_necesarios, num_alumnos = generar_asignaturas_b1(num_asignaturas)
capacidades = generar_salas_a1(num_salas)
restricciones = generar_restricciones_profesor(num_profesores)

guardar_instancia_en_txt(num_asignaturas, num_salas, num_profesores, num_bloques,
                         prioridades, bloques_necesarios, num_alumnos, capacidades, restricciones)

# Mostrar un ejemplo de salida
print(f"num_asignaturas = {num_asignaturas};")
print(f"num_salas = {num_salas};")
print(f"num_profesores = {num_profesores};")
print(f"num_bloques = {num_bloques};\n")
print("prioridad = [")
print(", ".join(str(p) for p in prioridades), "];")
print("R = [")
print(", ".join(str(b) for b in bloques_necesarios), "];")
print("num_alumnos = [")
print(", ".join(str(n) for n in num_alumnos), "];")
print("capacidad = [")
print(", ".join(str(c) for c in capacidades), "];")
print("restricciones = [")
for restriccion in restricciones:
    print(f"  {{{', '.join(str(b) for b in restriccion)}}},")
print("];")
