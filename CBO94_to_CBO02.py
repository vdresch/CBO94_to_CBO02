#
#       Esse programa recebe um PDF com a tabela de conversão de
#       CBO 1994 para CBO 2002, processa esse PDF e salva um dict
#       com a tabela.
#
from tika import parser
import re
import pickle

#Abre PDF com tabela de conversão
raw = parser.from_file('convert.pdf')

#Limpa dados
raw['content'] = raw['content'].replace('-', '')
raw['content'] = raw['content'].replace('X', '0')

#Transforma em um dict
dict_cbo = dict()

for i in raw['content'].splitlines():
    
    if i == 'TÍTULOS20021994 TÍTULOS20021994 CBO 2002' or len(i) < 12:
        continue
    
    if i[2].isnumeric():
        dict_cbo[i[6:12]] = i[:5]

#Salva em um picle
with open('Tabela_conversao_CBO.pkl', 'wb') as f:
    pickle.dump(dict_cbo, f)