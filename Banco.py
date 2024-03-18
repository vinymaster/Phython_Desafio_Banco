menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depositou: R$ {valor:.2f}\n"
            print("depósito efetuado com sucesso!")

        else:
            print("Utilize somente valores positivos.")

    elif opcao == "s":
        valor = float(input("Informe o valor a sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Quantidade de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Retirou: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque efetuado com sucesso!")


        else:
            print("Utilize somente valores positivos.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação não permitida, escolha o menu correto!")