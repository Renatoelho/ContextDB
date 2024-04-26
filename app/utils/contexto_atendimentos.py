
import os
from typing import Union
from pathlib import Path

from utils.controle_processados import lista_processados
from utils.controle_processados import adiciona_processados
from utils.controle_processados import remove_processados


def contexto_atendimentos() -> Union[list, bool]:
    try:
        caminho_local = (
            f"{Path(os.path.abspath(__file__)).parent.parent}/contexto"
        )
        assert os.path.exists(caminho_local), "Arquivos contexto indisponíveis"

        lista_atendimentos = []

        arquivos_atendimentos = remove_processados(
            os.listdir(caminho_local),
            lista_processados()
        )

        for arquivo in arquivos_atendimentos:
            with open(f"{caminho_local}/{arquivo}", "r+") as arq:
                conteudo_arquivo = (
                    [linha.strip("\n") for linha in arq.readlines()]
                )
            for index, linha in enumerate(conteudo_arquivo):
                if index > 0:
                    lista_atendimentos.append(linha)

        adiciona_processados(arquivos_atendimentos)

        return lista_atendimentos

    except Exception as erro:
        raise ValueError(f"Erro ao tratar os atendimentos: {erro}")
