from .ExtrairDicionário import extrair_dicionario
from .Llama import llama

def avaliar_resposta(questao, resposta, rubricas, pontuacao_maxima, dicionario_correcao):
  """
  Avalia a correção de uma pergunta respondida por um estudante, atribuindo pontuações
  com base em clareza, completude, corretude e precisão.

  Args:
      questao (str): A pergunta avaliada.
      resposta (str): A resposta fornecida pelo estudante.
      rubricas (str, float): Rubircas de avaliação detalhadas com pontuações específicas.
      pontuacao_maxima (float): Pontuação máxima atribuível para a resposta.
      dicionario_correcao (dict): Contém:
          - 1: Texto da correção.
          - 2: Feedback adicional.
          - 3: Pontuação atribuída pela correção.

  Returns:
      dict: Um dicionário contendo as pontuações para os critérios:
          - 'clareza': float (0.0 a 10.0)
          - 'completude': float (0.0 a 10.0)
          - 'corretude': float (0.0 a 10.0)
          - 'precisão': float (0.0 a 10.0)

  Raises:
      ValueError: Se nenhuma resposta válida for gerada após múltiplas tentativas.
  """
  prompt = f"""
  Esqueça o que foi dito antes.
  Considere os seguintes dados:
  **Pergunta**: {questao}
  **Resposta do estudante**: {resposta}
  **Rubricas** (com pontuações): {rubricas}
  **Pontuação máxima**: {pontuacao_maxima}
  **Texto da correção**: {dicionario_correcao[1]}
  **Feedback da correção**: {dicionario_correcao[2]}
  **Pontuação da correção**: {dicionario_correcao[3]}
  **Tarefa**:
  Avalie a correção da pergunta com base nas rubricas fornecidas.
  Atribua pontuações de 0 a 10 para clareza, completude, corretude, precisão.

  **Formato da resposta**:
  Retorne a resposta estritamente em formato de dicionário python com as seguintes chaves e valores, sem alucinar:
  {{'clareza': 'pontuação no formato float entre 0.0 e 10.0', 'completude': 'pontuação no formato float entre 0.0 e 10.0', 'corretude': 'pontuação no formato float entre 0.0 e 10.0', 'precisão': 'pontuação no formato float entre 0.0 e 10.0'}}

  **Dicionário Python**:
  """
  # Inicializa tentativa
  tentativa = 0
  max_tentativas = 4
  dicionario_resultado = None

  while dicionario_resultado is None and tentativa < max_tentativas:
    resposta_ia = llama(prompt)
    #pprint(resposta_ia)
    #print("\n")
    dicionario_resultado = extrair_dicionario(resposta_ia)
    tentativa += 1
    print(f"\nAvaliando a correção, tentativa {tentativa} de {max_tentativas}...")

  if dicionario_resultado is None:
    raise ValueError("Não foi possível gerar uma avaliação válida após várias tentativas.")

  return dicionario_resultado