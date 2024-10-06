from acoes.menu import menu
from loads.load_config import load_config


def extrato():
    config_file = ".\\configs\\config.json"
    extrato_file = ".\\configs\\extratos.json"
    config = load_config(config_file)
    extrato = load_config(extrato_file)

    print("\nExtrato:")
    if extrato:
        for id, detalhes in extrato.items():
            print("ID da transação: ", id)
            print("Tipo da transação: ", detalhes["tipo"].capitalize())
            print("Valor da transação: R$", detalhes["valor"]),
            print("Data da Operação: ", detalhes["data"])
            print("----------------------------------------------------")
    else:
        print("Nenhuma transação realizada.")
    saldo = config["saldo"]
    print(f"\nSaldo atual: R${saldo:.2f}\n")

    menu()
