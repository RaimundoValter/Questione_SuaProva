from .RecuperaAvaliações import recupera_avaliacoes
from .Llama import llama
from .MontarPDF import montar_pdf_correcao
from .AvaliarResposta import avaliar_resposta
from .ExtrairDicionário import extrair_dicionario
from .EscolheMelhor import escolhe_melhor

def corrigir(nome_pasta, gabarito_avaliacao, REPETIR_CORRECAO = 3, alunos = []):
  questoes = gabarito_avaliacao[0]
  rubricas = gabarito_avaliacao[1]
  pontuacao_maxima = gabarito_avaliacao[2]
  avaliacoes = recupera_avaliacoes(nome_pasta)


  avaliacoes_para_correcao = []

  if alunos != []:
    for avaliacao in avaliacoes:
      if avaliacao[0].strip('.txt') in alunos:
        avaliacoes_para_correcao.append(avaliacao)

  else:
    avaliacoes_para_correcao = avaliacoes

  # Para cada avaliação de um estudante
  for avaliacao in avaliacoes_para_correcao:

    # print("")
    # pprint(avaliacao)
    # print("")

    nome_arquivo = avaliacao[0].strip('.txt')
    #nome_estudante = avaliacao[0].split('- ')[0].strip('.txt')
    nome_estudante = nome_arquivo
    respostas = avaliacao[1]

    print(f"Avaliando o aluno {nome_estudante}...")

    avaliacao_corrigida = []

    # Para cada Questão em uma avaliação específica
    for numero_questao, questao in enumerate(questoes):

      if '<<QUESTÃO NÃO RESPONDIDA>>' in respostas[numero_questao]:
        print(f"Questão {numero_questao +1 } está vazia...")
        avaliacao_corrigida.append([0.0 , {1:"",2:"",3:0.0}])
        continue

      prompt = f"""
Esqueça o que foi dito antes.
Considere os seguintes dados:
**Pergunta**: {questao}
**Resposta do estudante**: {respostas[numero_questao]}
**Rubricas**: {rubricas[numero_questao]}
**Pontuação máxima**: {pontuacao_maxima[numero_questao]}
Assuma que o estudante possui um conhecimento **básico** sobre o assunto avaliado.
**Tarefa**:
- Corrija a resposta do estudante considerando as rubricas fornecidas.
- Seja flexível e atribua nota máxima na rubrica caso o estudante atinja parcialmente a descrição da rubrica.

**Formato da resposta**:
Retorne a resposta estritamente em formato de dicionário Python (chaves em formato de números inteiros e valores associados às chaves em formato string) com as seguintes chaves e valores, sem alucinar:
{{1: 'texto completo da avaliação da resposta do estudante em relação às rubircas fornecidas',
  2: 'texto com o feedback detalhado sobre os pontos fortes e as melhorias necessárias na resposta para atingir nota máxima na questão completa, caso não tenha atingido a nota máxima.',
  3: 'pontuação no formato float, garantindo que o total não ultrapasse a pontuação máxima e reflita a nota do item avaliado em acordo com as rubricas da questão avaliada.'}}

**Dicionário Python**:
"""

      qtd_correcoes = 0
      tentativas_correcao = []

      # Faz 5 tentativas para verificar qual correção foi a melhor.
      while qtd_correcoes < REPETIR_CORRECAO:
        print(f"\nCorrigindo a questão {numero_questao + 1}, vez {qtd_correcoes+1} de {REPETIR_CORRECAO}...")
        # Correção pela Llama
        resposta_ia = llama(prompt)

        # Extração do dicionário contendo a correção.
        dicionario_correcao = extrair_dicionario(resposta_ia)

        # Caso a resposta seja válida
        if dicionario_correcao is not None:
          # Avalia a qualidade da resposta solicitando ao Llama que avalie a própria
          qualidade_correcao = avaliar_resposta(questao, respostas[numero_questao], rubricas[numero_questao], pontuacao_maxima[numero_questao], dicionario_correcao)
          # Grava a correção e a avaliação da qualidade dessa correção
          tentativas_correcao.append([dicionario_correcao, qualidade_correcao])
          qtd_correcoes += 1

      #Ao terminar as 5 correções e suas avaliações, escolhe a melhor entre elas e grava a média das notas e a correção com melhor avaliação.
      avaliacao_corrigida.append(escolhe_melhor(tentativas_correcao))

      print(f"\nQuestão {numero_questao + 1}: ok!")
      
      if (numero_questao + 1) < len(questoes):
        print("\nIndo para próxima questão >>>")
      else:
        print(f"Finalizado a avaliação de {nome_estudante}!")

    #pprint(avaliacao_corrigida)

    # Ao finalizar uma correção completa, grava o resultado em pdf para aquele estudante.
    montar_pdf_correcao(nome_estudante, questoes, rubricas, respostas, avaliacao_corrigida, nome_pasta+"/correções")

    # pprint(avaliacao_corrigida)