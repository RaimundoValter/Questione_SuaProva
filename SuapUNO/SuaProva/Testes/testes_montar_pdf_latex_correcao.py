from SuaProva.Utils.MontarPDF import montar_pdf_latex

# Teste unitário:

nome_estudante_teste = "João Silva"

perguntas_teste = ["Explique o conceito de polimorfismo.",
                   "O que é herança em POO?",]

rubricas_teste = [
    {("Resposta deve conter exemplos e explicações claras sobre polimorfismo.", 5.0)},
    {("Resposta deve incluir exemplos de classes e subclasses.", 5.0)},
]

respostas_estudante_teste = [
    "Polimorfismo é quando um método pode se comportar de maneiras diferentes.",
    "Herança é quando uma classe herda características de outra classe."
]

avaliacao_corrigida_teste = [
    (4.0, {1: "Boa explicação com exemplo relevante.",
           2: "Continue aprofundando em exemplos.",
           3: 4.0}),
    (4.9, {1 : "Explicação clara, mas sem exemplos práticos.",
           2 : "Adicione exemplos para melhorar a resposta.",
           3 : 5.0}),
]

pontuacoes_maximas = [4.0, 5.0]

nome_pasta_teste = "./"

nome_disciplina_teste = "Inteligência Artificial"
nome_avaliacao_teste = "AP1-N1"
nome_conteudo_teste = "Métodos Conxionistas: RNN e CNN"

# Chamar a função e verificar saída
caminho_pdf = montar_pdf_latex(nome_disciplina_teste, nome_avaliacao_teste, nome_conteudo_teste, nome_estudante_teste, perguntas_teste, rubricas_teste, respostas_estudante_teste, avaliacao_corrigida_teste, pontuacoes_maximas, nome_pasta_teste)

print(f"Arquivo criado em: {caminho_pdf}")
