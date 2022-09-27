"""
Convert arquivos de pdf para o formato necessário
"""
# Importação das bibliotecas necessárias
from datetime import date, datetime, timedelta
from subprocess import os
#from .. email import outlook
from .. terminal import *

dt_now = date.today()

BASE_DIR = os.getcwd()
INPUT_DIR = os.path.join(BASE_DIR,'input')
OUTPUT_DIR = os.path.join(BASE_DIR,'output')
#os.chdir(BASE_DIR)
#list_files_names = os.listdir(DATA_DIR)
#file_test = DATA_DIR +'\\'+ list_files_names[0]
#print(f"FILE_NAME: {file_test}")

print('\n\
##################\n\
### LEITOR PDF ###\n\
##################\n\n')

print(dt_now)

print("\nBemvindo, escolha uma opção abaixo:\n\n\
    0. SAIR\n\
    1. CONVERT_PDF\n\
        ")
