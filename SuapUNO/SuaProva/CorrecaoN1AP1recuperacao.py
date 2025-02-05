# Utilizar este arquivo para realização das correções.
from Utils.Corrigir import corrigir
from Utils.Llama import llama

diretorio_recuperacao_ap1_n1 = '../../N1-AP1 Recuperação'

# Recuperação AP1-N1: Questões, rubricas e pontuação máxima
Recuperacao_ap1_n1_questoes = ['1. a) Explique por que a disponibilidade de grandes volumes de dados e o aumento na capacidade computacional têm sido fundamentais para o avanço do aprendizado de máquina nos últimos anos.',
             '1. b) Cite e explique dois exemplos de aplicações práticas que se tornaram possíveis ou foram aprimoradas devido a esses avanços.',
             '1. c) Quais são os elementos fundamentais de um sistema de aprendizado supervisionado? Explique cada um (conjunto de treinamento, conjunto de validação/teste, rótulos, variáveis independentes do modelo, modelo, exatidão do modelo, hold-out 80/20, cross-validation).',
             '1. d) Diferencie problemas de classificação e regressão no contexto de aprendizado supervisionado, fornecendo um exemplo prático para cada.',]

Recuperacao_ap1_n1_rubricas=[
    {('os avanços permitiram a criação de modelos relavantes para um maior número de aplicações', 1.0),
     ('permite o treinamento de modelos mais complexos', 1.25),
            ('permite a construção de modelos de parendizado de máquina mais precisos', 1.25),
            ('permite que modelos mais complexos sejam rápidos o suficiente para atenderem a aplicações em tempo real', 1.25)},
    {('dar um exmplo de aplicação que foi possível ser criada dado o aumento da capacidade dos computadores e disponibilidade de dados', 1.25),
            ('dar outro exmplo de aplicação que foi possível ser criada dado o aumento da capacidade dos computadores e disponibilidade de dados', 1.25)},
    {('explicar conjunto de treinamento', 0.32),
            ('explicar significado do termo conjunto de dados de validação/teste ou termo similar', 0.32),
            ('explicar significado do temro rótulo ou termo similar', 0.32),
            ('explicar significado do termo variáveis independentes do modelo ou termo similar', 0.32),
            ('explicar significado do temro modelo ou termo similar', 0.32),
            ('explicar signidicado do termo exatidão do modelo ou temro similar', 0.32),
            ('explicar significado do termo hold-out 80/20 ou termo similar', 0.32),
            ('explicar significado do termo cross-validation ou termo similar', 0.32)},
    {('diferenciar classificação de regressão no contexto de aprendizado de máquina upervisionado', 1.25),
            ('Dar um exemplo de classificação', 0.63),
            ('Dar um exemplo de regressão', 0.63)}
]

Recuperacao_ap1_n1_pontuacao_maxima = [2.5, 2.5, 2.5, 2.5]

Recuperacao_ap1_n1 = [Recuperacao_ap1_n1_questoes, Recuperacao_ap1_n1_rubricas, Recuperacao_ap1_n1_pontuacao_maxima]