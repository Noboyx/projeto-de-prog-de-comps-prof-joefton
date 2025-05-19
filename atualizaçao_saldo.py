ARQUIVO_SALDO = "saldo.txt"

def carregar_saldo():
    try:
        with open(ARQUIVO_SALDO, "r") as arquivo:
            return float(arquivo.read())
    except FileNotFoundError:
        return 0.0  # Se o arquivo não for achado o retorno do saldo inicial será 0
    except ValueError:
        return 0.0  # Caso o conteúdo esteja corrompido o retorno do saldo inicial 0 

def salvar_saldo(saldo):
    with open(ARQUIVO_SALDO, "w") as arquivo:
        arquivo.write(f"{saldo:.2f}")

def ver_saldo(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")

def depositar(saldo): # Ao depositar vai mostrar o novo saldo
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

def sacar(saldo): # Ao sacar vai mostrar o novo saldo depois do seu saque
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

def mostrar_menu(): # Menu de operações para o caixa eletonico
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
            #Fim do trabalho
            print("Opção inválida.")

# Iniciar
executar_controle_de_saldo()
