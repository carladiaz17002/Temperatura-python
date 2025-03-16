temperaturas = {
    "Quito": [20, 22, 21, 19],
    "Guayaquil": [28, 30, 29, 31],
    "Cuenca": [18, 19, 17, 20]
}
def calcular_promedio_ciudades(datos):
    promedios = {}
    for ciudad, temps in datos.items():
        promedio = sum(temps) / len(temps)
        promedios[ciudad] = promedio
    return promedios
print(calcular_promedio_ciudades(temperaturas))