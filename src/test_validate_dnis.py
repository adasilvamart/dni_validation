from TablaAsig import TablaAsignacion
from generate_dni_API import generateDNIList, generateIncorrectDNIList

def generateTestCases(numOfCases):
    correctCases = generateDNIList(numOfCases)
    incorrectCases = generateIncorrectDNIList(numOfCases)
    return correctCases, incorrectCases

def test_isCorrectDNI(numOfCases):
    correct, incorrect = generateTestCases(numOfCases)
    testCases = [correct, incorrect]
    for listOfCases in testCases:
        for dni in listOfCases:
            t = TablaAsignacion()
            print(f'{dni}\t: Correcto') if t.validateDNI(dni) else print(f'{dni}\t: Incorrecto')
    
    
if __name__ == '__main__':
    print(test_isCorrectDNI(20))