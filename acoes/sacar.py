from acoes.menu import menu
from datetime import datetime
from loads.load_config import load_config
from loads.save_config import save_config


def sacar():
    # Import das configs de saldo e limites do JSON
    config_file = ".\\configs\\config.json"
    extrato_file = ".\\configs\\extratos.json"
    config = load_config(config_file)
    extrato = load_config(extrato_file)
    data_atual = datetime.now().strftime("%Y-%m-%d")

    valor = float(input("Digite o valor para sacar: R$"))
    if valor > config["limite_por_operacao"]:
        print("Valor máximo excedido. Tente um valor menor")
        print("\n")
        menu()

    else:
        operacoes = 0
        for id, detalhes in extrato.items():
            if (detalhes["data"] == data_atual) and (detalhes["tipo"] == "saque"):
                operacoes += 1

        if operacoes >= config["operacao_por_dia"]:
            print("Limite de saques dirários atingido")
            print("Espere até amanhã para fazer outro saque!")
            print("\n")

        elif 0 < valor <= config["saldo"]:
            novo_saldo = config["saldo"] - valor
            config["saldo"] = novo_saldo

            if len(extrato) == 0:
                id = 1
            else:
                ultimo_id = list(extrato.keys())
                id = int((ultimo_id[-1]))+1

            extrato[id] = {
                "tipo": "saque",
                "valor": valor,
                "data": data_atual
            }
            save_config(config_file, config)
            save_config(extrato_file, extrato)
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            print("\n")

        elif valor > config["saldo"]:
            print("Saldo insuficiente!")
            print("\n")
        else:
            print("Valor de saque inválido!")
            print("\n")

        menu()
