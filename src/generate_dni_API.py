import requests
import random
from TablaAsig import TablaAsignacion

t = TablaAsignacion()

def generateDNIList(numDNIs):
    try:
        url = f"https://ensaimeitor.apsl.net/fiscal/10/?format=json&num={numDNIs}"
        response = requests.get(url).json()
        return response['codigo']
     
    except Exception as e:
        return f'Error: {e}'


def generateCorrectCases(numDNIs):
    valids = []
    for dni in generateDNIList(numDNIs):
        while len(valids) < numDNIs:
            if t.validateDNI(dni):
                valids.append(dni)
    return valids


def generateIncorrectDNIList(numDNIs):
    not_valids = []   
    for dni in generateDNIList(numDNIs):
        while len(not_valids) < numDNIs:
            if t.validateDNI(dni):
                not_valids.append(dni[:-1] + random.choice(t.getTabla()))
            elif len(dni) != 9:
                not_valids.append(str(random.randint(1, 9)) + dni[1:])
            else:
                not_valids.append(dni)
    return not_valids
    
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

    correctCases = generateCorrectCases(2)
    incorrectCases = generateIncorrectDNIList(2)
    randomCases = generateRandomCases(2)

    for i, dni in enumerate(incorrectCases):
        print(f'{i + 1}:\t{dni} \t{t.validateDNI(dni)}')

    for i, dni in enumerate(correctCases):
        print(f'{i + 1}:\t{dni} \t{t.validateDNI(dni)}')

    for i, dni in enumerate(randomCases):
        print(f'{i + 1}:\t{dni} \t{t.validateDNI(dni)}')