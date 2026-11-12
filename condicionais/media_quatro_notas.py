notas = [float(input(f"Digite a nota {i}: ")) for i in range(1, 5)]

if any(not 0 <= nota <= 10 for nota in notas):
    print("As notas devem estar entre 0 e 10.")
else:
    media = sum(notas) / len(notas)
    if media >= 7:
        print("Aprovado!")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
