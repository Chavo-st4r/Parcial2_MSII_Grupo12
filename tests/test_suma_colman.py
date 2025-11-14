from funciones.suma_gomez import suma_gomez

def test_suma_gomez():
    assert suma_gomez(3, 5) == 8
    assert suma_gomez(-2, 2) == 0
