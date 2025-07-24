num = int(input("Digite um numero: "))

for i in range(1, 21):
    mult = num * i
    print(f"{num} x {i: ^2} = {mult: ^5}")
