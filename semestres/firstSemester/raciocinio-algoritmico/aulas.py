import sys

#------Aula dia 10/03/2023--------

#valorA = 10+5
#ValorB = (80*4)-1
#ValorC = ValorB/valorA +1
#ValorC = ValorC**2
#print("O resultado final é",ValorC)
#anotação
#--------------------------------------------

#idade = int(input("digite sua idade: "))
#print("em 2 anos você vai ter", idade+2)

#---------------------------------------------

#dado = input("Digite: ")
#idade = int(dado)
#peso =  float(dado)
#nome = dado

#----------------------------------------------

#print("Informe suas 3 notas da prova")
#n1 = float(input("Digite nota 1:"))
#n2 = float(input("Digite nota 2:"))
#n3 = float(input("Digite nota 3:"))
#media = (n1 + )

#==============================================
#==============================================

# Aula 17/03/2023

#ano_atual = 2020 
#nascimento = int(input("Qual o seu ano de nascimento? "))
#idade = ano_atual - nascimento
#resp = input("você ja fez aniversario este ano? ")
#if resp == "n":
#    idade -= 1
#print("Sua idade é ", idade)

#--------------------------------


def calculaMedia(nota1: float, nota2: float, nota3: float, nota4: float):
    MEDIA = 7.0
    mediaDoAluno = ((nota1 + nota2 + nota3 + nota4) /4)

    if  mediaDoAluno >= MEDIA:
        print("você foi aprovado🤖!!!!")
    else:
        print("você reprovou")

def pedeNotas():
    notaa1 = float(input("informe a primeira nota: "))
    notaa2 = float(input("informe a segunda nota: "))
    notaa3 = float(input("informe a terceira nota: "))
    notaa4 = float(input("informe a quarta nota: "))
    calculaMedia(nota1= notaa1, nota2= notaa2, nota3= notaa3, nota4= notaa4)

#pedeNotas()
#calculaMedia(nota1= 7.0, nota2= 7.0, nota3= 7.0, nota4= 7.0)

def compareNum(num1: float, num2: float, num3= float):
    
    valores = [num1,num2,num3]
    menorvalor = min(valores)
    print("seu menor valor é: ",menorvalor)
    maiorValor = sys.float_info.max
    print("maiorValor:",maiorValor)

def pedeNum():
    numero1 = float(input("insira o primeiro numero: "))
    numero2 = float(input("insira o segundo numero: "))
    numero3 = float(input("insira o terceiro numero: "))
    compareNum(numero1,numero2,numero3)

#pedeNum()

#======================= 20/03/2023====================

#imposto.py


#====================== 27/03/2023 ================

def sominha():
    soma = 0
    for i in  range(3):
        num = int(input("Digite o " + str(i + 1) +" numero: "))
        soma += num
    print("A soma dos numeros é",soma)
#sominha()

#2

#def sominha2():
#
#    fatorial = 1
#    expressao = "Expressão: "
#    num = int(input("Digite um número para o cálculo do fatorial: "))
#    for i in range(num);

def norvo():
    mult = 1
    for i in range(10):
        num = int(input("Digite o " + str(i + 1) + " numero: "))
        if num == 0:
            continue
        mult += num
    print("A multiplicação dos números é",mult)

    
#norvo()
#soma ate digitar  '0' para encerrar e puchar calculo! metodo "while"
def norrvo():
    soma = 0
    num = -1
    while num !=0:
        num = int(input("Digite um número para somar (0 finaliza)"))
        soma += num
    print("A soma dos numeros é ",soma)

#norrvo()


#================== 31/03/2023=====================

def teste():
    while True:
        try: 
            num = int(input("Digite um número: "))
            break
        except ValueError:
            print("Valor inválido")
    print("número validado:", num)
#teste()

def tesste():
    numero = int(input('Digite um inteiro:   '))
    
    if (numero%2) == 0:
        print("Par")
    else:
        print("Ímpar")

#tesste()
