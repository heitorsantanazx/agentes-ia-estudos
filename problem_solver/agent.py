# Desenvolvendo com o uso do BuiltInPlanner
# Usado para modelos do Gemini (2.5 Flash, 2.5 Pro, 2.0 Flash)
# Processo de raciocínio mais natural.

from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from google.genai import types

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='strategic_problem_solver',
    description='Resolver problemas complexos usando raciocínio estratégico e com planejamento integrado.',
    instruction="""Você é um solucionador de problemas estratégicos.

        Sua abordagem para problemas complexos deverá ser:

        1. **Entender**: divida o problema em componentes
        2. **Analisar**: considere várias perspectivas, os prós e contras de cada abordagem
        3. **Planejar**: desenvolva uma estratégia de solução detalhada, incluindo etapas e recursos necessários
        4. **Executar**: apresente soluções claras e práticas

        Para problemas complexos:

        - Avalie bem as implicações e os casos extremos
        - Considere as consequências de curto e longo prazo
        - Identifique possíveis riscos e estratégias de mitigação
        - Mostre o raciocínio por trás de cada decisão e escolha 
    Seja detalhista, analítico e sistemático em sua abordagem.""",
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,  # True para mostrar o processo de raciocínio e False para ocultar
            thinking_budget=2048    # Orçamento grande para permitir um raciocínio mais profundo e detalhado
        )
    )
)