
import os
from typing import Union
from pathlib import Path

from utils.controle_processados import lista_processados
from utils.controle_processados import adiciona_processados
from utils.controle_processados import remove_processados


def atendimentos() -> Union[list, bool]:
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
        if len(lista_atendimentos) == 0:
            raise ValueError("Não existe novos arquivos para importação.")
        return lista_atendimentos

    except Exception as _:
        return False
