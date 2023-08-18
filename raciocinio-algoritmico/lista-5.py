
# lista em sala

def e1Errado():
    nums = [0,0,0,0]
    for i in range(5):
        num = int(input("Digite um número: "))
        nums [i] = num
    print(nums)

def e1():
    nums = []
    for i in range(5):
        num = int(input("Digite um número: "))
        nums.append(num)
    print(nums)

def e2Errado():
    pares = []
    impares = []
    for i in range(5):
        num = int(input("Digite um número: "))
        if num % 2 == 0 :
            pares.append(num)
        else:
            impares.append
    print("Numeros pares:",pares,"- numeros impares: ",impares)

def e3():
    nums = [1, 4, 23, 11, 8]
    for i in range(len(nums)):
        print(nums[i])

def e4():
    nums = [17, 33 ,23, 11, 8, 15, 9]
    maior = nums[0]
    menor = nums[0]
    for num in nums:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    print("O maior numero da lista é ",maior,"e o menor",menor)
    
def e5():
    nums = [17, 33, 23, 11, 8, 15, 9]
    aux= 0
    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[1] > nums[i+1]:

                aux= nums[1]
                nums[i] = nums[i+1]
                nums [i+1] = aux
                
    print(nums)

def e6():
    coordenadas = []
    for i in range(3):
        x = int(input("Insira um valor de x: "))
        y = int(input("Insira um valor de y: "))
        coordenadas.append([x,y])
    print(coordenadas)

    for x, y in coordenadas:
        print("")
        print("Coordenada x: ",x)
        print("Coordenada y: ",y)
        print("")

def e7():
    nomes = []
    while True:
        nome = input("Digite o nome: ")
        if nome == 'sair':
            break
        sobrenome = input("Digite o sobrenome: ")
        nome_completo = [nome, sobrenome]
        nomes.append(nome_completo)
    for nome in nomes:
        print(nome[1] + ", " + nome[0])


def e8():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    soma = 0
    for i in range(3):
        for j in range(3):
            soma += m[i][j]
    print("A soma dos elementos da matriz m é igual a", soma)


def e9():
    notas = []
    for _ in range(7):
        nota = float(input("Entre com uma das notas: "))
        notas.append(nota)
        menor = min(notas)
    if notas.count(menor) == 1: 
        notas.remove(menor)
    else:
        indice = -1
        for i in range(len(notas)):
            if notas[i] == menor:
                indice = i
                break
            notas.pop(indice)
            maior = max(notas)
            if notas.count(maior) == 1:
                notas.remove(maior)
            else:
                indice = -1
                for i in range(len(notas)):
                    if notas[i] == maior:
                        indice = i
                        break
                notas.pop(indice)
            soma = sum(notas)
            print(f"A pontuação do salto foi {soma:.1f}")
        
# lista de tarefa exercicios sala

def e10():

    # exercico 1

    numeros = []
    for i in range(6):
        numero = float(input("Digite um número: "))
        numeros.append(numero)

    media = sum(numeros) / len(numeros)

    acima_ou_igual = []
    abaixo = []

    for numero in numeros:
        if numero >= media:
            acima_ou_igual.append(numero)
        else:
            abaixo.append(numero)

    print("Números iguais ou acima da média:", acima_ou_igual)
    print("Números abaixo da média:", abaixo)

def e11():

    #exercicio 2

    lista1 = [0, 0, 0, 0, 0]
    lista2 = [0, 0, 0, 0, 0]

    for i in range(5):

        l1 = int(input("Digite um número da lista 1 :"))
        lista1.append(l1)

    print ("")

    for i in range(5):

        l2 = int(input("Digite um número da lista 2 :"))
        lista2.append(l2)

    lista3 = [lista1,lista2]
    print("a lista intercalada é:", lista3)

    

def opcaos():
    print("")
    print("="*50)
    print("escolha um exercicio")
    print("Exercicio 1 - 11 - Errado")
    print("Exercicio 1 - 1")
    print("Exercicio 2 - 2")
    print("Exercicio 3 - 3")
    print("Exercicio 4 - 4")
    print("Exercicio 5 - 5")
    print("Exercicio 6 - 6")
    print("Exercicio 7 - 7")
    print("Exercicio 8 - 8")
    print("Exercicio 9 - 9")
    print("Exercicio 10 - 10")
    print("Exercicio 11 - 11")
    print("")
    opcao = input("escolha uma das questões a cima e insira o número equivalente: ")
    if opcao == 1:
        e1Errado()
    elif opcao == 11:
        e1()
    elif opcao == 22:
        e2Errado()
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
    elif opcao == 10:
        e10()
    elif opcao == 11:
        e11()
   


opcaos()