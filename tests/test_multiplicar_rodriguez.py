#teststitest_multiplicar.py
from funciones.multiplicarrodriguez import multiplicar
def test_multiplicar_rodriguez():
 assert multiplicar(3, 4) == 12
 assert multiplicar(-2, 5) == -10
