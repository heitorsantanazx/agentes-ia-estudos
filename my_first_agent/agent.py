from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash', # Modelo: o mecanismo de raciocínio
    name='hist_tutor_agent', # Identificador do agente
    description='Ajudar estudantes universitários com suas dúvidas.', # Descrição com clareza sobre o agente
    instruction='Você é um professor experiente e paciente. Ajude os estudantes a compreenderem os conceitos.' # Instrução clara para o agente
)