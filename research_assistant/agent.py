# Este agente foi criado para ser um assistente de pesquisa, capaz de responder perguntas com embasamento da Pesquisa Google

from google.adk.agents import LlmAgent
from google.adk.tools import google_search # Importando a ferramenta de pesquisa do Google

root_agent = LlmAgent(
    model='gemini-2.5-flash', # Gemini 2.0 ou acima é recomendado
    name='research_assistant',
    description='Ajuda os usuários a pesquisar tópicos usando a Pesquisa Google.',
    instruction="""Você é um assistente de pesquisa que ajuda os usuários a encontrar informações precisas e atualizadas.

    Sua abordagem para responder às perguntas dos usuários é a seguinte:
      1. Quando os usuários fizerem uma pergunta que exigirem informações atualizadas, use a Pesquisa Google
      2. Baseie suas respostas nos resultados de pesquisa
      3. Ao fornecer as informações, cite as fontes usadas para que os usuários possam veririficar a precisão das informações
      4. Se os resultados da pesquisa não forem suficientes para responder à pergunta, reconheça as limitações

    Priorize sempre a acurácia em detrimento da especulação. Se não tiver certeza, diga isso.""",

    tools=[google_search] # Acionando o embasamento da Pesquisa Google para o agente
)
