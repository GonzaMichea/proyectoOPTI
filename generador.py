import random

def generar_asignaturas_b1(num_asignaturas):
    prioridades = []
    bloques_necesarios = []
    num_alumnos = []
    for i in range(num_asignaturas):
        es_indispensable = (i % 5 == 0)  # 1 de cada 5 asignaturas es indispensable
        prioridad = random.randint(6, 10) if es_indispensable else random.randint(1, 5)
        prioridades.append(prioridad)
        
        # Calcular el 65% y el 35% del total de asignaturas
        num_bloques_1 = int(num_asignaturas * 0.65)
        num_bloques_2 = num_asignaturas - num_bloques_1

        # Crear la lista de bloques necesarios asegurando la proporción exacta
        bloques_necesarios = [1] * num_bloques_1 + [2] * num_bloques_2

        # Barajar la lista para distribuir aleatoriamente los bloques
        random.shuffle(bloques_necesarios)
        
        alumnos = random.randint(10, 40)  # Cantidad de alumnos entre 10 y 40
        num_alumnos.append(alumnos)
        
    return prioridades, bloques_necesarios, num_alumnos

def generar_salas_a1(num_salas):
    capacidades = []
    for i in range(num_salas):
        capacidad = random.randint(20, 45)  # Capacidad entre 20 y 45
        capacidades.append(capacidad)
    return capacidades

def generar_restricciones_profesor(cant_profes):
    restricciones = []
    
    for i in range(cant_profes):
        n_bloques = random.randint(7,21) #Cantidad de bloques restringidos
        lista = [1] * 35 #35 = 7*5 bloques por dias
        posiciones = random.sample(range(35), n_bloques)

        for posicion in posiciones:
            lista[posicion] = 0
        
        restricciones.extend(lista)
        
    return restricciones

def guardar_instancia(num_asignaturas, num_salas, prioridades, bloques_necesarios, num_alumnos, capacidades, restricciones,
nombre_archivo="instancia.dzn"):
    with open(nombre_archivo, "w") as f:
        f.write(f"n = {num_asignaturas};\n")
        f.write(f"m = {num_salas};\n")

        
        f.write("p = [")
        f.write(", ".join(str(p) for p in prioridades))
        f.write("];\n")

        f.write("b = [")
        f.write(", ".join(str(b) for b in bloques_necesarios))
        f.write("];\n")
        
        f.write("I = [")
        f.write(", ".join(str(n) for n in num_alumnos))
        f.write("];\n")
        
        f.write("c = [")
        f.write(", ".join(str(c) for c in capacidades))
        f.write("];\n")
        
        f.write("r = array3d(1.."+str(num_asignaturas)+",1..7,1..5,[")
        f.write(", ".join(str(r) for r in restricciones))
        f.write("]);\n")


# Generar instancias específicas
num_asignaturas = int(input("Ingrese número de asignaturas: ")) # Equivale al n de profes
num_salas = int(input("Ingrese número de salas: "))
num_bloques = 35  # 7 bloques por día * 5 días no cambia

prioridades, bloques_necesarios, num_alumnos = generar_asignaturas_b1(num_asignaturas)
capacidades = generar_salas_a1(num_salas)
restricciones = generar_restricciones_profesor(num_asignaturas)

guardar_instancia(num_asignaturas, num_salas, prioridades, bloques_necesarios, num_alumnos, capacidades, restricciones)

print("Instancia generada satisfactoriamente")