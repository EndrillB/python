print("Média cinco números")
soma=0
for i in range(1,6):
    número=int(input(f"Digite o {i}° número:"))
    soma=soma+número
media=((soma)/5)
print(media)
