import random

v1 = 0
v2 = 0
empate = 0

def valida_int(pergunta: str, minimo: int, maximo: int) -> int:
    x = int(input(pergunta))
    while (x < minimo) or (x > maximo):
        x = int(input(pergunta))
    return x

def vencedor(jogador1: int, jogador2: int) -> None:
    global v1, v2, empate
    if jogador1 == jogador2:
        empate += 1
    elif jogador1 == 1:        # Pedra
        if jogador2 == 2:      # Papel
            v2 += 1
        else:                  # Tesoura
            v1 += 1
    elif jogador1 == 2:        # Papel
        if jogador2 == 1:      # Pedra
            v1 += 1
        elif jogador2 == 2:    # Papel
            empate += 1
        else:                  # Tesoura
            v2 += 1
    elif jogador1 == 3:        # Tesoura
        if jogador2 == 1:      # Pedra
            v2 += 1
        elif jogador2 == 2:    # Papel
            v1 += 1
        else:                  # Tesoura
            empate += 1

# PROGRAMA PRINCIPAL
print("PEDRA | PAPEL | TESOURA")
print("0 - Sair")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

jogadas = []

while True:
    j1 = valida_int("Escolha sua jogada (0 para sair): ", 0, 3)
    if j1 == 0:
        break
    j2 = random.randint(1, 3)
    jogadas.append((j1, j2))
    vencedor(j1, j2)

print("\nResumo das jogadas (Você, CPU):")
for a, b in jogadas:
    print(a, b)

print(f"\nNúmero de vitórias do Jogador 1: {v1}")
print(f"\nNúmero de vitórias do Jogador 2: {v2}")
print(f"\nNúmero de empates: {empate}")