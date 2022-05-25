class Deportista:

    def __init__(self, ap):
        self._deporte = "Futbol"
        self._añosPracticando = ap

    def getDeporte(self):
        return self._deporte

    def setDeporte(self, dd):
        self._deporte = dd

    def getAñosPracticando(self):
        return self._añosPracticando

    def setAñosPracticando(self, apap):
        self._añosPracticando = apap