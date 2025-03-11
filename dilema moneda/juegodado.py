import random

def num_par(num):
    return num % 2 == 0

def throw():
    return num_par(random.choice(range(1, 7))) and random.choice(["cara", "sello"]) == "cara"

def main():
    num_throw = int(input("Introduzca el número de lanzamientos: "))
    contG = sum(1 for _ in range(num_throw) if throw())
    contP = num_throw - contG

    print(f"Wins: {contG} | Losses: {contP} | Win Rate: {contG / num_throw:.2%}")

main()
