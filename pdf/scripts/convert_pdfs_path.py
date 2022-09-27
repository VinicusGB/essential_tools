# Importação das bibliotecas necessárias
from datetime import date, datetime, timedelta
from diretorio.classe import Diretorio
from os import getcwd, path, listdir, chdir
### Importando a biblioteca
import fitz as fz
import datetime
import os

dir = Diretorio()

# Definindo a base dos arquivos
for open_file in dir.input_files():
    print(open_file)
    ### Lendo o arquivo
    with fz.open(os.path.join(dir.input,open_file)) as file:
            contexts = ''
            i = 0
            for page in file:
                    i += 1
                    contexts += f"<pag {i}>\n"+page.get_text()
    #contexts = contexts[contexts.find('<pag 145>'):contexts.find('<pag 159>')]
    contexts = contexts.replace(" \n"," ")
    contexts = contexts.replace("-\n","")
    ### Salvando o arquivo final
    with open(f"{os.path.join(dir.output,open_file)}.txt","w",encoding='utf-8-sig') as output_file:
        output_file.write(contexts)
