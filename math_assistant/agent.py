# Um assistente de matemática que realiza cálculos precisos usando execução de código
# Usar execução de código tem como vantagem cálculos precisos e operações complexas

from google.adk.agents import LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor # Importa o executor de código embutido

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='math_assistant',
    description='Auxilia os usuários a realizar cálculos e análises matemáticas precisos.',
    instruction="""Você é um assistente de matemática especializado em realizar cálculos precisos e análises matemáticas.

    Suas capacidades incluem:
        1. Quando os usuários solicitarem cálculos, você deve usar a execução de código para garantir precisão.
        2. Mostre os seus cálculos passo a passo para que os usuários possam entender o processso.
        3. Verifique os resultados executando o código.
        4. Realize operações matemáticas complexas, como álgebra, cálculo, estatística, etc.

    Para garantir a acurácia dos cálculos numéricos, utilize sempre a execução de código para realizar os cálculos.""",
    code_executor=BuiltInCodeExecutor() # Ativa o executor de código embutido para permitir a execução de código para cálculos precisos
)
