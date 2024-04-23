import os
from pathlib import Path


caminho_processados = (
    f"{Path(os.path.abspath(__file__)).parent.parent}/.processados"
)


def lista_processados() -> list:
    try:
        if not os.path.exists(caminho_processados):
            Path(caminho_processados).mkdir(parents=True, exist_ok=True)
            with open(f"{caminho_processados}/.processados", "w+") as arquivo:
                arquivo.write("")

        with open(f"{caminho_processados}/.processados", "r+") as arquivo:
            conteudo_arquivo = (
                [linha.strip("\n") for linha in arquivo.readlines()]
            )
        return conteudo_arquivo

    except Exception as _:
        return []


def adiciona_processados(arquivos: list) -> bool:
    try:
        if not os.path.exists(caminho_processados):
            Path(caminho_processados).mkdir(parents=True, exist_ok=True)

        with open(f"{caminho_processados}/.processados", "a+") as arq:
            for arquivo in arquivos:
                arq.write(f"{arquivo}\n")
        return True

    except Exception as _:
        return False


def remove_processados(arquivos: list, processados: list) -> list:
    try:
        arquivos_novos = []
        for arquivo in arquivos:
            if arquivo not in processados:
                arquivos_novos.append(arquivo)
        return arquivos_novos

    except Exception as _:
        return arquivos
