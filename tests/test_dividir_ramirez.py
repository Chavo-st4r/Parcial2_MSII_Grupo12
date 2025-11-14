#Arreglo
from funciones.dividir_ramirez import dividir

def test_dividir_ramirez():
    assert dividir(10, 2) == 5
    assert dividir(5, 0) is None
