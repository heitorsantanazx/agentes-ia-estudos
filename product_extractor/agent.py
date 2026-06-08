# Agente de extração de produtos com saída JSON estruturada.
# Demonstra o output_schema do ADK com o Pydantic BaseModel.
# Uso do pydantic para definir o formato de saída esperado, garantindo que o agente retorne um JSON válido e estruturado.

from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field

class ProductInfo(BaseModel):
    product_name: str = Field(description="Nome do produto")
    price: float = Field(description="Preço do produto em USD")
    storage: str = Field(description="Capacidade de armazenamento do produto (ex. '128GB')")
    color: str = Field(default="Não especificado", description="Cor do produto, se for mencionada")

root_agent = Agent(
    model='gemini-2.5-flash',
    name='product_extractor_agent',
    description='Extrai informações do produto das mensagens dos usuários e retorna um JSON estruturado',
    instruction="""Você é um extrator de informações do produto.
        Sua tarefa:
        - Ler a mensagem do usuário sobre um produto
        - Extrair: product_name, price, storage e color (se mencionada)
        - Responder APENAS com JSON válido que corresponda a este formato:
            {
            "product_name": "nome do produto aqui",
            "price": 999.99,
            "storage": "256GB",
            "color": "Space Black"
            }
        Regras:
        - o preço precisa ser um número (sem cifrões)
        - o armazenamento precisa incluir a unidade (GB, TB)
        - se a cor não for mencionada, use "Não especificado"
        - APENAS a saída JSON, sem texto explicativo""",
    output_schema=ProductInfo,
    output_key="extracted_product" # Armazenar o resultado no estado da sessão"
)