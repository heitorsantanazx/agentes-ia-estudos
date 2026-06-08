# Demonstra o parâmetro de ferramentas do ADK com uma ferramenta de função personalizada simples.

from google.adk.agents import LlmAgent

# Criando uma função personalizada para ser usada como ferramenta.
def get_capital_city(country: str) -> str:
    """Recupera a capital de um país específico.
    
    Args:
        country (str): o nome do país.
    Retorna:
        str: o nome da capital do país ou uma mensagem de erro.
    """
    # Dicionário de exemplo de países e suas capitais.
    capitals = {
        "França": "Paris",
        "Espanha": "Madri",
        "Itália": "Roma",
        "Alemanha": "Berlim",
        "Brasil": "Brasília",
        "Japão": "Tóquio",
        "Irlanda": "Dublin",
        "Escócia": "Edimburgo",
        "Suécia": "Estocolmo",
    }

    #Consulta a capital no dicionário.
    return capitals.get(
        country.title(),
        f"Perdão, não tenho informações sobre a capital de {country}. Deseja saber sobre outro país?"
    )

# Criação do agente com a função personalizada como ferramenta.
root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='geography_assistant',
    description='Ajuda os usuários a aprender sobre geografia mundial.',
    instruction="""Você é um assistente de geografia que ajuda usuários sobre as capitais dos países que forem perguntados.

    Quando um usuário perguntar sobre a capital de um país:
       1. Use a ferramenta get_capital_city para obter a capital do país.
       2. Apresente as informações de forma amigável, clara e concisa.
       3. Você pode adicionar informações adicionais interessantes sobre o país ou a capital se conhecer.

    Se a ferramenta retornar uma mensagem de erro, diga educamente ao usuário que você não tem informações sobre a capital do país solicitado.
    """,
    tools=[get_capital_city] # Disponibiliza a função personalizada como ferramenta para o agente usar.
)
