"""Etapa 4: O Produto vira classe (Fonte: Aula 6)"""

TAMANHOS = ("PP", "P", "M", "G", "GG", "XXL")

class Produto:
    def __init__(self, nome, preco, tamanho):
        if not nome or not nome.strip():
            raise ValueError("O nome do produto não pode ser vazio!")
        if preco <= 0:
            raise ValueError("O valor não pode ser negativo!")
        if tamanho not in TAMANHOS:
            raise ValueError(f"Tamanho invalido: {tamanho}")
        self.nome = nome.strip()
        self.preco = preco
        self.tamanho = tamanho

    def descricao(self):
        return f"{self.nome} {self.tamanho}: R$ {self.preco:.2f}"

a = Produto("Moletom", 159.90, "G")
b = Produto(" Boné ", 35, "M")
c = Produto("Meia", 39.90, "P")
d = Produto("Jaqueta", 299.90, "GG")