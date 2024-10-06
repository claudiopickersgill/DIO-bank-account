from acoes.menu import menu
from datetime import datetime
from loads.load_config import load_config
from loads.save_config import save_config


def depositar():
    # Import das configs de saldo e limites do JSON
    config_file = ".\\configs\\config.json"
    extrato_file = ".\\configs\\extratos.json"
    config = load_config(config_file)
    extrato = load_config(extrato_file)
    data_atual = datetime.now().strftime("%Y-%m-%d")

    valor = float(input("Digite o valor para depósito: R$"))
    if valor > 0:
        antigo_saldo = config["saldo"]
        novo_saldo = antigo_saldo + valor
        config["saldo"] = novo_saldo

        if len(extrato) == 0:
            id = 1
        else:
            ultimo_id = list(extrato.keys())
            id = int((ultimo_id[-1]))+1

        extrato[id] = {
            "tipo": "deposito",
            "valor": valor,
            "data": data_atual
        }
        save_config(config_file, config)
        save_config(extrato_file, extrato)
        print("Valor depositado com sucesso")
        print("Voltando ao Menu inicial")
        print("\n")

    else:
        print("O Valor precisa ser maior que Zero!")
        print("\n")

    menu()
