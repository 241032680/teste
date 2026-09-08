import math


ex = input("Digite o exercício que deseja executar (A, B, C ou D): ").upper()
while ex not in ("A", "B", "C", "D"):
    print("Input inválido")
    ex = input("Digite o exercício que deseja executar (A, B, C ou D): ").upper()

#A

if ex == "A":
    valido = 0
    while valido == 0:
        p2 = float(input("Digite P2, maior que zero: "))
        if p2 > 0:
            p1 = 1
            decibeis = 10 * math.log10(p2 / p1)
            print(f"Resultado: {decibeis} dB")
            valido += 1
        else:
            print("P2 deve ser maior que zero.")

#B
elif ex == "B":
    for x in [lado1, lado2, lado3]:
        if x is not float:
            print("Entrada inválida. Por favor, insira números válidos.")
            break
    lado1 = float(input("Digite o primeiro lado: "))
    lado2 = float(input("Digite o segundo lado: "))
    lado3 = float(input("Digite o terceiro lado: "))

    if (lado1 > 0 and lado2 > 0 and lado3 > 0
            and lado1 + lado2 > lado3
            and lado1 + lado3 > lado2
            and lado2 + lado3 > lado1):
        semiperimetro = (lado1 + lado2 + lado3) / 2
        area = math.sqrt(
            semiperimetro
            * (semiperimetro - lado1)
            * (semiperimetro - lado2)
            * (semiperimetro - lado3)
        )
        print(f"Área: {area:.3f}")
    else:
        print("Os lados não formam um triângulo válido.")

#C
elif ex == "C":
    numeros = []
    rangelow = int(input("Digite o valor inicial do intervalo: "))
    rangehigh = int(input("Digite o valor final do intervalo (max 999999): "))
    for numero in range(rangelow, rangehigh + 1):
        if not 1000 <= numero <= 999999:
            continue

        raiz = math.sqrt(numero)
        texto = str(numero)
        primeira_metade = int(texto[:2])
        segunda_metade = int(texto[2:])
        if raiz.is_integer() and primeira_metade + segunda_metade == int(raiz):
            numeros.append(numero)

    print("Números encontrados:", numeros)

#D
elif ex == "D":
    numero = int(input("Digite um número inteiro: "))
    primo = numero > 1

    for divisor in range(2, math.isqrt(numero) + 1) if numero > 1 else []:
        if numero % divisor == 0:
            primo = False
            break

    if primo:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
