
# em meus estudos com documentos da oficina de meu pai vi que o sistema calcula em meses e o resultado tbm é em meses 
# por isso manti os resultados sem multiplicar por 12 pois antes era multiplicado o que gerou erro no código

def rendimentoMensal(rendimento=float, numeroDeDependentes=int, pensao=float, outrasDeducoes=float):
    deducaoPorDependente = 189.59
    deducaoTotal = deducaoPorDependente * numeroDeDependentes
    baseDeCalculo = rendimento - (deducaoTotal + pensao + outrasDeducoes)
    
    # observação: troquei a posição dos print para melhor visualização do código
    print(f'Rendimento mensal: R$ {rendimento:.2f}')
    print(f'Número de dependentes: {numeroDeDependentes}')
    print(f'Valor da pensão alimentícia: R$ {pensao:.2f}')
    print(f'Outras deduções: R$ {outrasDeducoes:.2f}')

    if baseDeCalculo <= 1903.98:
        imposto = 0
        aliquota = 0
    elif baseDeCalculo <= 2826.65:
        imposto = (baseDeCalculo - 1903.98) * 0.075
        aliquota = 7.5
    elif baseDeCalculo <= 3751.05:
        imposto = (baseDeCalculo - 2826.65) * 0.15 + 69.93
        aliquota = 15.0
    elif baseDeCalculo <= 4664.68:
        imposto = (baseDeCalculo - 3751.05) * 0.225 + 345.74
        aliquota = 22.5
    else:
        imposto = (baseDeCalculo - 4664.68) * 0.275 + 773.87
        aliquota = 27.5

    print("=" * 50)
    print(f'Imposto a pagar: R$ {imposto:.2f}')
    print(f'Faixa de rendimento: {aliquota}%')
    print(f'Taxa efetiva: {imposto / baseDeCalculo:.2%}')
    simNao()

def rendimentoMes():

    # estrutura de input onde realiza comparação no caso onde o usuario não insira um numero ou coloque letras
    # é solicitado que insira corretamente os valores.
    rendimento = input("Insira o seu salário: ")
    while not rendimento.isnumeric():
        print("Informe um valor numérico!")
        rendimento = input("Insira o seu salário: ")
    rendimento = float(rendimento)

    numeroDeDependentes = input("Insira o número de dependentes: ")
    while not numeroDeDependentes.isnumeric():
        print("Informe um valor numérico!")
        numeroDeDependentes = input("Insira o número de dependentes: ")
    numeroDeDependentes = int(numeroDeDependentes)

    pensao = input("Insira o valor da pensão alimentícia: ")
    while not pensao.isnumeric():
        print("Informe um valor numérico!")
        pensao = input("Insira o valor da pensão alimentícia: ")
    pensao = float(pensao)

    outrasDeducoes = input("Insira o valor de outras deduções: ")
    while not outrasDeducoes.isnumeric():
        print("Informe um valor numérico!")
        outrasDeducoes = input("Insira o valor de outras deduções: ")
    outrasDeducoes = float(outrasDeducoes)

    rendimentoMensal(rendimento, numeroDeDependentes, pensao, outrasDeducoes)

#====codigo a baixo gera um loop com saida do mesmo=========
def simNao():
    simounao = input('deseja repetir (s/n):')
    if simounao == 's':
        rendimentoMes()
    else: 
        print('obrigado por ultilizar!!')
        
rendimentoMes()     