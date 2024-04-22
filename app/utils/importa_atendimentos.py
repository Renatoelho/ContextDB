
import os
from pathlib import Path

def atendimentos() -> list:

    assert os.path.exists(f"{Path(os.path.abspath(__file__)).parent.parent}/contexto"), "Arquivos de contexto não estão disponíveis."
    path_local =  f"{Path(os.path.abspath(__file__)).parent.parent}/contexto"
    print(path_local)
    arquivos_atendimentos = os.listdir(path_local)
    lista_atendimentos = []
    for arquivo in arquivos_atendimentos:
        with open(f"{path_local}/{arquivo}", "r+") as arq:
            conteudo_arquivo = [linha.strip("\n") for linha in arq.readlines()]
        for index, linha in enumerate(conteudo_arquivo):
            if index > 0:
                lista_atendimentos.append(linha)
    assert len(lista_atendimentos) != 0, "Não foram encontrados atendimentos."
    return lista_atendimentos
