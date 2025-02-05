from scipy.stats import zscore

def escolhe_melhor(tentativas_correcao):
  """
  Seleciona a melhor tentativa de correção com base na qualidade e calcula uma nota final ponderada,
  removendo outliers para garantir resultados mais consistentes.

  Args:
      tentativas_correcao (list): Uma lista onde cada elemento é uma tentativa de correção no formato:
          [
              [correcao, ...],
              {'clareza': float, 'completude': float, 'corretude': float, 'precisão': float}
          ]

  Returns:
      tuple: Um par contendo:
          - nota_final (float): A nota final ponderada após a exclusão de outliers.
          - correcao_final (any): A melhor correção escolhida com base na mediana das qualidades.

  Raises:
      ValueError: Se a lista de tentativas estiver vazia ou se todas forem consideradas outliers.
  """
  if not tentativas_correcao:
    raise ValueError("A lista de tentativas de correção está vazia.")

  # Extrai notas e calcula qualidade total de cada correção
  notas = [float(correcao[0][3]) for correcao in tentativas_correcao]
  qualidades = [sum([float(valor) for valor in correcao[1].values()]) for correcao in tentativas_correcao]

  # Identificar e excluir outliers usando z-score
  z_scores = zscore(notas)
  outliers = [nota for nota, z in zip(notas, z_scores) if abs(z) > 2]

  for outlier in outliers:
    idx = notas.index(outlier)
    notas.pop(idx)
    qualidades.pop(idx)
    tentativas_correcao.pop(idx)

  if not notas:
    raise ValueError("Todas as tentativas foram consideradas outliers.")

  # Escolhe a melhor correção com base na mediana das qualidades
  lista_melhores = sorted(zip(qualidades, tentativas_correcao), key=lambda x: x[0])
  
  # Escolhe a correção de mais alta qualidade.
  correcao_final = lista_melhores[-1][1][0]

  # Seleciona a nota final da questão.
  nota_final = correcao_final[3] 

  return nota_final, correcao_final