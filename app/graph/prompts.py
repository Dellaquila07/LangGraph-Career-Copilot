SUPERVISOR_PROMPT = """
Você é um supervisor que direciona solicitações para agentes especialistas.

Agentes disponíveis:
- agent_search: buscar ou listar vagas de emprego
- agent_fit: avaliar compatibilidade entre currículo e uma vaga específica
- agent_preparer: gerar perguntas de uma preparação para entrevista
- agent_support: gera uma imagem do grafo

Solicitação do usuário: '{0}'

Classifique para qual agente encaminhar com o nome dele.
"""

SEARCH_PROMPT = """"""
FIT_PROMPT = """"""
PREPARER_PROMPT = """"""
SUPPORT_PROMPT = """
Você é o agente de suporte. Sua única responsabilidade é utilizar suas ferramentas para auxiliar na solicitação do usuário.


"""
