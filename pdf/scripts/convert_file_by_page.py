# Importação das bibliotecas necessárias
from datetime import date, datetime, timedelta
from diretorio.classe import Diretorio
from os import getcwd, path, listdir, chdir
### Importando a biblioteca
import fitz as fz
import datetime
import os

dir = Diretorio()

i = 0

for file in dir.input_files():
    print(f'({i}) - {file}')
    i += 1

c = int(input("Escolha um arquivo"))
a,b = input("Digite a página inicial e final").split('-')

# Definindo a base dos arquivos
print(dir.input_files()[c])

### Lendo o arquivo
with fz.open(os.path.join(dir.input,dir.input_files()[c])) as file:
        contexts = ''
        i = 0
        for page in file:
                i += 1
                contexts += f"<pag {i}>\n"+page.get_text()
contexts = contexts[contexts.find('<pag {a}>'):contexts.find('<pag {b}>')]
contexts = contexts.replace(" \n"," ")
contexts = contexts.replace("-\n","")

### Salvando o arquivo final
with open(f"{os.path.join(dir.output,dir.input_files()[c])}.txt","w",encoding='utf-8-sig') as output_file:
    output_file.write(contexts)
