import pytz
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap
from pylatex import Document, Section, Command, Figure, NoEscape, Package, MiniPage, Enumerate, Itemize


def montar_pdf_correcao(nome_estudante_, perguntas, rubricas, respostas_estudante, avaliacao_corrigida, pontuacoes_maximas, nome_pasta="."):
    """
    Gera um arquivo PDF contendo a correção detalhada de uma avaliação.

    Args:
        nome_estudante_ (str): Nome do estudante.
        perguntas (list): Lista de perguntas realizadas na avaliação.
        rubricas (list): Lista de rubricas para as respostas esperadas.
        respostas_estudante (list): Lista de respostas fornecidas pelo estudante.
        avaliacao_corrigida (list): Lista de tuplas contendo:
            - Nota da questão (float).
            - Detalhes da correção (dict) com as chaves:
                - 'consideracoes': Considerações sobre a resposta do estudante.
                - 'feedback': Feedback fornecido.
                - 'pontuacao': Pontuação atribuída.
        nome_pasta (str, optional): Diretório onde o arquivo PDF será salvo.
                                    Padrão é o diretório atual (".").

    Returns:
        str: Caminho do arquivo PDF gerado.

    Raises:
        ValueError: Se o tamanho das listas de perguntas, rubricas ou respostas não coincidir.

    """
    # Validação das listas
    if not (len(perguntas) == len(rubricas) == len(respostas_estudante) == len(avaliacao_corrigida) == len(pontuacoes_maximas)):
        raise ValueError("As listas de perguntas, rubricas, respostas e avaliações devem ter o mesmo tamanho.")

    # Cálculo da pontuação total
    pontuacao_total = sum(nota for nota, _ in avaliacao_corrigida)

    print(f"Atribuído nota {pontuacao_total:.2f} para {nome_estudante_}...")
    
    fuso_sao_paulo = pytz.timezone("America/Sao_Paulo")
    hora_atual_sp = datetime.datetime.now(fuso_sao_paulo)

    data_hora = hora_atual_sp.strftime("%Y-%m-%d %Hh%Mm")
    # Nome do arquivo PDF
    nome_arquivo_pdf = f"{nome_pasta}/Correção do {nome_estudante_} - {data_hora} - Nota {pontuacao_total:.2f}.pdf"

    # Configuração do PDF
    c = canvas.Canvas(nome_arquivo_pdf, pagesize=letter)

    c.setFont("Helvetica-Bold", 10)
    largura, altura = letter
    margem = 50  # Margem do documento
    largura_texto = largura - 2 * margem
    linha_atual = altura - margem  # Posição inicial no topo da página
    espaco_entre_linhas = 12  # Espaço entre as linhas

    # Função para adicionar texto ao PDF com controle de quebras de linha
    def adicionar_texto(texto, c, linha_atual):
        linhas = wrap(texto, width=95)  # Ajuste o valor para controlar a largura do texto
        for linha in linhas:
            if linha_atual <= margem:
                c.showPage()  # Cria uma nova página se necessário
                linha_atual = altura - margem
            c.drawString(margem, linha_atual, linha)
            linha_atual -= espaco_entre_linhas
        return linha_atual

    # Texto do PDF
    correcao = f"Nome: {nome_estudante_}\n"
    correcao += f"Pontuação Total da Avaliação: {pontuacao_total:.2f} pontos\n"
    correcao += "=" * 25 + "\n"

    for id, pergunta in enumerate(perguntas):
        correcao += f"Correção da Questão {id+1}:\n"
        correcao += f"Pergunta: {pergunta}\n\n"
        correcao += "=" * 10 + "Rubrica(s)\n"
        
        for rubrica in rubricas[id]:
          correcao += f"{rubrica}\n"

        correcao += "=" * 10 + f"Resposta do estudante da questão {id+1}:\n"
        correcao += f"{respostas_estudante[id]}\n\n"
        correcao += "=" * 25 + "\n"
        correcao += f"Correção proposta pela IA:\n"
        correcao += "=" * 25 + "\n"
        correcao += "=" * 10 + f"Considerações:\n"
        correcao += f"{avaliacao_corrigida[id][1][1]}\n\n"
        correcao += "=" * 10 + "Feedback:\n"
        correcao += f"{avaliacao_corrigida[id][1][2]}\n\n"
        correcao += "=" * 10 + "Pontuação:\n"
        correcao += f"{avaliacao_corrigida[id][1][3]}\n\n"
        correcao += "=" * 25 + "\n"

    # Adicionar texto ao PDF
    for linha in correcao.split("\n"):
        linha_atual = adicionar_texto(linha, c, linha_atual)

    # Salvar o PDF
    c.save()
    print(f"Correção gravada em: {nome_arquivo_pdf}")
    return nome_arquivo_pdf

def montar_pdf_latex(nome_aluno, perguntas, rubricas, respostas_estudante, avaliacao_corrigida, pontuacoes_maximas, nome_pasta):
  ifce_logo_path = "/content/ifce_logo.png"
  nome_disciplina = "Inteligência Artificial"
  nome_avaliacao = "AP1-N1"
  nome_conteudo = "Métodos Conxionistas: RNN e CNN"

  # Validação das listas
  if not (len(perguntas) == len(rubricas) == len(respostas_estudante) == len(avaliacao_corrigida) == len(pontuacoes_maximas)):
    raise ValueError("As listas de perguntas, rubricas, respostas e avaliações devem ter o mesmo tamanho.")

  # Cálculo da pontuação total
  pontuacao_total = sum(nota for nota, _ in avaliacao_corrigida)

  print(f"Atribuído nota {pontuacao_total:.2f} para {nome_aluno}...")
  
  fuso_sao_paulo = pytz.timezone("America/Sao_Paulo")
  hora_atual_sp = datetime.datetime.now(fuso_sao_paulo)

  data_hora = hora_atual_sp.strftime("%Y-%m-%d %Hh%Mm")
  # Nome do arquivo PDF
  nome_arquivo_pdf = f"{nome_pasta}/Correcao do {nome_aluno} - {pontuacao_total} - {data_hora}"

  # Criar o documento LaTeX
  doc = Document()

  # Configurar margens
  doc.packages.add(Package('geometry', options=['a4paper', 'left=1.5cm', 'right=1.5cm', 'top=0.0cm', 'bottom=0.0cm']))
  doc.packages.add(Package('graphicx'))
  doc.packages.add(Package('enumitem'))  # Para personalização de listas

  # Cabeçalho

  # Logo à esquerda
  with doc.create(MiniPage(width=NoEscape(r'0.17\textwidth'), pos='t')) as logo_minipage:
    logo_minipage.append(NoEscape(r'\vspace{0.0cm}'))
    logo_minipage.append(Command('includegraphics', arguments=ifce_logo_path, options=NoEscape(r'width=\linewidth')))
  
  # Texto à direita
  with doc.create(MiniPage(width=NoEscape(r'0.75\textwidth'), pos='t', align='r')) as text_minipage:
    text_minipage.append(NoEscape(r'\vspace{1.5cm}'))
    text_minipage.append(NoEscape(r'{\raggedleft \fontsize{16}{16}\selectfont Disciplina ' + nome_disciplina + r'}\\'))
    text_minipage.append(NoEscape(r'\vspace{0.3cm}'))
    text_minipage.append(NoEscape(r'{\fontsize{16}{16}\selectfont ' + nome_avaliacao + r'}\\'))
    text_minipage.append(NoEscape(r'\vspace{0.3cm}'))
    text_minipage.append(NoEscape(r'{\fontsize{12}{14}\selectfont ' + nome_conteudo + r'}'))
    text_minipage.append(NoEscape(r'\vspace{0.5cm}'))

  # Linha horizontal
  doc.append(NoEscape(r'\\'))
  doc.append(NoEscape(r'\noindent\rule{\textwidth}{0.4pt}\\'))
  doc.append(NoEscape(r'\noindent Nome: ' + nome_aluno + r'\\'))
  doc.append(NoEscape(r'\noindent Data Correção: ' + hora_atual_sp.strftime("%d/%m/%Y") + r'\\'))
  doc.append(NoEscape(r'\noindent\rule{\textwidth}{0.4pt}\\'))

  # Fim de Cabeçalho

  # Apresentação da pergunta do item
  for id_item, (pergunta, rubricas, resposta, (nota, feedback), pontuacao_maxima) in enumerate(zip(perguntas, rubricas, respostas_estudante, avaliacao_corrigida, pontuacoes_maximas), start=1):
    doc.append(NoEscape(r'\textbf{Pergunta do item ' + str(id_item) + r':} ' + pergunta + r'\\'))

    # Montagem dos critérios
    for id_criterio, rubrica in enumerate(rubricas):
      criterio =  rubrica[0]
      criterio_pontos = rubrica[1]
      doc.append(NoEscape(r'\textbf{Critério ' + str(id_criterio + 1) + r' (' + str(criterio_pontos) + ' pontos):} ' + criterio + r'\\'))
 
    # Resposta do estudante
    doc.append(NoEscape(r'\textbf{Resposta do estudante: } ' + resposta+ r'\\'))
    
    # Considerações
    doc.append(NoEscape(r'\textbf{Considerações: }'+ str(feedback[1])+ r'\\'))

    # Nota
    doc.append(NoEscape(r'\textbf{Nota atribuída: ' + str(nota) + r' de ' + str(pontuacao_maxima) + r' pontos }\\'))

    # Feedback
    doc.append(NoEscape(r'\textbf{Feedback: }'+ str(feedback[2])+ r'\\'))
    
    # Linha horizontal
    doc.append(NoEscape(r'\\'))
    doc.append(NoEscape(r'\noindent\rule{\textwidth}{0.4pt}\\'))

  # Gerar o PDF
  doc.generate_pdf(nome_arquivo_pdf)
  return nome_arquivo_pdf