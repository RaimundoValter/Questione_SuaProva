from SuaProva.Utils.RecuperaAvaliações import recupera_avaliacoes
from pprint import pprint

# Teste unitário: recupera_avaliacoes()
avaliacoes = recupera_avaliacoes('/content/provas_ia/N1-AP2')
pprint(avaliacoes)

# for avaliacao in avaliacoes:
#   print(len(avaliacao[1]))