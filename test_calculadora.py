import pytest

from calculadora import sumar, restar, multiplicar, dividir


# =====================================================================
# CASOS DE PRUEBA INICIALES (CP01 - CP05)
# =====================================================================
def test_sumar_positivos():
    # CP01: Caso normal de suma
    assert sumar(2, 3) == 5


def test_sumar_negativos():
    # CP02: Suma de negativos
    assert sumar(-2, -3) == -5


def test_dividir_exactamente():
    # CP03: División exacta
    assert dividir(10, 2) == 5


def test_dividir_decimal():
    # CP04: División con decimal
    assert dividir(7, 2) == 3.5


def test_dividir_entre_cero():
    # CP05: División entre cero (prueba negativa)
    with pytest.raises(ValueError):
        dividir(10, 0)


# =====================================================================
# ACTIVIDAD COMPLEMENTARIA (CP06 - CP12)
# =====================================================================
def test_restar_positivos():
    # CP06: Función de resta (prueba 1)
    assert restar(10, 4) == 6


def test_restar_negativos():
    # CP07: Función de resta con negativos (prueba 2)
    assert restar(-5, -8) == 3


def test_multiplicar_positivos():
    # CP08: Función de multiplicación con positivos
    assert multiplicar(6, 7) == 42


def test_multiplicar_negativos():
    # CP09: Función de multiplicación con valores negativos
    assert multiplicar(-4, 5) == -20
    assert multiplicar(-3, -6) == 18


def test_dividir_cero_entre_numero():
    # CP10: Dividir cero entre un número distinto de cero
    assert dividir(0, 5) == 0
    assert dividir(0, -8) == 0


def test_dividir_entrada_no_numerica():
    # CP11: Validación de entradas no numéricas en dividir() (Issue #1)
    with pytest.raises(TypeError, match="Los argumentos deben ser valores numéricos"):
        dividir("diez", 2)


def test_operaciones_entrada_no_numerica():
    # CP12: Validación de entradas no numéricas en sumar, restar y multiplicar
    with pytest.raises(TypeError):
        sumar("2", 3)
    with pytest.raises(TypeError):
        restar(10, None)
    with pytest.raises(TypeError):
        multiplicar(True, 5)
