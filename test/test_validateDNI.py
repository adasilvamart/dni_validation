import src.generate_dni_API as gdni
from src.TablaAsig import TablaAsignacion


def test_validateDNI():
    t = TablaAsignacion()

    for dni in gdni.generateCorrectCases(10):
        assert t.validateDNI(dni)

    for dni in gdni.generateIncorrectDNIList(10):
        assert not t.validateDNI(dni)


def test_isCorrectDNI():
    t = TablaAsignacion()

    for dni in gdni.generateCorrectCases(10):
        assert t.isCorrectDNI(dni)

    for dni in gdni.generateIncorrectDNIList(10):
        assert not t.isCorrectDNI(dni)
