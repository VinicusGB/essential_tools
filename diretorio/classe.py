from subprocess import os

class Diretorio():
    '''
    Classe base de diretório para projetos
    '''
    def __init__(self):
        self.base = os.getcwd()
        self.input = os.path.join(self.base,'inputs')
        self.output = os.path.join(self.base,'outputs')
    def __str__(self):
        return self.base
    def make(self):
        return [os.makedirs(x) for x in [self.input,self.output]]        
    def input_files(self):
        return os.listdir(self.input)
    def output_files(self):
        return os.listdir(self.output)
    def input_clear(self):
        return [os.remove(os.path.join(self.input,file)) for file in self.input_files() ]
    def output_clear(self):
        return [os.remove(os.path.join(self.output,file)) for file in self.output_files()]

dir = Diretorio()
