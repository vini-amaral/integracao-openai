import os
from openai import AzureOpenAI
import dotenv

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

dotenv.load_dotenv()

client = AzureOpenAI(
    # https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
    api_version="2023-09-01-preview",
    # https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_key=os.getenv("API_KEY"),
    azure_deployment=os.getenv("AZURE_DEPLOYMENT")
)



nome_do_produto = "Tapete de yoga"

prompt_sistema = """
Você é um analisador de sentimentos de avaliações de produtos.
Escreva um parágrafo com até 50 palavras resumindo as avaliações e depois atribua qual o sentimento geral para o produto.
Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

#### Formato de saída

Nome do produto: 
Resumo das avaliações:
Sentimento geral: [aqui deve ser POSITIVO, NEUTRO ou NEGATIVO]
Pontos fortes: [3 bullet points]
Pontos fracos: [3 bullet points]
"""

prompt_usuario = carrega(f"./dados/avaliacoes-{nome_do_produto}.txt")

resposta = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "system",
            "content": prompt_sistema
        },
        {
            "role": "user",
            "content": prompt_usuario
        }
    ]
)

salva(f"./dados/analise-{nome_do_produto}.txt", resposta.choices[0].message.content)