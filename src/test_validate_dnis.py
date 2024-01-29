from TablaAsig import TablaAsignacion
from generate_dni_API import generateCorrectCases, generateIncorrectDNIList, generateRandomCases

t = TablaAsignacion()


def test_validDNI(numOfCases):
    correctCases = generateCorrectCases(numOfCases)
    incorrectCases = generateIncorrectDNIList(numOfCases)
    randomCases = generateRandomCases(numOfCases)

    testCases = [correctCases, incorrectCases, randomCases]
    
    for listOfCases in testCases:
        for i, dni in enumerate(listOfCases):
            print(f'{i + 1}:\t{dni} \t{t.validateDNI(dni)}')
        print(f'-' * 45)
    
    
if __name__ == '__main__':
    test_validDNI(10)