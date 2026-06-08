# Estudos envolvendo o pydantic

from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field

class CapitalOutput(BaseModel):
    capital: str = Field(description="A capital do país")

root_agent = Agent(
    model='gemini-2.5-flash',
    name='capital_finder',
    description='Um assistente que ajuda a encontrar capitais.',
    instruction="""
        Você é um agente de informações sobre capitais.
        Quando um país é informado, responda APENAS com um objeto JSON que contém a capital.
        Format: {"capital": "capital_name"} """,
    output_schema=CapitalOutput, # Aplicar saída JSON
    output_key="found_capital" # Armazenar em session.state["found_capital"]
)