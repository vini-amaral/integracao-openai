import os
from openai import AzureOpenAI
import dotenv
import tiktoken

codificador = tiktoken.encoding_for_model("gpt-3.5-turbo")


def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")


dotenv.load_dotenv()
client = AzureOpenAI(
    # https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
    api_version="2023-09-01-preview",
    # https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_key=os.getenv("API_KEY"),
    azure_deployment=os.getenv("AZURE_DEPLOYMENT")
)

prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("./dados/lista_de_compras_100_clientes.csv")

lista_de_tokens = codificador.encode(prompt_sistema + prompt_usuario)
numero_de_tokens = len(lista_de_tokens)
print(f"Número de tokens na entrada: {numero_de_tokens}")
modelo = "gpt-3.5-turbo"
tamanho_esperado_saida = 2048
print(f"Número de tokens esperados na saída: {tamanho_esperado_saida}")
print(f"Número de tokens total: {numero_de_tokens + tamanho_esperado_saida}")
if numero_de_tokens >= 8192 - tamanho_esperado_saida:
    #modelo = "gpt-3.5-turbo-16k"
    print("Necessário configurar um azure_deployment que suporte gpt-3.5-turbo-16k")
else:
    print(f"Modelo escolhido: {modelo}")
    resposta = client.chat.completions.create(
        model=modelo,
        messages=[
            {
                "role": "system",
                "content": prompt_sistema
            },
            {
                "role": "user",
                "content": prompt_usuario
            }
        ],
        temperature=0.7,
        max_tokens=tamanho_esperado_saida,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    print(resposta.choices[0].message.content)
