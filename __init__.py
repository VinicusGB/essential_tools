import os, sys, importlib

def import_path(fullpath):
    """ 
    Import a file with full path specification. Allows one to
    import from anywhere, something __import__ does not do. 
    """
    path, filename = os.path.split(fullpath)
    filename, ext = os.path.splitext(filename)
    sys.path.append(path)
    module = __import__(filename)
    importlib.reload(module)
    del sys.path[-1]
    return module

#import_path("C:\Projetos\essential_tools\diretorio\diretorio_classe.py")
import_path("C:\Projetos\essential_tools\\essential_tools.py")
