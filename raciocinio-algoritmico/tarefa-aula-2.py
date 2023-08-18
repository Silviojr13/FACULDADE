# exercicio 1 "soma de dois numeros"

def soma(primeiro:float,segundo:float):
    
    result = primeiro + segundo
    print(f"sua soma: {result:9.0f}",)
    outra();

def valores():

    valor1 = float(input("insira o primeiro valor:"))
    valor2 = float(input("insira o segundo valor:"))
    soma(valor1,valor2)

# 2. Elaborar um algoritmo que solicita ao usuário seu ano de nascimento e calcula sua idade com
#    relação ao ano de 2023, sendo que o usuário já fez aniversário neste ano.

def idadee(idades:float,inf2:float):           

    if inf2 == 's':
        vari = 0;
    elif inf2 == 'n':
        vari = 1;
    else:
        print('insira a resposta correta!!')
        idade();
    
    iidade = 2023 - idades - vari
    print(f"sua idade é:{iidade:2.0f} ")
    outra();

def idade():

    inf1 = float(input("data de nascimento: "))
    inf2 = input("ja fez aniversario este ano? (s/n): ")
    idadee(inf1,inf2)
#   3. Elaborar um algoritmo que solicita ao usuário o nome de uma disciplina e suas quatro notas
#      bimestrais. O algoritmo deve calcular a média destas notas, e uma mensagem
#      informando a média da disciplina, nome é média.

def disciplina(dici:float,not1:float,not2:float,not3:float,not4:float):

    dici = input("Insira o nome da disciplina: ")
    not1 = float(input('Insira a primeira nota:'))
    not2 = float(input('Insira a segunda nota:'))
    not3 = float(input('Insira a terceira nota:'))
    not4 = float(input('Insira a quarta nota:'))

    somaa = (not1 + not2 + not3 + not4)/ 4  
    print("Sua média em ",dici," é: ",somaa)
    outra();

     
#   4. Elaborar um algoritmo que solicita o nome de um produto, seu valor e quantidade,
#      informando o valor de compra calculado.

def compra():

    prod = (input("Qual o produto desejado: "))
    preco = float(input("Insira o valor unitario do produto: "))
    quant = float(input("Qual a quantidade desejada:"))

    calc = quant * preco
    print("Valor total da compra do produto",prod,":",calc)
    outra()

#   5. Estender o exercício 4 anterior, informando que para pagamento à vista tem 15% de desconto,
#      calculando e exibindo este valor.

def compras():

    prod = (input("Qual o produto desejado: "))
    preco = float(input("Insira o valor unitario do produto: "))
    quant = float(input("Qual a quantidade desejada:"))

    calc = quant * preco
    cont = calc * 0.15
    contt = calc - cont
    print("Valor total da compra a vista com 15% de desconto do produto",prod,":",contt)
    outra()
    

def escolha():
    print("="*50)
    print('exercicos:')
    print('1-Soma')
    print('2-Idade:')
    print('3-nota')
    print('4-produto')
    print('5-descontinho')
    print("")
    exercicio = int(input("insira o numero do exercicio:"))
    if exercicio == 1:
        valores();
    elif exercicio == 2:
        idade();
    elif exercicio == 3:
        disciplina()
    elif exercicio == 4:
        compra()
    elif exercicio == 5:
        compras()
    else:
        print('este exercicio não existe!!')


def outra():
    desejaContinuar = input("deseja continuar? (s/n):")
    if desejaContinuar == 's':
        escolha();
    else:
        if desejaContinuar == 'n':
            print("obrigado por ultilizar o programa!!");

escolha()