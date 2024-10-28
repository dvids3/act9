from typing import Tuple, List

class DatosMeteorologicos:
    DIRECCIONES_VIENTO = {
        "N": 0,
        "NNE": 22.5,
        "NE": 45,
        "ENE": 67.5,
        "E": 90,
        "ESE": 112.5,
        "SE": 135,
        "SSE": 157.5,
        "S": 180,
        "SSW": 202.5,
        "SW": 225,
        "WSW": 247.5,
        "W": 270,
        "WNW": 292.5,
        "NW": 315,
        "NNW": 337.5
    }

    def __init__(self, nombre_archivo: str):
        self.filename = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperaturas = []
        humedades = []
        presiones = []
        vientos = []
        direcciones_viento = []

        with open(self.filename, 'r') as file:
            lineas = file.readlines()

        for linea in lineas:
            if "Estacion" in linea:
                continue  
            datos = linea.splitlines()
            for dato in datos:
                if dato.strip():  
                    clave, valor = dato.split(": ")
                    if clave == "Temperatura":
                        temperaturas.append(float(valor))
                    elif clave == "Humedad":
                        humedades.append(float(valor))
                    elif clave == "Presion":
                        presiones.append(float(valor))
                    elif clave == "Viento":
                        velocidad, direccion = valor.split(",")
                        vientos.append(float(velocidad))
                        direcciones_viento.append(direccion)

        
        temp_promedio = sum(temperaturas) / len(temperaturas)
        humedad_promedio = sum(humedades) / len(humedades)
        presion_promedio = sum(presiones) / len(presiones)
        viento_promedio = sum(vientos) / len(vientos)

       
        grados_viento = [self.DIRECCIONES_VIENTO[d] for d in direcciones_viento]
        direccion_promedio = sum(grados_viento) / len(grados_viento)

        
        direccion_final = self.obtener_direccion(direccion_promedio)

        return (temp_promedio, humedad_promedio, presion_promedio, viento_promedio, direccion_final)

    def obtener_direccion(self, grados: float) -> str:
       
        grados = grados % 360
        direcciones = list(self.DIRECCIONES_VIENTO.keys())
        diferencias = [abs(grados - self.DIRECCIONES_VIENTO[d]) for d in direcciones]
        indice_minimo = diferencias.index(min(diferencias))
        return direcciones[indice_minimo]


datos = DatosMeteorologicos('datos.txt')
estadisticas = datos.procesar_datos()
print("Temperatura promedio:", estadisticas[0])
print("Humedad promedio:", estadisticas[1])
print("Presión promedio:", estadisticas[2])
print("Velocidad promedio del viento:", estadisticas[3])
print("Dirección predominante del viento:", estadisticas[4])
