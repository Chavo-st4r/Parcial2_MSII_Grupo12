#tests/test_multiplicar.py
from funciones.multiplicar_rodriguez import multiplicar_rodriguez
def test_multiplicar_rodriguez():
 assert multiplicar_rodriguez(3, 4) == 12
 assert multiplicar_rodriguez(-2, 5) == -10
