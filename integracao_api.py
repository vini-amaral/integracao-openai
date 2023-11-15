from openai import AzureOpenAI
import dotenv
import os

dotenv.load_dotenv()

client = AzureOpenAI(
    # https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
    api_version="2023-09-01-preview",
    # https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_key=os.getenv("API_KEY"),
    azure_deployment=os.getenv("AZURE_DEPLOYMENT")
)

resposta = client.chat.completions.create(
    model="gpt-3.5-turbo",  # e.g. gpt-3.5-turbo
    messages=[
        {
            "role": "system",
            "content": "Gere nomes de produtos fictícios sem descrição de acordo com a requisição do usuário",
        },
        {
            "role": "user",
            "content": "Gere 5 produtos",
        },
    ],
)

print(resposta.choices[0].message.content)
