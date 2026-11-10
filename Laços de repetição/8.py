pares=0
impares=0
for i in range(1,11):
    número=int(input(f"Digite o {i}° número:"))
    if número % 2==0:
        pares+=1
    else:
        impares+=1
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")