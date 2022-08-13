#
#       Esse programa recebe um PDF com a tabela de conversão de
#       CBO 1994 para CBO 2002, processa esse PDF e salva um dict
#       com a tabela.
#
from tika import parser
import csv

#Abre PDF com tabela de conversão
raw = parser.from_file('convert.pdf')

#Limpa dados
raw['content'] = raw['content'].replace('-', '')
raw['content'] = raw['content'].replace('X', '')

#Transforma em um dict
dict_cbo = dict()
dict_cbo['CBO2002'] = 'CBO1994'

for i in raw['content'].splitlines():
    
    if i == 'TÍTULOS20021994 TÍTULOS20021994 CBO 2002' or len(i) < 12:
        continue
    
    if i[2].isnumeric():
        dict_cbo[i[6:12]] = i[:5]

#Salva em um csv
with open('converted.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in dict_cbo.items():
       writer.writerow([key, value])