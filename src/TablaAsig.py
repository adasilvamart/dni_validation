class TablaAsignacion:
    def __init__(self):
        self.tabla = [
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]

    def __repr__(self):
        return str(self.getTabla())
    
    def getTabla(self):
        return self.tabla

    @staticmethod
    def isCorrectDNI(dni_string):
        return True if dni_string[:-1].isdigit() and dni_string[-1].isalpha() and len(dni_string) == 9 else False
    
    def calcLetra(self, dni_string):
        return int(dni_string[:-1]) % len(self.getTabla())
    
    def getLetra(self, dni_string):
        return self.tabla[self.calcLetra(dni_string)]

    
    def validateDNI(self, dni_string):
        if self.isCorrectDNI(dni_string):
            return self.getLetra(dni_string) == dni_string[-1].upper()
    