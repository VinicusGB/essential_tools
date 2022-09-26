# Importação das bibliotecas necessárias
from datetime import date, datetime, timedelta
from os import getcwd, path, listdir, chdir
### Importando a biblioteca
import fitz as fz
import datetime
import os


class Convert_PDF():
        """
        Classe para conversão de arquivos PDF para TXT, CSV e TSV
        """
        def __init__(self,BASE_DIR,INPUT_DIR,OUTPU_DIR) -> None:
              self.BASE_DIR = BASE_DIR
              self.



# Definindo a base dos arquivos
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR,'data/files_pdf')
os.chdir(BASE_DIR)
print(f"DATA_DIR: {DATA_DIR}")
list_files_names = os.listdir(DATA_DIR)
#file_test = DATA_DIR +'/'+ list_files_names[5]
#print(f"FILE_NAME: {file_test}")
SAVE_DIR = "data/outputs_files_pdf/"

for open_file in list_files_names:
    print(open_file)
    ### Lendo o arquivo
    with fz.open(f'{DATA_DIR}/{open_file}') as file:
            contexts = ''
            i = 0
            for page in file:
                    i += 1
                    contexts += f"<pag {i}>\n"+page.get_text()
    #contexts = contexts[contexts.find('<pag 145>'):contexts.find('<pag 159>')]
    contexts = contexts.replace(" \n"," ")
    contexts = contexts.replace("-\n","")
    ### Salvando o arquivo final
    with open(f"{SAVE_DIR}{open_file}.txt","w",encoding='utf-8-sig') as output_file:
        output_file.write(contexts)
