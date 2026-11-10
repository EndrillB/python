x=int(input("Digite um número:"))
for i in range(1,x+1):
    if x%i ==0:
        print(f"{x} é divisivel por {i}")