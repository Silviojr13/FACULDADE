
def e1():
    def decomposicao(num):
    
        decomposicao_texto = ""
        tamanho = len(str(num))
        for i, digito in enumerate(str(num)):
            expoente = tamanho - i - 1
            if digito != "0":
                if expoente == 0:
                    decomposicao_texto += f"{digito}"
                elif expoente == 1:
                    decomposicao_texto += f"{digito} x 10"
                else:
                    decomposicao_texto += f"{digito} x 10^{expoente}"
                if i != tamanho - 1:
                    decomposicao_texto += " + "
        return decomposicao_texto

    # Exemplo de uso:
    numero = float(input("digite um numero: "))
    print(f"Decomposição: {decomposicao(numero)}")
    continuar()

def e2():
    numero = int(input("digite um numero para verificar se é ou não perfeito: "))

    soma = 0

    for i in range(1,numero):
        if numero % i == 0:
            soma += 1
            if soma == numero:
                print(numero, "é um número perfeito")
            else:
                print(numero, "não é um número perfeito")
                continuar()
    

def e3():
    string = input("Escreva uma frase: ")
    stringSemEspacos = string.replace(' ', '')
    stringTodaMinuscula = stringSemEspacos.lower()
    stringInvertida = stringTodaMinuscula[::-1]
    if stringInvertida == stringTodaMinuscula:
        print("SIM")
    else:
        print("NAO")
        continuar()


def e4():
    a1 = float(input("Digite o primeiro termo da PG: "))
    q = float(input("Digite a razão da PG: "))
    n = int(input("Digite o número sequencial do elemento da PG que deseja calcular: "))

    # Calcula o enésimo termo da PG
    an = a1 * q ** (n - 1)

    # Exibe o resultado
    print("O", n, "º termo da PG é", an)
    continuar()

def e5():
    C = float(input("Digite o valor inicial da aplicação: "))
    i = float(input("Digite a taxa de juros ao mês (em porcentagem): ")) / 100
    n = int(input("Digite o tempo de aplicação em meses: "))

    # Calcula o montante final com juros compostos
    M = C * (1 + i) ** n

    # Exibe o resultado
    print("O montante final com juros compostos é de R$", round(M, 2))
    continuar()

def opcaos():
    print("")
    print("="*50)
    print("escolha um exercicio")
    print("Exercicio - 1")
    print("Exercicio - 2")
    print("Exercicio - 3")
    print("Exercicio - 4")
    print("Exercicio - 5")
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


def continuar():
    print("")
    escolha = input("Deseja continuar (s/n)?: ")
    if escolha == 's':
        opcaos()
    elif escolha == 'n':
        print("")
        print("Obrigado por utilizar!!\n")
        
opcaos()