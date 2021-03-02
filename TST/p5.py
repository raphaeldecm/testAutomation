import math

#entrada
a = int(input("a? "))
b = int(input("b? "))
c = int(input("c? "))

#processamento
delta = b ** 2 - 4 * a * c

if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

#saida
print(f"{delta:.5f}")

if delta >= 0:
    print(f"{x1:.5f}")
    print(f"{x2:.5f}")
else:
    print("sem raizes")

