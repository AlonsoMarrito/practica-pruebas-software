def _validar_numeros(a, b):
    """Valida que ambos operandos sean números reales (int o float) y no booleanos."""
    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser valores numéricos")


def sumar(a, b):
    _validar_numeros(a, b)
    return a + b


def restar(a, b):
    _validar_numeros(a, b)
    return a - b


def multiplicar(a, b):
    _validar_numeros(a, b)
    return a * b


def dividir(a, b):
    _validar_numeros(a, b)
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
