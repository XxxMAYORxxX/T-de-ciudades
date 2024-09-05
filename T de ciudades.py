import numpy  as np

# Definir las dimensiones
num_ciudades = 3
num_dias_semana = 7
num_semanas = 4

# Crear una matriz 3D con valores aleatorios para las temperaturas
np.random.seed(0)  # Para reproducibilidad
temperaturas = np.random.randint(0, 35, size=(num_ciudades, num_dias_semana, num_semanas))

# Calcular el promedio de temperaturas por ciudad y semana
promedios = np.zeros((num_ciudades, num_semanas))

for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        # Extraer las temperaturas de la ciudad en la semana actual
        temperaturas_semana = temperaturas[ciudad, :, semana]
        # Calcular el promedio de temperaturas para la ciudad en esa semana
        promedio_semana = np.mean(temperaturas_semana)
        promedios[ciudad, semana] = promedio_semana

# Mostrar el promedio de temperaturas por ciudad y semana
for ciudad in range(num_ciudades):
    print(f"Ciudad {ciudad + 1}:")
    for semana in range(num_semanas):
        print(f"  Semana {semana + 1}: {promedios[ciudad, semana]:.2f}°C")

