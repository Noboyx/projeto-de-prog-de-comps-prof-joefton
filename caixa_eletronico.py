def mostrar_menu():
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

def ver_saldo(saldo):
    print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

def depositar(saldo):
    try:
        valor = float(input("Digite o valor para depósito: R$ "))
        if valor > 0:
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido. O valor precisa ser positivo.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
    return saldo

def sacar(saldo):
    try:
        valor = float(input("Digite o valor para saque: R$ "))
        if valor <= 0:
            print("Valor inválido. O valor precisa ser positivo.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
    return saldo

def caixa_eletronico():
    saldo = 0.0
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ver_saldo(saldo)
        elif opcao == "2":
            saldo = depositar(saldo)
        elif opcao == "3":
            saldo = sacar(saldo)
        elif opcao == "4":
            print("Encerrando o sistema. Obrigado por utilizar nossos serviços.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
caixa_eletronico()
ARQUIVO_SALDO = "caixa_eletronico.py"

def carregar_saldo():
    try:
        with open(ARQUIVO_SALDO, "r") as arquivo:
            return float(arquivo.read())
    except FileNotFoundError:
        return 0.0  # saldo inicial se o arquivo não existir
    except ValueError:
        return 0.0  # caso o conteúdo esteja corrompido

def salvar_saldo(saldo):
    with open(ARQUIVO_SALDO, "w") as arquivo:
        arquivo.write(f"{saldo:.2f}")

def ver_saldo(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")

def depositar(saldo):
    try:
        valor = float(input("Digite o valor para depósito: R$ "))
        if valor > 0:
            saldo += valor
            salvar_saldo(saldo)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido.")
    except ValueError:
        print("Entrada inválida.")
    return saldo

def sacar(saldo):
    try:
        valor = float(input("Digite o valor para saque: R$ "))
        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("Valor inválido.")
        else:
            saldo -= valor
            salvar_saldo(saldo)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    except ValueError:
        print("Entrada inválida.")
    return saldo

def mostrar_menu():
    print("\n=== MENU SALDO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

def executar_controle_de_saldo():
    saldo = carregar_saldo()
    
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            ver_saldo(saldo)
        elif opcao == "2":
            saldo = depositar(saldo)
        elif opcao == "3":
            saldo = sacar(saldo)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

executar_controle_de_saldo()

import controle_saldo

# Usuários cadastrados: login e senha
usuarios = {
    "joaopedro": "1010",
    "jeofton": "1030",
    "lucas": "1020"
   
}

def fazer_login():
    print("=== LOGIN ===")
    tentativas = 3
    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario in usuarios and usuarios[usuario] == senha:
            print(f"\nBem-vindo(a), {usuario}!\n")
            return True
        else:
            tentativas -= 1
            print(f"Login inválido. Tentativas restantes: {tentativas}")

    print("Acesso bloqueado. Tente novamente mais tarde.")
    return False

def mostrar_menu():
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

def caixa_eletronico():
    if not fazer_login():
        return

    saldo = controle_saldo.carregar_saldo()
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            controle_saldo.ver_saldo(saldo)
        elif opcao == "2":
            saldo = controle_saldo.depositar(saldo)
        elif opcao == "3":
            saldo = controle_saldo.sacar(saldo)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Executar
caixa_eletronico()




