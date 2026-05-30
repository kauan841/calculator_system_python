def dividir (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Os argumentos devem ser números.")
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b