from TablaAsig import TablaAsignacion

class Dni:

    def __init__(self, dni, tabla=TablaAsignacion()):
        self.__dni = self.createValidDNI(dni, tabla)

    def __eq__(self, other):
        return self.getDni() == other.getDni()

    def __repr__(self):
        return str(self.getDni())

    def getDni(self):
        return self.__dni
    
    @staticmethod
    def padDni(dni):
        return str(f"{int(dni[:-1]):08}{dni[-1].upper()}")

    @classmethod
    def createValidDNI(cls, dni, tabla):
        if tabla.validateDNI(dni):
            return cls.padDni(dni)
        raise ValueError('[!] El DNI no es válido')


# El estado del objeto se determina con las propiedades del objeto. Cada instancia es diferente en memoria.
if __name__ == '__main__':

    dni1 = Dni('39462114w')

    dni2 = Dni('39462114w')

    dni3 = Dni('00000014z')
    dni4 = Dni('1R')

    print(dni4)

    print(83391625 % 23)