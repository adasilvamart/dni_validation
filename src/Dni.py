from TablaAsig import TablaAsignacion
class Dni:
    def __init__(self, dni, tabla=TablaAsignacion()):
        self.__dni = self.createValidDNI(dni, tabla)

    def __repr__(self):
        return str(self.getDni())

    def getDni(self):
        return self.__dni

    @staticmethod
    def createValidDNI(dni, tabla):
        if tabla.validateDNI(dni):
            return dni[:-1] + dni[-1].upper()
        raise ValueError('[!] El DNI no es válido')
