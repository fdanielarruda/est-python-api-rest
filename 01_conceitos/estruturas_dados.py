# ========================================
# 1. estruturas_dados.py
# Estruturas de Dados Básicas
# ========================================

def exemplo_estruturas_dados():
    print("=" * 50)
    print("ESTRUTURAS DE DADOS")
    print("=" * 50 + "\n")

    # LISTAS []
    frutas = ["maçã", "banana", "laranja"]
    print("LISTA:", frutas)
    frutas.append("uva")
    frutas[0] = "morango"
    print("Lista modificada:", frutas, "\n")

    # TUPLAS ()
    coordenadas = (10.5, 20.3, 5.8)
    print("TUPLA:", coordenadas)
    print("Tuplas são imutáveis - não podem ser alteradas\n")

    # SETS {}
    numeros = {1, 2, 3, 2, 1, 4, 5}
    print("SET (valores únicos):", numeros)
    numeros.add(6)
    print("Set após adicionar 6:", numeros, "\n")

    # DICIONÁRIO
    aluno = {
        "nome": "João",
        "idade": 20,
        "curso": "Python"
    }
    print("DICIONÁRIO:", aluno)
    print(f"Nome do aluno: {aluno['nome']}\n")

    # LIST COMPREHENSION
    quadrados = [x ** 2 for x in range(1, 6)]
    print("LIST COMPREHENSION (quadrados):", quadrados)

    pares = [n for n in range(10) if n % 2 == 0]
    print("Números pares de 0 a 9:", pares)

exemplo_estruturas_dados()