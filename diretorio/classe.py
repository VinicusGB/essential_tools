from datetime import datetime
from lib2to3.pytree import convert
from subprocess import os

from numpy import empty, iterable

class Diretorio():
    '''
    Classe base de diretório para projetos
    '''
    def __init__(self,projeto=''):
        os.chdir(os.path.join(os.getcwd(),projeto))
        self.base = os.getcwd()
        self.input = os.path.join(self.base,'inputs')
        self.output = os.path.join(self.base,'outputs')
    def __str__(self):
        return self.base
    def make(self) -> None:
        """Cria as pastas input e output"""
        return [os.makedirs(x) for x in [self.input,self.output]]
    def input_list_files(self,e='',s='',p=False):
        """Retorna os arquvios da pasta input.\nFiltros: end = sufixo, start = prefixo, print = bool """
        return [f"{os.listdir(self.input).index(filename)} - {filename}" if p == True else filename for filename in os.listdir(self.input) if filename.endswith(e) and filename.startswith(s)]
    def output_list_files(self,e='',s='',p=False):
        """Retorna os arquvios da pasta output.\nFiltros: end = sufixo, start = prefixo, print = bool """
        return [f"{os.listdir(self.output).index(filename)} - {filename}" if p == True else filename for filename in os.listdir(self.output) if filename.endswith(e) and filename.startswith(s)]
    def input_clear(self):
        """Limpa a pasta input"""
        return [os.remove(os.path.join(self.input,file)) for file in self.input_files()]
    def output_clear(self):
        """Limpa a pasta output"""
        return [os.remove(os.path.join(self.output,file)) for file in self.output_files()]
    def output_save_file(self,filename_output=datetime.now(),f='csv',t='a',e='utf-8',contexts=''):
        """Salva o arquivo na pasta de outputs. filename_output = nome do arquivo\nf = formato do arquivo final\nt = tipo de acesso ao arquivo (a - adiciona nova linha, w = sobreescreve o testo\ne = enconding)"""
        with open(f"{os.path.join(self.output,filename_output)}.{f}",{t},encoding='utf-8') as output_file:
            output_file.write(contexts)
    def input_read_files(self,files,num):
        print('arquvios files')
        print(type(files))
        #print(files)
        print('arquvios files[num]')
        print(type(files[num]))
        print(files[num])
        files1 = iter(files)
        print(type(files1))
        print(files1)
        conteudos = ''
        for file in files:
            print(file)
            enc = open(f"{os.path.join(self.input,file)}","r").encoding
            print(enc)
            with open(f"{os.path.join(self.input,file)}","r",encoding=enc,errors='ignore') as input_file:
                conteudo = ''
                for line in input_file.readlines():
                    conteudo += line
                conteudos += conteudo
            #print(conteudos)
