menu = """
Clientes
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar conta
[l] Login
--------------------
Função exclusiva adm
[V] Verificar contas
--------------------
[q] Sair

=> """
user = ''
saldo = 0
contas = []
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = {}
AGENCIA = "0001"
numero_conta_sequencial = 1
cpf_logado = None


def depositar(saldo,extrato,valor):
       if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
       else:
           print('Operacao falhuo! Valor informado é invalido')

       return saldo, extrato
        

def saque(*,saldo,valor,extrato,numero_saques):
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")


        return saldo , extrato , numero_saques

def visualizarHistorico(saldo,sessao,*,extrato):
        print("\n================ EXTRATO ================")
        print("\n================ Usuario ================")
        print(f"\n================ {sessao} ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


def visualizar_dados():
    if not usuarios:
        print("Nenhuma conta cadastrada")
    else:
        print("\n======= USUÁRIOS =======")
        for cpf, dados in usuarios.items():
            print(f"CPF: {cpf}")
            print(f" Nome: {dados['nome']}")
            print(f" Nascimento: {dados['data_nascimento']}")
            print(f" Endereço: {dados['endereco']}")
            print(f" Contas: {dados['contasCorrente']}")
            print("------------------------")

        print("\n======= CONTAS =======")
        for conta in contas:
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | CPF: {conta['cpf']}")

     

def createUser(usuarios):
    print("\n================ Criacao de usuario ================")

    cpf = input("cadastre o CPF (somente números): ")
   
    if cpf in usuarios:
        print("Já existe usuário com esse CPF!")
        return usuarios[cpf]
    
    nome = input("cadastre o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")
    print("==========================================")
    
    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "contasCorrente":[]
    }


    numero_conta = createAccount(cpf)

    usuarios[cpf]["contasCorrente"].append(numero_conta)
   

    print("Usuário e conta criados com sucesso!")
    return usuarios[cpf]

def createAccount(cpf):
    global numero_conta_sequencial

    conta = {
        "agencia": AGENCIA,
        "numero": numero_conta_sequencial,
        "cpf": cpf,
    }

    contas.append(conta)
    numero_conta_sequencial += 1
    
    
    return conta["numero"]



def login():
     global cpf_logado
     print("================LOGIN================")
     cpf = input("Informe o CPF (somente números): ")

     if cpf in usuarios or cpf == '000':
        if cpf == "000":
            print("bem vindo Administrador")
        else:
           print(f"bem vindo {usuarios[cpf]['nome']}")
     else:
        print(f"o CPF:{cpf} não foi encontrado em nossos sistemas, direcionando para sistema de cadastros.")
        createUser(usuarios) 
        print(f"bem vindo {usuarios[cpf]['nome']}")
     

     cpf_logado = cpf
     return

def menu_operation():   
    global saldo, extrato, numero_saques, usuarios
    while True:
        user = "ADM" if cpf_logado == "000" else "USER"
        opcao = input(menu)
        if cpf_logado:
          if cpf_logado =='000':
            sessao = 'Administrador'
          else:
            sessao = usuarios[cpf_logado]['nome']
        else:
            sessao = 'Convidado'
        if opcao == "d":
            valor = float(input(f"{sessao}, informe o valor do depósito: "))
            saldo,extrato = depositar(saldo,extrato,valor,)


        elif opcao == "s":
            valor = float(input(f"{sessao}, Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(
                valor=valor,saldo=saldo,extrato=extrato,numero_saques=numero_saques
            )
    

        elif opcao == "e":
           
            visualizarHistorico(saldo,sessao,extrato=extrato)

        elif opcao== "c":
            createUser(usuarios)
        elif opcao == "l":
            login()

        
        elif opcao == "v":
            if user == "ADM": 
              visualizar_dados()
            else:
                print("Usuario sem permissao")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    return
menu_operation()