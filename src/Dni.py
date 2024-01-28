from TablaAsig import TablaAsignacion
class Dni:
    
    tabla = TablaAsignacion()

    def __init__(self, dni):
        self.__dni = self.createValidDNI(dni)

    def __repr__(self):
        return str(self.getDni())

    def getDni(self):
        return self.__dni

    @staticmethod
    def createValidDNI(dni):
        if Dni.tabla.validateDNI(dni):
            return dni[:-1] + dni[-1].upper()
        raise ValueError('[!] El DNI no es válido')
    