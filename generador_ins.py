import random
def generar_asignaturas_b1(num_asignaturas):
    asignaturas = []
    for i in range(num_asignaturas):
        es_indispensable = (i % 5 == 0)  # 1 de cada 5 asignaturas es indispensable
        prioridad = random.randint(6, 10) if es_indispensable else random.randint(1, 5)
        
        # El 65% tendrá 1 bloque, el 35% tendrá 2 bloques
        bloques_necesarios = 1 if random.random() < 0.65 else 2
        
        num_alumnos = random.randint(10, 40)  # Cantidad de alumnos entre 10 y 40
        
        asignaturas.append({
            'id': i + 1,
            'indispensable': es_indispensable,
            'prioridad': prioridad,
            'bloques': bloques_necesarios,
            'num_alumnos': num_alumnos
        })
    return asignaturas


def generar_salas_a1(num_salas):
    salas = []
    for i in range(num_salas):
        capacidad = random.randint(20, 45)  # Capacidad entre 20 y 45
        salas.append({
            'id': i + 1,
            'capacidad': capacidad
        })
    return salas


def generar_restricciones_profesor(num_profesores, min_bloques=7, max_bloques=21):
    restricciones = {}
    for profesor in range(num_profesores):
        bloques_restringidos = random.sample(range(35), random.randint(min_bloques, max_bloques))
        restricciones[profesor] = bloques_restringidos
    return restricciones




# Generar instancias específicas para el grupo 9 (B=1, A=1)
num_asignaturas = 43 # Número de asignaturas en tu caso
num_salas = 3  # Número de salas

asignaturas = generar_asignaturas_b1(num_asignaturas)
restricciones_profesores = generar_restricciones_profesor(10)  # 10 profesores
salas = generar_salas_a1(num_salas)

# Mostrar un ejemplo de salida
print("Asignaturas:", asignaturas)
print("Restricciones profesores:", restricciones_profesores)
print("Salas:", salas)
