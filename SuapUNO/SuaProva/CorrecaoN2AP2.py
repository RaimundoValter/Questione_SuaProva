# Utilizar este arquivo para realização das correções.

diretorio_ap2_n2 = '../../N2-AP2'

# AP2-N2: Questões, rubricas e pontuação máxima
ap2_n2_questoes = ['1) Uma startup inovadora do Vale do Jaguaribe está treinando uma rede neural artificial profunda para detectar viveiros de camarão por meio da segmentação de imagens de satélite. Para isso, foi utilizada a composição das bandas espectrais R (vermelho), G (verde), B (azul) e NIR (infravermelho próximo). Durante o processo de treinamento do algoritmo de deep learning, observou-se que a perda (loss) no conjunto de treino diminui de forma consistente, enquanto a perda no conjunto de validação começa a aumentar após algumas épocas. Explique o fenômeno observado e seus possíveis impactos no desempenho do modelo final.',
                   '2) Um pesquisador está ajustando uma rede neural artificial e percebe que, com uma taxa de aprendizado muito alta, o modelo oscila sem convergir. Ao diminuir a taxa de aprendizado, a convergência ocorre, mas de forma muito lenta. Ele decide adicionar um termo de momento ao otimizador. Explique como o momento influencia o treinamento e por que ele pode ajudar nessa situação.',
                   '3) Você recebeu um conjunto de dados contendo metadados de exames de imagem e informações clínicas de pacientes (18 atributos ao total) para auxiliar no diagnóstico de doenças pulmonares. Com base nesses dados, projete uma rede neural artificial capaz de classificar os pacientes em três categorias: saudável, pneumonia viral ou pneumonia bacteriana. Na sua resposta, aborde os seguintes aspectos: 1.	Arquitetura da rede: descreva as camadas utilizadas, o número de neurônios em cada camada, as funções de ativação escolhidas e as estratégias para evitar overfitting. Considere que estejas utilizando todos os atributos disponíveis. 2.	Pré-processamento dos dados: explique como os metadados das imagens e as informações clínicas devem ser pré-processados, considerando que serão utilizados no treinamento de uma rede neural. 3.	Treinamento e avaliação: detalhe como você treinará e validará o modelo proposto. 4.	Exemplo de aplicação: apresente um cenário prático onde o modelo seria utilizado.',
                   '4) Uma equipe de cientistas de dados está treinando uma rede neural artificial profunda para prever quais clientes responderão positivamente a uma campanha de marketing. Após algumas épocas de treinamento, o modelo começa a apresentar um desempenho excepcional no conjunto de treino, mas um desempenho ruim no conjunto de teste. Eles decidem adicionar dropout em algumas camadas da rede. Explique como o dropout funciona e por que pode ajudar a melhorar a capacidade de generalização do modelo?']

ap2_n2_rubricas=[
    {
        ("Explicação clara do fenômeno de overfitting observado, destacando a relação entre as perdas (loss) de treino e validação.", 1.0),
        ("Citar e/ou explicar o impacto do everfitting na generalização do modelo final.", 1.0),
        ("Citação e/ou explicar pelo menos uma estratégia para mitigar o overfitting.", 0.5)
    },
    {
        ("Ao explicar, citar e/ou explicar que o momento no otimizador pode acelerar a convergência, introduzindo um termo a mais no cálculo da atualização dos pesos p(t+1)=p(t)+lr*E*erro+alfa*[p(t)-p(t-1)] **o estudante não precisa explicitar a fórmula**.", 1.5),
        ("Ao responder o porquê, citar e/ou explicar que o momento ajudará a reduzir a perda mais rapidamente, não intorduzindo instabilidade ao modelo.", 1.0)
    },
    {
        ("Descrever corretamente a arquitetura da rede, incluindo número de camadas, neurônios, funções de ativação e o uso de pelo menos uma estratégia (dropout/normalização/etc.) para controlar overfitting.", 1.0),
        ("Citar e/ou explicar que o pré-processamento dos dados clínicos e de metadados das imagem resultará em atributos de entrada números normalizados na rede neural.", 0.5),
        ("Discussão breve/simplificada sobre o treinamento e validação do modelo, incluindo métricas de avaliação.", 0.5),
        ("Exemplo de aplicação realista e relevante para a rede neural desenvolvida.", 0.5)
    },
    {
        ("Explicação de como o dropout funciona na camada da rede neural e em que momento é utilizado (apenas durante o terinamento) para redução de overfitting.", 1.25),
        ("Discussão breve/simplificada sobre como o dropout melhora a capacidade de generalização do modelo.", 1.25)
    }
]

ap2_n2_pontuacao_maxima = [2.5, 2.5, 2.5, 2.5]

ap2_n2 = [ap2_n2_questoes, ap2_n2_rubricas, ap2_n2_pontuacao_maxima]
