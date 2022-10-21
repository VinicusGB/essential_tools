"""
Usar ANSI Escape Codes para imprimir texto colorido em Python
Fonte: https://www.delftstack.com/pt/howto/python/python-print-colored-text/#:~:text=Em%20resumo%2C%20a%20%C3%BAnica%20forma%20de%20imprimir%20texto,consola%20compreender%20as%20instru%C3%A7%C3%B5es%20da%20declara%C3%A7%C3%A3o%20print%28%29de%20Python.
"""
from colorama import Fore, Style, Back
from .fontes import *
from .fundos import *

#OK = '\033[92m' #GREEN
#WARNING = '\033[93m' #YELLOW
#FAIL = '\033[91m' #RED
#RESET = '\033[0m' #RESET COLOR
#BOLD = '\033[;1m'

def MENSAGEM_SUCESSO(TEXTO):
        print(f"{Fore.GREEN}{Style.BRIGHT}{TEXTO}{Fore.RESET}{Style.RESET_ALL}")
def MENSAGEM_ATENCAO(TEXTO:str):
        print(f"{Fore.YELLOW}{Style.BRIGHT}{TEXTO}{Fore.RESET}{Style.RESET_ALL}")
def MENSAGEM_ALERTA(TEXTO):
        print(f"{Fore.RED}{Style.BRIGHT}{TEXTO}{Fore.RESET}{Style.RESET_ALL}")
def MENSAGEM_INFORME(TEXTO):
        print(f"{Back.BLUE}{Fore.WHITE}{Style.BRIGHT}{TEXTO}{Style.RESET_ALL}")
def MENSAGEM_ERRO(TEXTO):
        print(f"{Back.RED}{Style.BRIGHT}{TEXTO}{Style.RESET_ALL}")
