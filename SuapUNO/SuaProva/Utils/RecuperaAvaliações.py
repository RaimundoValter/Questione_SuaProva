import os
import re

def recupera_avaliacoes(nome_pasta):
    """
    Processa arquivos de texto contendo avaliações de estudantes em uma pasta específica.

    Esta função realiza as seguintes etapas:
    1. Lista todos os arquivos com extensão .txt na pasta fornecida.
    2. Lê o conteúdo de cada arquivo e associa ao nome do estudante, extraído do nome do arquivo.
    3. Extrai as respostas dos estudantes no formato esperado, separando-as por questões indicadas pelos padrões como '1)', '2a)', '2b)', etc.

    Args:
        nome_pasta (str): Caminho para a pasta contendo os arquivos de texto das avaliações.

    Returns:
        list: Uma lista de listas, onde cada sublista contém:
              - O nome do estudante (str).
              - Uma lista de strings com as respostas extraídas de cada questão (list).

    Raises:
        FileNotFoundError: Se a pasta fornecida não for encontrada.
        ValueError: Se o formato esperado dos arquivos de texto não for atendido.
    """
    # Listar apenas arquivos com extensão .txt
    arquivos_txt = [f for f in os.listdir(nome_pasta) if f.endswith('.txt') and os.path.isfile(os.path.join(nome_pasta, f))]

    print("Arquivos .txt na pasta:")
    for arquivo in arquivos_txt:
        print(arquivo)
    print("\n\n")

    # Lista para armazenar o conteúdo de cada arquivo
    avaliacoes = []
    nomes_estudantes = []

    # Ler o conteúdo de cada arquivo e adicioná-lo à lista
    for arquivo in arquivos_txt:
        nomes_estudantes.append(arquivo.strip('.txt'))
        with open(os.path.join(nome_pasta, arquivo), 'r', encoding="ISO-8859-1") as f: #"ISO-8859-1"
            conteudo = f.read()
            avaliacoes.append(conteudo)

    # Separação das respostas
    respostas_estudantes = []
    for idx, avaliacao in enumerate(avaliacoes):
      # Regex para capturar questões no formato ##<<...>>## seguido pelo conteúdo da questão
      padrao = r"##<<(.+?)>>##(.*?)(?=##<<.+?>>##|$)"
      respostas = re.findall(padrao, avaliacao, re.DOTALL)
      respostas_formatadas = [f"{identificador}) {'<<QUESTÃO NÃO RESPONDIDA>>' if conteudo.strip()== '' else conteudo.strip()}" for identificador, conteudo in respostas]
      respostas_estudantes.append([nomes_estudantes[idx], respostas_formatadas])

    return respostas_estudantes