import re
import ast

def extrair_dicionario(texto):
  """
  Extrai o primeiro dicionário Python válido de uma string usando expressão regular.

  A função reformata o dicionário:
  - Substitui as chaves originais por índices numéricos sequenciais.
  - Se o dicionário possui uma terceira chave, tenta converter seu valor para float.

  Args:
      texto (str): Texto contendo um ou mais dicionários.

  Returns:
      dict: O dicionário formatado com chaves numéricas, ou None se nenhum dicionário válido for encontrado.
  """
  # Expressão regular para capturar estruturas parecidas com dicionários
  padrao = r'\{.*?\}'

  # Buscar todas as ocorrências no texto
  correspondencias = re.findall(padrao, texto, re.DOTALL)

  for texto in correspondencias:
    try:
      # Tenta converter a string para um dicionário Python
      texto_limpo = re.sub(r'\\n+', r' ', texto)
      texto_limpo = re.sub(r'\s+', ' ', texto_limpo)
      texto_limpo = re.sub(r'`', "'", texto_limpo)
      dicionario = ast.literal_eval(texto_limpo)

      if isinstance(dicionario, dict):

        dicionario_formatado = dict()

        # Verificando se é um dicionário de chaves numéricas: representando um dicionário de correção.
        if all(map(lambda elemento: str(elemento).isnumeric(), dicionario.keys())) and len(dicionario) == 3:

          # Para garantir que as chaves sejam números
          for idx, valor in enumerate(dicionario.values(), start=1):
            if idx == 3:
              dicionario_formatado[idx] = float(valor)
            else:
              dicionario_formatado[idx] = str(valor)

          return dicionario_formatado

        elif all(map(lambda elemento: str(elemento).isalpha(), dicionario.keys())) and len(dicionario) == 4: # Verifica se é um dicionário de avaliação de correção.

          # Para garantir que as chaves sejam as strings esperadas.
          valores_dicionario = list(dicionario.values())

          for idx, chave in enumerate(['clareza', 'completude', 'corretude', 'precisao']):
            dicionario_formatado[chave] = int(valores_dicionario[idx])

          return dicionario_formatado

      # Caso não seja um dicionário.
      continue

    except (SyntaxError, ValueError):

      print(f"\nErro ao converte dicionário, tentanto novamente...")
      # Ignora strings que não sejam dicionários válidos
      continue

  # Retorna None se nenhum dicionário válido for encontrado
  return None
