# Utilizar este arquivo para realização das correções.
from Utils.Corrigir import corrigir
from Utils.Llama import llama

diretorio_ap1_n1 = '../../N1-AP1'

# AP1-N1: Questões, rubricas e pontuação máxima
ap1_n1_questoes = ['1a) ...',
                   '1b) ...',
                   '2a) ...',
                   '2b) ...']

ap1_n1_rubricas=[
    {('...', 0.32),
     ('...', 0.32),
     ('...', 0.32)},
       {('...', 1.0),
        ('...', 1.0),
         ('...', 0.5)},
          {('...', 1.0),
           ('...', 1.0),
            ('...', 1.0)},
             {('...', 2.50),
              ('...', 1.25),
              ('...',0.0)}]

ap1_n1_pontuacao_maxima = [2.5, 2.5, 2.5, 2.5]

ap1_n1 = [ap1_n1_questoes, ap1_n1_rubricas, ap1_n1_pontuacao_maxima]