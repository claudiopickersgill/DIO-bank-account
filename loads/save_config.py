import json


def save_config(caminho_arquivo, dados):
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
