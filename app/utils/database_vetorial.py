
import os
from typing import Union, List
from pathlib import Path

import duckdb
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import DuckDB


load_dotenv()


def conexao_database_vetorial() -> Union[object, bool]:
    try:
        caminho_database = (
            f"{Path(os.path.abspath(__file__)).parent.parent}/database"
        )

        if not os.path.exists(caminho_database):
            Path(caminho_database).mkdir(parents=True, exist_ok=True)

        return duckdb.connect(
            database=f"{caminho_database}/vetorial-atendimentos-db.duckdb",
            config={
                "enable_external_access": "false",
                "autoinstall_known_extensions": "false",
                "autoload_known_extensions": "false"
            }
        )

    except Exception as erro:
        raise ValueError(f"Erro ao conectar no database vetorial: {erro}")


def grava_embedding_database_vetorial(
    conexao: object,
    atendimentos: List[str]
) -> bool:
    try:

        embedding = OpenAIEmbeddings(
            model="text-embedding-ada-002",
            embedding_ctx_length=8191
        )

        database_vetorial = DuckDB(
            connection=conexao,
            embedding=embedding,
            table_name="vetorial_atendimentos"
        )

        database_vetorial.add_texts(atendimentos)

        return True

    except Exception as erro:
        raise ValueError(f"Erro ao adicionar embeddings ao database: {erro}")


def pesquisa_contexto_database_vetorial(
    conexao: object,
    mensagem: str,
    quantidade: int
) -> Union[str, bool]:
    try:

        base_contexto_tmp = []

        embedding = OpenAIEmbeddings(
            model="text-embedding-ada-002",
            embedding_ctx_length=8191
        )

        database_vetorial = DuckDB(
            connection=conexao,
            embedding=embedding,
            table_name="vetorial_atendimentos"
        )

        contexto = database_vetorial.similarity_search(
            mensagem,
            k=quantidade
        )

        for id, contexto in enumerate(contexto):
            contexto_tmp = (
                f"-> Exemplo {id + 1}: "
                f"{contexto.page_content.split(';')[1]}"
            )
            base_contexto_tmp.append(contexto_tmp)

        return "\n".join(base_contexto_tmp)

    except Exception as erro:
        raise ValueError(f"Erro ao pesquisa no database: {erro}")
