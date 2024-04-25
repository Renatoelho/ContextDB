
import os
from pathlib import Path

import duckdb
import pandas as pd


pd.set_option("display.max_columns", None)

caminho_database = (
    f"{Path(os.path.abspath(__file__)).parent.parent}"
    "/database/atendimentos-db.duckdb"
)

with duckdb.connect(database=caminho_database, read_only=True) as conexao:
    query = "SELECT * FROM atendimentos LIMIT 3;"
    resultados = conexao.execute(query).df()

    print(resultados)
