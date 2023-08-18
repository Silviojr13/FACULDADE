
#============= Listas =================
estudantess = []
lista_vazia = []

#======================================


#=========== Menu principal ===========
def menuprincipal():
    print('-' * 30)
    print('        MENU PRINCIPAL')
    print('-' * 30)
    print()
    print("Digite (1) para Gerenciar Estudantes.")
    print("Digite (2) para Gerencia Disciplinas.")
    print("Digite (3) para Gerenciar Professores.")
    print("Digite (4) para Gerenciar Matrículas.")
    print("Digite (5) para Sair.")
    opcao = int(input("Informe a opção desejada: "))
    if opcao == 1:
        estudantes()
    elif opcao == 2:
        print("EM DESENVOLVIMENTO")
        print('Escolha outra Opção')
        
        menuprincipal()
    elif opcao == 3:
        print("EM DESENVOLVIMENTO")
        print('Escolha outra Opção')
        menuprincipal()
    elif opcao == 4:
        print("EM DESENVOLVIMENTO")
        print('Escolha outra Opção')
        menuprincipal()
    elif opcao == 5:
        print("OBRIGADO POR UTILIZAR")
    else:
        print("ESCOLHA UMA OPÇÃO EXISTENTE !!!")
        menuprincipal()
 #============== FIM DO menu principal ================



#================== Gerenciar Estudante ================

def estudantes():
    print()

    print("Gerenciar Estudantes!")
    print()
    print("**MENU DE OPERAÇOES**")
    print("Digite (1) para Incluir.")
    print("Digite (2) para Listar.")
    print("Digite (3) para Atualizar.")
    print("Digite (4) para Excluir")
    print("Digite (5) para Menu Principal.")
    print()

    #-------- INCLUIR = DEFINICAO ---------
    opcaoo2 = int(input("Informe a opção desejada: "))

    if opcaoo2 == 1:
        incluir(opcaoo2)
    elif opcaoo2 == 2:
        listaestudantes()
    elif opcaoo2 == 3:
        print("EM DESENVOLVIMENTO")
        menuprincipal()
    elif opcaoo2 == 4:
        print("EM DESENVOLVIMENTO")
        menuprincipal()
    elif opcaoo2 == 5:
        print("EM DESENVOLVIMENTO")
        menuprincipal()
    elif opcaoo2 == 6:
        print("EM DESENVOLVIMENTO")
        menuprincipal()
    else:
        print("ESCOLHA UMA OPÇÃO EXISTENTE !!!")
        estudantes()
# CODIGO ABAIXO PERTENCE A GERNECIAR ESTUDANTES


def incluir(opcaoo2: int):

    print("        INCLUIR!")
    nome = input("Informe o nome do Estudante:")
    nomeusuario(nome)


def nomeusuario(nome: float):
    estudantess.append(nome)
    print("        Lista!")
    print("Nome do usuario: ", nome)
    
    decisao = input("DESEJA VOLTAR PARA O MENU ESTUDANTES (s/n): ")
    if decisao == 's':
        estudantes()
    elif decisao == 'n':
        menuprincipal()
# FIM DO CODIGO GERENCIAR ESTUDANTES
# INICIO DA LISTA DE ESTUDANTES


def listaestudantes():
    print("LISTA DE REGISTRADOS")
    
    if not estudantess:
        print("Não ha estudante cadastrados")
    else:
        for est in estudantess:
            print("-",est)
    
    voltar = input("Pressione ENTER para Continuar")
    if voltar == "":
        menuprincipal()


# COMEÇO DO GERENCIAR DISCIPLINAS
# variavel de chamada do codigo

menuprincipal()