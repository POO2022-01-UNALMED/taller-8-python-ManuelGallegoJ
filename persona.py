class Persona():

    def __init__(self, n, e, a, s):
        self._nombre = n
        self._edad = e
        self._altura = a
        self._sexo = s

    def getNombre(self):
        return self._nombre

    def setNombre(self, nn):
        self._nombre = nn

    def getEdad(self):
        return self._edad

    def setEdad(self, ee):
        self._edad = ee

    def getAltura(self):
        return self._altura

    def setEdad(self, aa):
        self._edad = aa

    def getSexo(self):
        return self._sexo

    def setSexo(self, ss):
        self._sexo = ss