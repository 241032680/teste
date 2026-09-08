#Fundamentos
def testar_e():
    for limite in (0, 50, 150, 300):
        valores = (0, limite, 300)
        maior = max(valores)
        menor = min(valores)
        meio = sum(valores) - maior - menor
        print(f"Teste E ({limite}): maior = {maior}, meio = {meio}")


def testar_f():
    for limite in (0, 50, 150, 300):
        if limite == 0:
            resultado = "zero"
        elif limite % 2 == 0:
            resultado = "positivo e par"
        else:
            resultado = "positivo e ímpar"
        print(f"Teste F ({limite}): número {resultado}")


def testar_g():
    for limite in (0, 50, 150, 300):
        lado_a = lado_b = lado_c = limite
        valido = (lado_a > 0 and lado_a + lado_b > lado_c
                  and lado_a + lado_c > lado_b
                  and lado_b + lado_c > lado_a)
        if valido:
            semiperimetro = (lado_a + lado_b + lado_c) / 2
            area = (semiperimetro * (semiperimetro - lado_a)
                    * (semiperimetro - lado_b)
                    * (semiperimetro - lado_c)) ** 0.5
            print(f"Teste G ({limite}): válido, área = {area:.2f}")
        else:
            print(f"Teste G ({limite}): triângulo inválido")


def testar_h():
    for limite in (0, 50, 150, 300):
        valor_final = max(100, 30)
        if limite > 300:
            valor_final *= 0.95
        print(f"Teste H ({limite} km): R$ {valor_final:.2f}")


exvalido = 0
while exvalido == 0:
    ex = input("Digite o exercício que deseja executar: ")
    if ex == "A" or ex == "B" or ex == "C" or ex == "D" or ex == "E" or ex == "F" or ex == "G" or ex == "H" or ex == "I" or ex == "J" or ex == "K" or ex == "L" or ex == "a" or ex == "b" or ex == "c" or ex == "d" or ex == "e" or ex == "f" or ex == "g" or ex == "h" or ex == "i" or ex == "j" or ex == "k" or ex == "l":
        exvalido += 1
    else:
        print("Input Inválido")

#A e B
if ex == "A" or ex == "a" or ex == "B" or ex == "b":
    Valido = 0
    b = int(input("Digite o primeiro numero: "))
    c = int(input("Digite o segundo numero: "))
    while Valido == 0:
        a = str(input("Multiplicar(M) ou Somar(S)? "))
        if a == "Multiplicar" or a == "M":
            d = float(c * b)
            Valido = 1
        elif a == "Somar" or a == "S":
            d = float(c + b)
            Valido = 1
        else:
            print ("Input Inválido")

    print("O resultado é: ", d)

#C
elif ex == "C" or ex == "c":
    catum= int(input("Digite o primeiro cateto: "))
    catdois= int(input("Digite o segundo cateto: "))
    hip = float(catum**2 + catdois**2)**0.5
    print(f"O valor da hipotenusa é: {hip:.3f}")

#D
elif ex == "D" or ex == "d":
    A = int(input("Digite o primeiro numero: "))
    B = int(input("Digite o segundo numero: "))
    C = int(input("Digite o terceiro numero: "))

    D = (A + B + C) / 3 
    print(f"A média é: {D:.2f}")
    E = (A + B + C)
    print("A soma é: ", E)

#Decisões
elif ex == "E" or ex == "e":
    A = int(input("Digite o primeiro numero: "))
    B = int(input("Digite o segundo numero: "))
    C = int(input("Digite o terceiro numero: "))
    maior = max(A, B, C)
    menor = min(A, B, C)
    meio = A + B + C - maior - menor
    print(f"O maior valor é: {maior}")
    print(f"O valor do meio é: {meio}")
    if input("Deseja executar os testes de limite? (s/n) ").lower() == "s":
        testar_e()

elif ex == "F" or ex == "f":
    A = float(input("Digite o numero: "))
    if A > 0:
        print("O numero é positivo")
        if A % 2 == 0:
            print("O numero é par")
    elif A < 0:
        print("O numero é negativo")
        if A % 2 == 0:
            print("O numero é par")
    elif A == 0:
        print("O numero é zero")
    else:
        print("NaN")
    if input("Deseja executar os testes de limite? (s/n) ").lower() == "s":
        testar_f()

elif ex == "G" or ex == "g":
    lado_a = float(input("Digite o primeiro lado: "))
    lado_b = float(input("Digite o segundo lado: "))
    lado_c = float(input("Digite o terceiro lado: "))

    if (lado_a > 0 and lado_b > 0 and lado_c > 0
            and lado_a + lado_b > lado_c
            and lado_a + lado_c > lado_b
            and lado_b + lado_c > lado_a):
        semiperimetro = (lado_a + lado_b + lado_c) / 2
        area = (
            semiperimetro
            * (semiperimetro - lado_a)
            * (semiperimetro - lado_b)
            * (semiperimetro - lado_c)
        )**0.5
        print(f"A área do triângulo é: {area:.2f}")
    else:
        print("Os lados não formam um triângulo válido.")
    if input("Deseja executar os testes de limite? (s/n) ").lower() == "s":
        testar_g()

elif ex == "H" or ex == "h":
    valor_aluguel = float(input("Digite o valor do aluguel: R$ "))
    quilometros = float(input("Digite a quantidade de quilômetros: "))

    valor_final = max(valor_aluguel, 30)
    if quilometros > 300:
        valor_final *= 0.95

    print(f"O valor final do aluguel é: R$ {valor_final:.2f}")
    if input("Deseja executar os testes de limite? (s/n) ").lower() == "s":
        testar_h()

elif ex == "I" or ex == "i":
    palavra = input("Digite uma palavra com cinco caracteres: ")
    while len(palavra) != 5 or not palavra.isalpha():
        print("A palavra deve ter exatamente cinco letras.")
        palavra = input("Digite uma palavra com cinco caracteres: ")

    vogais = "aeiouáéíóúâêîôûãõ"
    encontradas = [letra for letra in palavra if letra.lower() in vogais]
    print(f"Quantidade de vogais: {len(encontradas)}")
    print(f"Vogais encontradas: {encontradas}")

elif ex == "J" or ex == "j":
    palavra = input("Digite uma palavra: ")
    substituicoes = str.maketrans({"a": "i", "e": "o", "i": "u"})
    print(f"Palavra transformada: {palavra.translate(substituicoes)}")

elif ex == "K" or ex == "k":
    texto = input("Digite uma palavra ou frase: ")
    texto_normalizado = "".join(texto.split()).lower()
    if texto_normalizado == texto_normalizado[::-1]:
        print("O texto é igual ao seu inverso.")
    else:
        print("O texto não é igual ao seu inverso.")
    
elif ex == "L" or ex == "l":
    p = input("Digite a sequência p: ")
    q = input("Digite o texto q: ")
    if p in q:
        print("A sequência p aparece dentro de q.")
    else:
        print("A sequência p não aparece dentro de q.")