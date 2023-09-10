

# Exercicio == 1
def e1():
    print("")
    altura = float(input("Digite a altura da pessoa em metros: "))
    sexo = input("Digite o sexo da pessoa (M ou F): ")

    if sexo == "M":
        peso_ideal = (72.7 * altura) - 58
        print(f"O peso ideal para um homem de {altura:.2f}m é de {peso_ideal:.2f}kg.")
    elif sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"O peso ideal para uma mulher de {altura:.2f}m é de {peso_ideal:.2f}kg.")
    else:
        print("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")
    continuar()
# =======================================================================================================
# =======================================================================================================
# =======================================================================================================

# Exercicio 2

def e2():
    print("")
    peso = float(input("Digite o seu peso (em kg): "))
    altura = float(input("Digite a sua altura (em metros): "))

    imc = peso / altura ** 2

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        print("Peso normal")
    elif imc >= 25 and imc < 30:
        print("Acima do peso")
    else:
        print("Obeso")
    continuar()

# =======================================================================================================
# =======================================================================================================
# =======================================================================================================

# Exercicio 3

def e3():
    print("")
    print("Jogo de Par ou Ímpar\n")

    jogador1_palpite = input("Jogador 1: Par ou Ímpar? ").lower()
    while jogador1_palpite not in ['par', 'ímpar']:
        print("Palpite inválido! Digite 'par' ou 'ímpar'.")
        jogador1_palpite = input("Jogador 1: Par ou Ímpar? ").lower()

    jogador1_valor = int(input("Jogador 1, digite um número : "))
    

    jogador2_valor = int(input("Jogador 2, digite um número: "))
    

    soma_valores = jogador1_valor + jogador2_valor
    print(f"\nJogador 1 escolheu {jogador1_valor} e Jogador 2 escolheu {jogador2_valor}.")
    print(f"A soma dos valores é {soma_valores}.\n")

    if soma_valores % 2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"

    if resultado == jogador1_palpite:
        print("Jogador 1 ganhou!")
    else:
        print("Jogador 2 ganhou!")
    continuar()
# =======================================================================================================
# =======================================================================================================
# =======================================================================================================

# Exercicio 4

def e4():
    print("")
    preco_etiqueta = float(input("Digite o preço normal do produto: "))
    print("")
    print("formas de pagamento")
    print("1 - À vista ou cheque")
    print("2 - À vista no cartão de crédito")
    print("3 - Em 2x sem juros")
    print("4 - Em 2x com juros de 10%")
    condicao_pagamento = int(input("Digite o código da condição de pagamento (1 a 4): "))

    if condicao_pagamento == 1:
        preco_final = preco_etiqueta * 0.9
    elif condicao_pagamento == 2:
        preco_final = preco_etiqueta * 0.85
    elif condicao_pagamento == 3:
        preco_final = preco_etiqueta
    else:
        preco_final = preco_etiqueta * 1.1

    if condicao_pagamento == 3:
        parcelas = 2
        valor_parcela = preco_final / parcelas
        print("O produto será parcelado em {}x de R$ {:.2f} sem juros.".format(parcelas, valor_parcela))
    elif condicao_pagamento == 4:
        parcelas = 2
        valor_parcela = preco_final / parcelas
        parce = preco_final / 2
        print("O produto será parcelado em {}x de R$ {:.2f} com juros.".format(parcelas, parce))
    else:
        print("O produto será pago à vista com desconto de 10%.")

    print("O preço final a ser pago é R$ {:.2f}.".format(preco_final))
    continuar()
# =======================================================================================================
# =======================================================================================================
# =======================================================================================================
# Exercicio 5

def e5():

    
    print("\nDestinos de viagem\nNorte\nSul\nNordeste\n")

    destino = input("Digite o destino da viagem: ")
    ida_e_volta = input("A viagem inclui retorno (ida e volta)? (s/n): ")

    if destino == "Norte":
        if ida_e_volta == "s":
            preco_passagem = 900.00
        else:
            preco_passagem = 500.00
    elif destino == "Nordeste":
        if ida_e_volta == "s":
            preco_passagem = 650.00
        else:
            preco_passagem = 350.00
    elif destino == "Centro-Oeste":
        if ida_e_volta == "s":
            preco_passagem = 600.00
        else:
            preco_passagem = 350.00
    elif destino == "Sul":
        if ida_e_volta == "s":
            preco_passagem = 550.00
        else:
            preco_passagem = 300.00
    else:
        print("Destino inválido!")
        exit()

    print(f"O preço da passagem para {destino}{' (ida e volta)' if ida_e_volta == 'S' else ''} é R$ {preco_passagem:.2f}")
    continuar()
# =======================================================================================================
# =======================================================================================================
# =======================================================================================================
# Exercicio 6

def e6():
    print("")
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))

    # cálculo do delta
    delta = b**2 - 4*a*c

    # verificação das raízes
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação possui apenas uma raiz real: x = {x:.2f}")
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print(f"A equação possui duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}")
    continuar()
# =======================================================================================================
# =======================================================================================================
# =======================================================================================================
# Exercicio 7

def e7():
    print("")
    dia = int(input("Digite o dia de nascimento: "))
    mes = int(input("Digite o mês de nascimento: "))
    ano = int(input("Digite o ano de nascimento: "))

    formato = int(input("Digite o código de exibição de data (1 para simples, 2 para abreviada, 3 para completa): "))

    if formato == 1:
        if  mes <10 :
            print("{}/0{}/{}".format(dia, mes, ano))
        else:
            print("{}/{}/{}".format(dia, mes, ano))
    elif formato == 2:
        if mes == 1:
            mes_abrev = "jan"
        elif mes == 2:
            mes_abrev = "fev"
        elif mes == 3:
            mes_abrev = "mar"
        elif mes == 4:
            mes_abrev = "abr"
        elif mes == 5:
            mes_abrev = "mai"
        elif mes == 6:
            mes_abrev = "jun"
        elif mes == 7:
            mes_abrev = "jul"
        elif mes == 8:
            mes_abrev = "ago"
        elif mes == 9:
            mes_abrev = "set"
        elif mes == 10:
            mes_abrev = "out"
        elif mes == 11:
            mes_abrev = "nov"
        elif mes == 12:
            mes_abrev = "dez"
        print("{}/{}/{}".format(dia, mes_abrev, ano))
    elif formato == 3:
        if mes == 1:
            mes_extenso = "janeiro"
        elif mes == 2:
            mes_extenso = "fevereiro"
        elif mes == 3:
            mes_extenso = "março"
        elif mes == 4:
            mes_extenso = "abril"
        elif mes == 5:
            mes_extenso = "maio"
        elif mes == 6:
            mes_extenso = "junho"
        elif mes == 7:
            mes_extenso = "julho"
        elif mes == 8:
            mes_extenso = "agosto"
        elif mes == 9:
            mes_extenso = "setembro"
        elif mes == 10:
            mes_extenso = "outubro"
        elif mes == 11:
            mes_extenso = "novembro"
        elif mes == 12:
            mes_extenso = "dezembro"
        print("{:02d} de {} de {}".format(dia, mes_extenso, ano))
    else:
        print("Código inválido de exibição de data!")
    continuar()
# =======================================================================================================
# =======================================================================================================
# =======================================================================================================
# Exercicio 8
def e8():
    print("")
    # solicita a data com hora
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    hora = int(input("Digite a hora: "))
    minuto = int(input("Digite o minuto: "))
    segundo = int(input("Digite o segundo: "))

    # solicita a informação a ser acrescentada e a quantidade
    info = input("Digite a informação a ser acrescentada (dia, mês, ano, hora, minuto, segundo): ")
    quantidade = int(input("Digite a quantidade a ser acrescentada: "))

    # adiciona a informação e a quantidade
    if info == "dia":
        dia += quantidade   
    elif info == "mês":
        mes += quantidade
    elif info == "ano":
        ano += quantidade
    elif info == "hora":
        hora += quantidade
    elif info == "minuto":
        minuto += quantidade
    elif info == "segundo":
        segundo += quantidade

    # ajusta a data e a hora
    while segundo >= 60:
        segundo -= 60
        minuto += 1
    while minuto >= 60:
        minuto -= 60
        hora += 1
    while hora >= 24:
        hora -= 24
        dia += 1
        if mes == 2 and (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
            if dia > 29:
                dia = 1
                mes += 1
        elif mes in [4, 6, 9, 11]:
            if dia > 30:
                dia = 1
                mes += 1
        else:
            if dia > 31:
                dia = 1
                mes += 1
            if mes > 12:
                mes = 1
                ano += 1

    # exibe a nova data
    print("{:02}/{:02}/{:04} {:02}:{:02}:{:02}".format(dia, mes, ano, hora, minuto, segundo))
    continuar()

# =======================================================================================================
# =======================================================================================================
# =======================================================================================================                         
# Exercicio 9  

def e9():
    print("")
    # Solicita os dígitos do CPF separadamente
    cpf = ""
    for i in range(11):
        cpf += input(f"Digite o {i+1}º dígito do CPF: ")

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        print("CPF inválido")
    else:
        # Converte o CPF em uma lista de inteiros
        cpf = [int(d) for d in cpf]

        # Calcula o primeiro dígito verificador
        soma = sum(cpf[i] * (10 - i) for i in range(9))
        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto

        # Verifica o primeiro dígito verificador
        if digito1 != cpf[9]:
            print("CPF inválido")
        else:
            # Calcula o segundo dígito verificador
            soma = sum(cpf[i] * (11 - i) for i in range(10))
            resto = soma % 11
            if resto < 2:
                digito2 = 0
            else:
                digito2 = 11 - resto

            # Verifica o segundo dígito verificador
            if digito2 != cpf[10]:
                print("CPF inválido")
            else:
                print("CPF válido")

    continuar()


# lista de chamada de cada questão

def opcaos():
    print("")
    print("="*50)
    print("escolha um exercicio")
    print("Exercicio - 1")
    print("Exercicio - 2")
    print("Exercicio - 3")
    print("Exercicio - 4")
    print("Exercicio - 5")
    print("Exercicio - 6")
    print("Exercicio - 7")
    print("Exercicio - 8")
    print("Exercicio - 9")
    print("")
    opcao = float(input("escolha uma das questões a cima e insira o número equivalente: "))
    if opcao == 1:
        e1()
    elif opcao == 2:
        e2()
    elif opcao == 3:
        e3()
    elif opcao == 4:
        e4()
    elif opcao == 5:
        e5()
    elif opcao == 6:
        e6()
    elif opcao == 7:
        e7()
    elif opcao == 8:
        e8()
    elif opcao == 9:
        e9()
  


def continuar():
    print("")
    escolha = input("Deseja continuar (s/n)?: ")
    if escolha == 's':
        opcaos()
    elif escolha == 'n':
        print("")
        print("Obrigado por ultilizar!!\n")



opcaos(); 