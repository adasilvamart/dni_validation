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
    
    def validateDNI(self, dni_string):
        return self.getLetra(dni_string) == dni_string[-1].upper() if self.isCorrectDNI(dni_string) else False

    def isCorrectDNI(self, dni_string):
        return dni_string[:-1].isdigit() and dni_string[-1].isalpha() and dni_string[-1].upper() == self.getLetra(dni_string).upper()
    
    def calcLetra(self, dni_string):
        return int(dni_string[:-1]) % len(self.getTabla())

    def getLetra(self, dni_string):
        return self.tabla[self.calcLetra(dni_string)]
    
if __name__ == '__main__':
    tabla = TablaAsignacion()
    print(tabla.getTabla()[20])