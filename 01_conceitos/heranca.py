# ========================================
# 3. heranca.py
# Herança entre Classes
# ========================================

class Animal:
    """Classe base"""
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        return "Algum som..."


class Cachorro(Animal):
    """Classe derivada com herança"""
    def __init__(self, nome, raca):
        # Herança com super()
        super().__init__(nome, "Cachorro")
        self.raca = raca

    def emitir_som(self):
        return "Au au!"

    def info(self):
        return f"{self.nome} é um {self.especie} da raça {self.raca}"


class Gato(Animal):
    """Outra classe derivada"""

    def __init__(self, nome, cor):
        super().__init__(nome, "Gato")
        self.cor = cor

    def emitir_som(self):
        return "Miau!"


def exemplo_heranca():
    print("\n" + "=" * 50)
    print("HERANÇA")
    print("=" * 50 + "\n")

    dog = Cachorro("Rex", "Labrador")
    cat = Gato("Mimi", "Branco")

    print(dog.info())
    print(f"Som: {dog.emitir_som()}\n")

    print(f"{cat.nome} é {cat.cor}")
    print(f"Som: {cat.emitir_som()}")

exemplo_heranca()