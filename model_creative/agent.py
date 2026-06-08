# Agente 2: otimizado para criação de ideias inovadoras
# Usa temperatura alta para criatividade, modelo Pro para ideias melhores

from google.adk.agents.llm_agent import Agent
from google.genai import types

root_agent = Agent(
    model="gemini-2.5-pro", # Pro para criatividade superior
    name="creative_brainstormer",
    description="Gera ideias criativas e examina as possibilidades",
    instruction="""Você é um parceiro de criação de ideias inovadoras.
        Gerar ideias variadas e cheias de imaginação. Fique à vontade para:
        - Soltar a imaginação
        - Combinar conceitos inesperados
        - Analisar abordagens pouco convencionais
        Seja criativo, diversificado e instigante.""",

    generate_content_config=types.GenerateContentConfig(
    temperature=0.9, # Alta para criatividade
    max_output_tokens=2000, # Permitir ideias detalhadas
    top_p=0.95,
    top_k=40,
        safety_settings=[
            types.SafetySetting(
            category="HARM_CATEGORY_DANGEROUS_CONTENT",
            threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            )
        ]
    )
)