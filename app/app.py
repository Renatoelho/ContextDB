
from utils.importa_atendimentos import atendimentos
from utils.database_vetorial import conexao_database_vetorial
from utils.database_vetorial import grava_embedding_database_vetorial
from utils.database_vetorial import pesquisa_contexto_database_vetorial


# Cria uma conexão com Database Vetorial (DuckDB).
conexao = conexao_database_vetorial()

# Verifica e lista atendimentos para inserir no Database.
dados_atendimentos = atendimentos()

# Só grava no Database, se existir novos atendimentos.
if dados_atendimentos:
    grava_embedding_database_vetorial(conexao, dados_atendimentos)

# Mensagem que deve ser respondida pelo modelo de LLM.
mensagem_atendimento = "meu pedido chegou incompleto"

# Pesquisa no Database N... últimas respostas baseado em similaridade.
base_contexto = (
    pesquisa_contexto_database_vetorial(conexao, mensagem_atendimento, 3)
)

# Prompt final que seguindo o método 'Few-Shot Prompting'.
prompt_final = f"""
Tarefa:Atue como um atendente e responda à seguinte solicitação de um cliente:
'{mensagem_atendimento}'

Contexto para a Resposta: Utilize os exemplos abaixo, provenientes de atendimentos anteriores em nossa base de dados, para guiar sua resposta:
{base_contexto}
"""

print(prompt_final)

# Exemplos:
# meu pedido chegou incompleto
# quero cancelar minha assinatura
