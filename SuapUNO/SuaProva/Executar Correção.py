# Utilizar este arquivo para realização das correções.
import os

os.environ["CHAVE_GROQ"] = "insira_a_chave_groq_aqui"

from Utils.Corrigir import corrigir
from Utils.Llama import llama

from CorrecaoN1AP1 import diretorio_ap1_n1, ap1_n1
from CorrecaoN1AP1recuperacao import diretorio_recuperacao_ap1_n1, Recuperacao_ap1_n1
from CorrecaoN1AP2 import diretorio_ap2_n1, ap2_n1
from CorrecaoN2AP1 import diretorio_ap1_n2, ap1_n2
from CorrecaoN2AP1recuperacao import diretorio_recuperacao_ap1_n2, Recuperacao_ap1_n2
from CorrecaoN2AP2 import diretorio_ap2_n2, ap2_n2

lista_alunos = []
#corrigir(diretorio_ap1_n1, ap1_n1, alunos=lista_alunos)

#corrigir(diretorio_recuperacao_ap1_n1, Recuperacao_ap1_n1, alunos=lista_alunos)

#corrigir(diretorio_ap2_n1, ap2_n1, alunos=lista_alunos)

#corrigir(diretorio_ap1_n2, ap1_n2, alunos=lista_alunos)

#corrigir(diretorio_recuperacao_ap1_n2, Recuperacao_ap1_n2, alunos=lista_alunos)

#corrigir(diretorio_ap2_n2, ap2_n2, alunos=lista_alunos)