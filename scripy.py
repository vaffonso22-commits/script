numero = int(input("digite o numero da tabuada: "))

print(f"\nTabuada do {numero}:n")

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")