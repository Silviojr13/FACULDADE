# Exercicio 1

def e1():

    massa_inicial = float(input("Digite a massa inicial em gramas: "))
    massa_atual = massa_inicial
    tempo = 0

    while massa_atual >= 0.5:
        massa_atual /= 2
        tempo += 50

    print("Massa final:", massa_atual, "gramas")
    print("Tempo calculado:", tempo, "segundos")

def e2():

    for num in range(1000, 2000):
        if num % 11 == 5:
            print(num)

def e3():

    pontos_vitoria = int(input("Digite a quantidade de pontos para vencer: "))

    jogador1_pontos = 0
    jogador2_pontos = 0

    while jogador1_pontos < pontos_vitoria and jogador2_pontos < pontos_vitoria:
        print("Escolha sua jogada:")
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")

        jogador1_jogada = int(input("Jogador 1: "))
        jogador2_jogada = int(input("Jogador 2: "))

        if jogador1_jogada == jogador2_jogada:
            print("Empate!")
        elif (
            (jogador1_jogada == 1 and jogador2_jogada == 3) or
            (jogador1_jogada == 2 and jogador2_jogada == 1) or
            (jogador1_jogada == 3 and jogador2_jogada == 2)
        ):
            print("Jogasdor 1 ganhou a rodada!")
            jogador1_pontos += 1
        else:
            print("Jogador 2 ganhou a rodada!")
            jogador2_pontos += 1

        print("Pontuação:")
        print("Jogador 1:", jogador1_pontos)
        print("Jogador 2:", jogador2_pontos)
        print()

    if jogador1_pontos >= pontos_vitoria:
        print("Jogador 1 venceu o jogo!")
    else:
        print("Jogador 2 venceu o jogo!")

def e4():
    numero = []
    for i in range(5):

        num = int(input("Digite um numero: "))
        numero.append(num)

    sequencia = sorted(numero)
    print("A ordem é: ", sequencia)

def e5():
    paisA = 5000000 #3% ao ano
    taxaA = 0.03
    paisB = 7000000 #2% ao ano
    taxaB = 0.02
    ano = 0

    while paisA <= paisB :
        paisA += paisA * taxaA
        paisB += paisB * taxaB
        ano += 1
    
    print(f"Levara {ano:.0f} anos para o pais A ter a população de pais B\nPopulação de pais A {paisA:.0f}\nPopulação de pais B {paisB:.0f}")

def e6():

    nome = input("Digite seu nome completo: ")

    primeiro_nome = nome.split()[0]
    
    print(f"seu primeiro nome é: {primeiro_nome}")

def e7():
    
    caractere = 'a'
    frase = input("Digite uma frase: ")
    frases = list(frase)

    while not frase == '':
        frase = input("Digite uma frase: ")
        frases.extend(frase)
        count = frases.count(caractere)

    print("frases escrita: ", frases,"\nquantidade de letras 'a': ", count)

def e8():

    binario = input("Digite um número binário: ")
    decimal = 0
    potencia = 0

    for digito in reversed(binario):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1

    print("O número decimal equivalente é:", decimal)

def e9():
    decimal = int(input("Digite um número decimal: "))
    hexadecimal = ""

    while decimal > 0:
        resto = decimal % 16
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = chr(resto + 55) + hexadecimal
        decimal = decimal // 16

    print("O número hexadecimal equivalente é:", hexadecimal)

def e10():
    data1_str = input("Digite a primeira data (formato: dd/mm/aaaa): ")
    data2_str = input("Digite a segunda data (formato: dd/mm/aaaa): ")

    dia1, mes1, ano1 = map(int, data1_str.split("/"))
    dia2, mes2, ano2 = map(int, data2_str.split("/"))

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if ano1 % 4 == 0 and (ano1 % 100 != 0 or ano1 % 400 == 0):
        dias_por_mes[1] = 29
    if ano2 % 4 == 0 and (ano2 % 100 != 0 or ano2 % 400 == 0):
        dias_por_mes[1] = 29

    total_dias = 0

    if ano1 == ano2:
        if mes1 == mes2:
            total_dias = dia2 - dia1
        else:
            total_dias += dias_por_mes[mes1 - 1] - dia1
            for mes in range(mes1 + 1, mes2):
                total_dias += dias_por_mes[mes - 1]
            total_dias += dia2
    else:
        total_dias += dias_por_mes[mes1 - 1] - dia1
        for mes in range(mes1 + 1, 13):
            total_dias += dias_por_mes[mes - 1]
        for ano in range(ano1 + 1, ano2):
            if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
                total_dias += 366
            else:
                total_dias += 365
        for mes in range(1, mes2):
            total_dias += dias_por_mes[mes - 1]
        total_dias += dia2

    print("A quantidade de dias entre as duas datas é:", total_dias)
