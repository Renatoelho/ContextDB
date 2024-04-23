
import os
from pathlib import Path

import duckdb
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import DuckDB

from utils.importa_atendimentos import atendimentos


load_dotenv()

caminho_database = f"{Path(os.path.abspath(__file__)).parent}/database"

if not os.path.exists(caminho_database):
    Path(caminho_database).mkdir(parents=True, exist_ok=True)

conexao = duckdb.connect(
    database=f"{caminho_database}/atendimentos.duckdb",
    config={
        "enable_external_access": "false",
        "autoinstall_known_extensions": "false",
        "autoload_known_extensions": "false"
    }
)

embedding_atendimento = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    embedding_ctx_length=8191
)

database_atendimento = DuckDB(
    connection=conexao,
    embedding=embedding_atendimento
)

dados_atendimentos = atendimentos()

if dados_atendimentos:
    database_atendimento.add_texts(dados_atendimentos)

def contexto(mensagem: str, quantidade: int) -> str:
    base_contexto_tmp = []
    base_contexto = database_atendimento.similarity_search(
        mensagem,
        k=quantidade
    )

    for id, contexto in enumerate(base_contexto):
        contexto_tmp = (
            f"-> Exemplo {id + 1}: {contexto.page_content.split(';')[1]}"
        )
        base_contexto_tmp.append(contexto_tmp)

    return "\n".join(base_contexto_tmp)

atendimento = "quero cancelar minha assinatura"

prompt_final = f"""
Tarefa:Atue como um atendente e responda à seguinte solicitação de um cliente:
'{atendimento}'

Contexto para a Resposta: Utilize os exemplos abaixo, provenientes de atendimentos anteriores em nossa base de dados, para guiar sua resposta:
{contexto(atendimento, 3)}
"""

print(prompt_final)

# meu pedido chegou incompleto
# quero cancelar minha assinatura
