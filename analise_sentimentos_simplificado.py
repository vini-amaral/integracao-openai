import processa_openai
import util

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

nome_do_produto = "Tapete de yoga"

prompt_usuario = util.carrega(f"./dados/avaliacoes-{nome_do_produto}.txt")

resposta = processa_openai.requisicao(prompt_sistema, prompt_usuario)

util.salva(f"./dados/analise-{nome_do_produto}.txt", resposta)
print(resposta)
