# ========================================
# 5. args_kwargs.py
# *args e **kwargs
# ========================================

def somar_numeros(*args):
    """*args - aceita quantidade variável de argumentos posicionais"""
    print(f"Argumentos recebidos: {args}")
    return sum(args)


def criar_perfil(**kwargs):
    """**kwargs - aceita quantidade variável de argumentos nomeados"""
    print("\nPerfil criado:")
    for chave, valor in kwargs.items():
        print(f"  {chave}: {valor}")


def funcao_completa(*args, **kwargs):
    """Combina *args e **kwargs"""
    print(f"\nArgumentos posicionais (*args): {args}")
    print(f"Argumentos nomeados (**kwargs): {kwargs}")


def exemplo_args_kwargs():
    print("\n" + "=" * 50)
    print("*ARGS E **KWARGS")
    print("=" * 50 + "\n")

    # *args
    resultado = somar_numeros(1, 2, 3, 4, 5)
    print(f"Soma: {resultado}")

    # **kwargs
    criar_perfil(
        nome="Daniel",
        idade=23,
        cidade="Maranguape",
        profissao="Desenvolvedor"
    )

    # Ambos
    funcao_completa(10, 20, 30, cor="azul", tamanho="grande")


exemplo_args_kwargs()