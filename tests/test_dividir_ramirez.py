#Arreglo
from funciones.dividir_ramirez import dividir_ramirez

def test_dividir_ramirez():
    assert dividir_ramirez(10, 2) == 5
    assert dividir_ramirez(5, 0) is None
