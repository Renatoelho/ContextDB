
import duckdb
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import DuckDB

from utils.importa_atendimentos import atendimentos

load_dotenv()

conn = duckdb.connect(database=':memory:',
    config={
            "enable_external_access": "false",
            "autoinstall_known_extensions": "false",
            "autoload_known_extensions": "false"
        }
)
embedding_function = OpenAIEmbeddings()
vector_store = DuckDB(connection=conn, embedding=embedding_function)
vector_store.add_texts(atendimentos())
result = vector_store.similarity_search('meu pedido chegou incompleto', k=3)
print(result)