saldo = 0
tentativas_saque = 3
quantidade_saque = 0
valor_total_saques = 0


while True:

    print("Bem Vindo ao Banco")
    print("==========")
    print("1)Deposito\n2)Saque\n3)Extrato\n4)Sair ")
    print("==========")
    opcao = int(input("Escolha a Operação:"))

    if opcao == 1:

        saldo += float(input("Digite o valor do Deposito: "))

    elif opcao == 2:

        saque = float(input("Digite o valor do Saque: "))

        while saque > 500:

            print("\nO saque deve ser menor que 500!\n ")
            saque = float(input("Digite o valor do Saque: "))

        if saldo < saque:

            print("\nSaldo Insuficiente!\n ")

        else:
            tentativas_saque -= 1
            quantidade_saque += 1
            valor_total_saques += saque
            saldo -= saque

        if tentativas_saque == 0:
            print("Voce chegou ao limite de saques diarios, Tente novamente amanhã ")


    elif opcao == 3:
        print("==========")
        print(f"Extrato:\nSaldo:{saldo:.2f}\nSaques:{quantidade_saque}\nValor Total Saques: {valor_total_saques:.2f}\n")
        print("==========")

    elif opcao == 4:

        print("Saindo do Banco")
        break
