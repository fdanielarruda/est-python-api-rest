# ========================================
# 2. poo_basico.py
# POO - Classes, Objetos e Construtor
# ========================================

class Pessoa:
    """Classe básica representando uma pessoa"""

    def __init__(self, nome, idade):
        """Construtor - inicializa os atributos"""
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

    def aniversario(self):
        self.idade += 1
        return f"{self.nome} agora tem {self.idade} anos!"

def exemplo_poo_basico():
    print("\n" + "=" * 50)
    print("POO BÁSICO - Classes e Objetos")
    print("=" * 50 + "\n")

    # Criando OBJETOS (Instâncias)
    pessoa1 = Pessoa("Maria", 25)
    pessoa2 = Pessoa("Carlos", 30)

    print(pessoa1.apresentar())
    print(pessoa2.apresentar())
    print()

    print(pessoa1.aniversario())

exemplo_poo_basico()