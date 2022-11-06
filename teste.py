from terminal import *
from pdf import *
from diretorio.classe import Diretorio
from bancodedados.sqllite import BDSQLITE
from email import *
import functools

diretorio = Diretorio()
banco = BDSQLITE(f"{diretorio.base}/teste.db")

colunas =   "TEXTO TEXT NOT NULL,\
            COLUMN2 TEXT"

banco.table_create(table="teste22",columns=colunas)

coluna = "COMENTARIO TEXT"

#banco.table_alter_add_column(table="teste22",new_column=coluna)
banco.table_drop("teste2")
banco.data_select_example_full()
