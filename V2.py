def menu():
    return """
[d] Depositar
[s] Sacar
[e] Extrato
[a] Adicionar Usuário
[c] Criar Conta Corrente
[q] Sair

=> """

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    valor = float(input("Informe o valor do saque: "))
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
    return saldo, extrato, numero_saques

def extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def adicionar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
    cpf = input("Digite o CPF do usuário (apenas números): ")

    if cpf in usuarios:
        print("CPF já cadastrado!")
        return

    endereco = input("Digite o endereço do usuário: ")
    usuarios[cpf] = {'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco}
    print("Usuário adicionado com sucesso!")

def criar_conta_corrente(contas, agencia):
    cpf = input("Digite o CPF do usuário para criar a conta corrente: ")

    if cpf not in usuarios:
        print("CPF não encontrado!")
        return

    if cpf not in contas:
        contas[cpf] = {'agencia': agencia, 'numero_conta': 1, 'usuario': usuarios[cpf]}
    else:
        nova_conta = {'agencia': agencia, 'numero_conta': contas[cpf][-1]['numero_conta'] + 1, 'usuario': usuarios[cpf]}
        contas[cpf].append(nova_conta)

    print("Conta corrente criada com sucesso!")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = {}
contas = {}
agencia = "0001"

while True:
    opcao = input(menu())

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
    elif opcao == "e":
        extrato(saldo, extrato)
    elif opcao == "a":
        adicionar_usuario(usuarios)
    elif opcao == "c":
        criar_conta_corrente(contas, agencia)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
