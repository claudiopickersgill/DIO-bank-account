def menu():

    from acoes.depositar import depositar
    from acoes.sacar import sacar
    from acoes.extrato import extrato

    print("----- Sistema Bancário -----")
    print("Seja bem vindo ao nosso Novo Banco")
    print("O que deseja fazer?")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Visualizar Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        depositar()
    elif opcao == '2':
        sacar()
    elif opcao == '3':
        extrato()
    elif opcao == '4':
        print("Encerrando o sistema bancário.")
    else:
        print("Opção inválida! Tente novamente.")
