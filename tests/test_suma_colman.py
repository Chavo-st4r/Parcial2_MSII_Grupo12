from funciones.suma_colman import suma

def test_suma():
    assert suma(3, 5) == 8
    assert suma(-2, 2) == 0
