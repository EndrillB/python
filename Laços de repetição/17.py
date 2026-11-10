fatorial=1
x=(int(input("Digite um número:")))
for i in range(x,1,-1):
    fatorial*=i
    print(fatorial)