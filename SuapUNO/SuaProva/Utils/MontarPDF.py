import pytz
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPS
from textwrap import wrap


def montar_pdf_correcao(nome_estudante_, perguntas, rubricas, respostas_estudante, avaliacao_corrigida, nome_pasta="."):
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
    if not (len(perguntas) == len(rubricas) == len(respostas_estudante) == len(avaliacao_corrigida)):
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
    renderPS.drawToFile(c, 'ifce_logo.png')

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
