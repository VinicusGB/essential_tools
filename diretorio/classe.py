from subprocess import os

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
    def make(self):
        """Cria as pastas input e output"""
        return [os.makedirs(x) for x in [self.input,self.output]]
    def list_input_files(self,e='',s='',p=False) -> list:
        """Retorna os arquvios da pasta input.\nFiltros: end = sufixo, start = prefixo, print = bool """
        return [print(f"{self.output_files().index(filename)} - {filename}") if p == True else os.listdir(self.output) for filename in self.output_files() if filename.endswith(e) and filename.startswith(s)]
    def list_output_files(self,e='',s='',p=False) -> list:
        """Retorna os arquvios da pasta output.\nFiltros: end = sufixo, start = prefixo, print = bool """
        return [print(f"{self.output_files().index(filename)} - {filename}") if p == True else os.listdir(self.output) for filename in self.output_files() if filename.endswith(e) and filename.startswith(s)]
    def input_clear(self):
        """Limpa a pasta input"""
        return [os.remove(os.path.join(self.input,file)) for file in self.input_files()]
    def output_clear(self):
        """Limpa a pasta output"""
        return [os.remove(os.path.join(self.output,file)) for file in self.output_files()]
