# ========================================
# 6. decoradores.py
# Decoradores
# ========================================

def medir_tempo(func):
    """Decorador que mede o tempo de execução"""
    import time

    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"⏱️  {func.__name__} executou em {fim - inicio:.4f}s")
        return resultado

    return wrapper


def validar_positivo(func):
    """Decorador que valida se argumentos são positivos"""

    def wrapper(*args):
        if any(x < 0 for x in args):
            raise ValueError("Todos os números devem ser positivos!")
        return func(*args)

    return wrapper


@medir_tempo
def calcular_soma(n):
    """Função decorada"""
    return sum(range(n))


@validar_positivo
@medir_tempo
def multiplicar(a, b):
    """Múltiplos decoradores"""
    return a * b


def exemplo_decoradores():
    print("\n" + "=" * 50)
    print("DECORADORES")
    print("=" * 50 + "\n")

    resultado = calcular_soma(1000000)
    print(f"Resultado: {resultado}\n")

    resultado2 = multiplicar(5, 8)
    print(f"Resultado: {resultado2}")


exemplo_decoradores()