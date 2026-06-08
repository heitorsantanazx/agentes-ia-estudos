"""
Demonstração da configuração do modelo que compara a otimização factual com a criativa.
Demonstra o generate_content_config do ADK com configurações diferentes.
"""

from google.adk.agents.llm_agent import Agent
from google.genai import types

# Agente otimizado para respostas factuais
# Usa temperatura baixa para respostas mais precisas e com segurança rigorosa.

root_agent = Agent(
    model='gemini-2.5-flash', # Flash é o sufuciente para respostas factuais, e é mais econômico.
    name='data_extractor',
    description='Extrai informações factuais com alta consistência e precisão.',
    instruction="""Você é um agente extrator de dados preciso.
        
        Extrair os fatos exatamente como estão apresentados:
         - Não adicione informações que não constam na entrada
         - Não faça suposições ou inferências
         - Não use linguagem figurada ou criativa
        Seja preciso, conciso e determinista.""",
    
    generate_content_config=types.GenerateContentConfig(
        temperature=0.1, #Muito baixa pra consistência
        max_output_tokens=500,
        top_p=0.8,
        top_k=10,
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
            )
        ]
    )
)
