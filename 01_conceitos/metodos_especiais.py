# ========================================
# 4. metodos_especiais.py
# Métodos de Classe e Estáticos
# ========================================

class Contador:
    """Demonstra métodos de classe e estáticos"""

    total = 0  # Atributo de classe

    def __init__(self, nome):
        self.nome = nome
        Contador.total += 1

    @classmethod
    def get_total(cls):
        """Método de classe - acessa atributos da classe"""
        return f"Total de contadores criados: {cls.total}"

    @staticmethod
    def validar_nome(nome):
        """Método estático - não acessa self nem cls"""
        return len(nome) > 0 and nome.isalpha()


def exemplo_metodos_especiais():
    print("\n" + "=" * 50)
    print("MÉTODOS DE CLASSE E ESTÁTICOS")
    print("=" * 50 + "\n")

    # Método estático
    print(f"'João' é válido? {Contador.validar_nome('João')}")
    print(f"'123' é válido? {Contador.validar_nome('123')}\n")

    # Criando instâncias
    c1 = Contador("Primeiro")
    c2 = Contador("Segundo")
    c3 = Contador("Terceiro")

    # Método de classe
    print(Contador.get_total())

exemplo_metodos_especiais()