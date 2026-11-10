soma=0
while True:
    número=int(input("Digite um número:"))
    if número==0:
        break
    soma+=número
print(f"A soma dos números é:{soma}")
