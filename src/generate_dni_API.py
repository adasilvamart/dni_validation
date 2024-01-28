import requests
import random
from TablaAsig import TablaAsignacion


def generateDNIList(numDNIs):
    try:
        if isinstance(numDNIs, int):
            url = f"https://ensaimeitor.apsl.net/fiscal/10/?format=json&num={numDNIs}"
            response = requests.get(url).json()
            return response['codigo']
        
    except Exception as e:
        return f'Error: {e}'
    

def generateIncorrectDNIList(numDNIs):
    tabla = TablaAsignacion()
    incorrectList = []
    for dni in generateDNIList(numDNIs):
        if random.choice(tabla.getTabla()) != dni[-1]:
            incorrectList.append(dni[:-1] + random.choice(tabla.getTabla()))
        elif len(dni) != 9:
            pass
    return incorrectList
    
def generateRandomCases(numCases):
    casosTest = []
    for i in range(1, numCases + 1):
        caso = ""
        for j in range(1, 9):
            caracterAscii = random.randrange(48, 58 + 1, 1)
            caso = caso + chr(caracterAscii)
        # en la ultima posicion añado una letra A-Z
        caso = caso + chr(random.randrange(65, 90 + 1, 1))
        casosTest = casosTest + [caso]
    return casosTest




if __name__ == '__main__':

    correctCases = generateDNIList(10)
    incorrectCases = generateIncorrectDNIList(10)
    randomCases = generateRandomCases(10)
    print(len(incorrectCases[0]), incorrectCases[0])
    print(len(correctCases[0]), correctCases[0])