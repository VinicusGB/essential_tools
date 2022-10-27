from terminal import *
from pdf import *
from diretorio.classe import Diretorio
from bancodedados.sqllite import BDSQLITE
from email import *

diretorio = Diretorio()
banco = BDSQLITE(f"{diretorio.base}/teste.db")
