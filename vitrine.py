# Lista dos Tamanhos das vestimentas
Tamanhos = ["PP", "P", "M", "G", "GG", "XXL"]

# Lista de dicionário: um por produto

vitrine = [
    {"nome": "Camiseta Básica", "preço": 39.90, "tamanho": "M"},
    {"nome": "Calça Jeans", "preço": 129.90, "tamanho": "G"},
    {"nome": "Moletom NIKE", "preço": 159.90, "tamanho": "P"},
]

# Lista de pares (nome, quantidade)
carrinho = [("Camiseta Básica", 3), ("Calça Jeans", 1)]

# Dicionário: nome -> preço

precos = {}
for produto in vitrine:
    precos[produto["nome"]] = produto["preço"]

total = 0 
for nome, quantidade in carrinho:
    total = total + precos[nome] * quantidade

print("Peças na vitrine:", len(vitrine))
print("Total do carrinho: R$", round(total, 2))