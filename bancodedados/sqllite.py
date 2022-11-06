import sqlite3
import functools
from datetime import datetime


class BDSQLITE():
    """
    Bando de Dados SQLlite
        DATATYPES:  https://www.sqlite.org/datatype3.html
        QUERYS:     https://www.w3schools.com/SQl/sql_alter.asp
        TECHINNET:  https://www.techonthenet.com/sqlite/tables/alter_table.php
        
    """
    def __init__(self,fullpath):
        """
        Criar conexão com o banco e cursor.
        """
        self.diretorio = fullpath
        self.connect = sqlite3.connect(self.diretorio)
        self.cursor = self.connect.cursor()
    def connect_commit_close(func,self):
        @functools.wraps(func)
        def wrappert_connect_commit_close(*args,**kwargs):
            # Do something before
            print("Estabelecendo conexão com o banco")
            connect = sqlite3.connect(self.diretorio)
            print("Intânciando o cursor")
            cursor = connect.cursor()

            # Function executable
            value = func(*args,**kwargs)

            # Do something after
            self.connect.commit()
            self.cursor.close()
            print("Fechando conexão com o banco de dados.")
            self.connect.close()
            
            return value
        return wrappert_connect_commit_close
    def start_connect(self):
        print("Estabelecendo conexão com o banco")
        setattr(self,'connect',sqlite3.connect(self.diretorio))
        print("Intânciando o cursor")
        setattr(self,'cursor',self.connect.cursor())
    def end_connect(self):
        self.connect.commit()
        self.cursor.close()
        print("Fechando conexão com o banco de dados.")
        self.connect.close()
    """
    DDL - DATA DEFINITION LANGUAGE - LINGUAGEM DE DEFINIÇÃO DOS DADOS
    """
    def table_create(self,table,columns):
        """
        Criar uma tabela.
            table = nome_tabela
            columns = colunas com parâmetros
            e.g.: 'CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
              'prod_name TEXT, valor REAL)'
        """
        # Do something before
        self.start_connect()
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table} (\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            created_date TIMESTAMP AUTO,\
            modified_date TIMESTAMP AUTO,\
            {columns});')
        self.end_connect()
    def table_alter(self,table,columns):
        """
        Altera uma tabela.
            table = nome_tabela
            columns = colunas com parâmetros
            e.g.: 'ALTER TABLE produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
              'prod_name TEXT, valor REAL)'
        """
        self.start_connect()
        self.cursor.execute("PRAGMA foreign_keys=off;")
        self.cursor.execute("BEGIN TRANSACTION;")
        self.cursor.execute(f"ALTER TABLE {table} RENAME TO old_{table};")
        self.cursor.execute(f"CREATE TABLE {table}({columns});")
        self.cursor.execute(f"INSERT INTO {table}({columns})\
            SELECT {columns}\
            FROM old_{table};")
        self.connect.commit()
        self.cursor.execute("PRAGMA foreign_keys=on;")
        self.end_connect()
    def table_drop(self,table):
        """
        Deletar uma tabela.
            table = nome_tabela
            e.g.: 'DROP TABLE [ IF EXISTS ] table_name;'
        """
        # Do something before
        self.start_connect()
        self.cursor.execute(f'DROP TABLE IF EXISTS {table};')
        self.end_connect()
    def table_truncate(self,table):
        """
        Deletar os dados de uma tabela.
            table = nome_tabela
            e.g.: 'DELETE FROM table_name;'
        """
        # Do something before
        self.start_connect()
        self.cursor.execute(f'DELETE FROM {table};')
        self.end_connect()
    def tables_list(self):
        self.start_connect()
        self.cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
        self.end_connect()
    def table_alter_add_column(self,table,new_column):
        """
        Adicionar um novo campo a uma tabela.
            table = nome_tabela
            columns = colunas com parâmetros
            e.g.: 'ALTER TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
              'prod_name TEXT, valor REAL)'
        """
        self.start_connect()
        self.cursor.execute(f'ALTER TABLE {table}\
            ADD {new_column};')
        self.end_connect()
    """
    DML - DATA MANIPULATION LANGUAGE - LINGUAGEM DE MANIPULAÇÃO DE DADOS
    """
    def data_insert(self,table,columns,values):
        """
        Inserir uma linha na tabela.
            tabela = nome_tabela
            columns = nome_colunas
            values = valores
            e.g.: "INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?, ?)"
        """
        self.start_connect()
        for value in values:
            date_published = datetime.datetime.now()
            self.cursor.execute(f"INSERT INTO {table} (date_published,{columns}) VALUES(?, ?, ?, ?)",f"({date_published},{value})")
        self.end_connect()
    def data_update(self,table,values,conditional):
        """
        Atualizar dados.
            table = nome_tabela
            values = valores para atualização
            conditional = condição de atualização
            e.g.: "UPDATE produtos SET valor = 70.00 WHERE valor > 80.0"
        """
        self.start_connect()
        self.cursor.execute(f"UPDATE {table} SET {values} WHERE {conditional}")
        self.end_connect()
    def data_delete(self,table,conditional):
        """
        Remover dados.
            table = nome_tabela
            values = valores para atualização
            conditional = condição de atualização
            e.g.: "DELETE FROM produtos WHERE valor = 62.0"
        """
        self.start_connect()
        self.cursor.execute(f"DELETE FROM {table} WHERE {conditional}")
        self.end_connect()
    """
    DQL - DATA QUERY LANGUAGE = LINGUAGEM DE CONSULTA DE DADOS
    """
    def data_select(self,table,columns='*'):
        """
        Ler dados.
            table = nome_tabela
            columns = nome das colunas. default = *
            e.g.: "SELECT * FROM PRODUTOS"
        """
        self.start_connect()
        self.cursor.execute(f"SELECT {columns} FROM {table}")
        for line in self.cursor.fetchall():
            print(line)
        self.end_connect()
    def data_select_where(self,table,columns,conditional):
        """
        Ler dados com filtro de dados
            table = nome_tabela
            columns = nome das colunas. default = *
            where = condição
            e.g.: "SELECT * FROM PRODUTOS"
        """
        self.start_connect()
        self.cursor.execute(f"SELECT {columns} FROM {table} WHERE {conditional}")
        for line in self.cursor.fetchall():
            print(line)
        self.end_connect()
    def data_select_example_full(self):
        print("""
        SELECT [ ALL | DISTINCT ]
                ALL - Opcional. Se especificado, ele retorna todas as linhas correspondentes.
                DISTINCT - Opcional. Se especificado, ele remove duplicatas do conjunto de resultados.\n\
                    Saiba mais sobre acláusula DISTINTA.
            expressions - As colunas ou cálculos que você deseja recuperar.\n\
                    Use * se desejar selecionar todas as colunas.
        FROM tables - As tabelas que você deseja recuperar registros.\n\
                    Deve haver pelo menos uma tabela listada na cláusula FROM.
            [WHERE conditions] Opcional As condições que devem ser cumpridas para que os registros sejam selecionados.
            [GROUP BY expressions] Opcional. Ele coleta dados em vários registros e agrupa os resultados\n\
                     por uma ou mais colunas. Saiba mais sobre a cláusula GRUPO POR.
            [HAVING condition] Opcional. É usado em combinação com o GRUPO BY para restringir os\n\
                     grupos de linhas devolvidas apenas àqueles cuja condição é TRUE. Saiba mais sobre acláusula TER.
            [ORDER BY expression [ ASC | DESC ]] Opcional. É usado para classificar os registros em seu conjunto de resultados.\n\
                    Saiba mais sobre acláusula ORDEM POR CLÁUSULA.
            [LIMIT number_rows OFFSET offset_value]; Opcional. Se o LIMIT for fornecido, ele controla o número máximo de registros para recuperar.\n\
                     No máximo, o número de registros especificados pornumber_rowsserá devolvido no conjunto de resultados.\n\
                     A primeira linha devolvida pela LIMIT será determinada poroffset_value.
        
        #############

        SELECT employees.employee_id, employees.last_name, positions.title
        FROM employees
        INNER JOIN positions
        ON employees.employee_id = positions.employee_id
            ORDER BY positions.title;
        """)
    def execute_query(self,COMMAND):
        self.start_connect()
        self.cursor.execute(COMMAND)
        self.end_connect()
