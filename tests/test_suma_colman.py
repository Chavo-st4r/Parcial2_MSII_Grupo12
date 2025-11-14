from funciones.suma_colman import suma_colman

def test_suma_colman():
    assert suma_colman(3, 5) == 8
    assert suma_colman(-2, 2) == 0
