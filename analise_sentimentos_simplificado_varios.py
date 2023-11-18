import processa_openai
import util

def analise_sentimento(nome_do_produto):
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

    prompt_usuario = util.carrega(f"./dados/avaliacoes-{nome_do_produto}.txt")
    print(f"Iniciando a análise do produto: {nome_do_produto}")

    resposta = processa_openai.requisicao(prompt_sistema, prompt_usuario)

    util.salva(f"./dados/analise-{nome_do_produto}.txt", resposta)
    print(f"Análise concluída com sucesso.")

lista_de_produtos = ["Tapete de yoga", "Tabuleiro de xadrez de madeira"]

for nome_do_produto in lista_de_produtos:
    analise_sentimento(nome_do_produto)
