def raiz(a):
    if not isinstance(a, (int, float)):
        raise ValueError("O argumento deve ser um número.")
    if a < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return a ** 0.5