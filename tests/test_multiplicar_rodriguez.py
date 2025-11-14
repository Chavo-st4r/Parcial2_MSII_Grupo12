#teststitest_multiplicar.py
from funciones.multiplicarrodriguez import multiplicarrodriguez
def test_multiplicar_rodriguez():
 assert multiplicarrodriguez(3, 4) == 12
 assert multiplicarrodriguez(-2, 5) == -10
