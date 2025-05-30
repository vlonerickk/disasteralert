class Localizacao:
    def __init__(self, cidade, estado, latitude, longitude):
        self.cidade = cidade
        self.estado = estado
        self.latitude = latitude
        self.longitude = longitude

    def calcular_distancia(self, outra):
        from math import radians, sin, cos, sqrt, atan2

        raio_terra = 6371  # km
        lat1 = radians(self.latitude)
        lon1 = radians(self.longitude)
        lat2 = radians(outra.latitude)
        lon2 = radians(outra.longitude)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distancia = raio_terra * c
        return distancia

    def __str__(self):
        return f"{self.cidade} - {self.estado} (Lat: {self.latitude}, Lon: {self.longitude})"
