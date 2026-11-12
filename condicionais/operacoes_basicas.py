n1 = int(input("Digite um número "))
n2 = int(input("Digite outro número "))
op = int(input("1 para adição\n2 para subtração \n3 para multiplicação\n4 para divisão\n "))
if op == 1:
    print(f"A soma é: {n1 + n2}")
elif op == 2:
    print(f"A subtração é igual a {n1 - n2}")
elif op == 3:
    print(f"A multiplicação é: {n1 * n2}")
elif op == 4:
    if n2 == 0:
        print("Não é possível dividir por zero.")
    else:
        print(f"A divisão é: {n1 / n2}")
else:
    print("Operação inválida.")
