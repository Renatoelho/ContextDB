
from utils.database_vetorial import conexao_database
from utils.database_vetorial import grava_embedding
from utils.database_vetorial import pesquisa_contexto
from utils.contexto_atendimentos import contexto_atendimentos


# Cria uma conexão com Database Vetorial (DuckDB).
conexao = conexao_database()

# Verifica e lista atendimentos para inserir no Database.
atendimentos = contexto_atendimentos()

# Só grava no Database, se existir novos atendimentos.
if atendimentos:
    grava_embedding(conexao, atendimentos)

# Mensagem que deve ser respondida pelo modelo de LLM.
mensagem_atendimento = "meu pedido chegou incompleto"

# Pesquisa no Database N... últimas respostas baseado em similaridade.
contexto = (
    pesquisa_contexto(conexao, mensagem_atendimento, 3)
)

# Prompt final que seguindo o método 'Few-Shot Prompting'.
prompt_final = f"""
Tarefa:Atue como um atendente e responda à seguinte solicitação de um cliente:
'{mensagem_atendimento}'

Contexto para a Resposta: Utilize os exemplos abaixo, provenientes de atendimentos anteriores em nossa base de dados, para guiar sua resposta:
{contexto}
"""

print(prompt_final)

# Exemplos:
# meu pedido chegou incompleto
# quero cancelar minha assinatura
