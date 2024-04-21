

from dotenv import load_dotenv

import duckdb

#from langchain.embeddings import OpenAIEmbeddings
#from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
#from langchain.vectorstores import DuckDB
from langchain_community.vectorstores import DuckDB

#from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

loader = TextLoader("./contexto/atendimento_clientes.txt")
documents = loader.load()

documents = CharacterTextSplitter().split_documents(documents)
embeddings = OpenAIEmbeddings()

#db = duckdb.connect(database = ":memory:", read_only = False)

con = duckdb.connect(database = "atendimento_clientes.duckdb", read_only = False)

#docsearch = DuckDB.from_documents(documents, embeddings, enable_external_access=True)

docsearch = DuckDB(con, embeddings, table_name="atendimento_clientes")


query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query, k=3)

print(docs)
