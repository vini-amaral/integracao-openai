import os
from openai import AzureOpenAI
import dotenv


def requisicao(prompt_sistema, prompt_usuario):

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
                "content": prompt_sistema,
            },
            {
                "role": "user",
                "content": prompt_usuario,
            },
        ],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    return resposta.choices[0].message.content
