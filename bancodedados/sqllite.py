import sqlite3

class BDSQLITE():
    """
    Bando de Dados SQLlite
    """
    def __init__(self,path):
        """
        Criar conexão com o banco e cursor.
        """
        self.connect = sqlite3.connect(path)
        self.cursor = self.connect.cursor()
    def create_table(self,table,columns):
        """
        Criar uma tabela.
            table = nome_tabela
            columns = colunas com parâmetros
            e.g.: 'CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
              'prod_name TEXT, valor REAL)'
        """
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table}({columns})')
    def data_insert(self,table,columns,values):
        """
        Inserir uma linha na tabela.
            tabela = nome_tabela
            columns = nome_colunas
            values = valores
            e.g.: "INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?, ?)"
        """
        self.cursor.execute(f"INSERT INTO {table} ({columns}) VALUES(?, ?, ?, ?)",(values))
        self.connect.commit()
        self.cursor.close()
        self.connect.close()
    def data_select(self,table,columns='*'):
        """
        Ler dados.
            table = nome_tabela
            columns = nome das colunas. default = *
            e.g.: "SELECT * FROM PRODUTOS"
        """
        self.cursor.execute(f"SELECT {columns} FROM {table}")
        for line in self.cursor.fetchall():
            print(line)
    def data_select_where(self,table,columns,conditional):
        """
        Ler dados com filtro de dados
            table = nome_tabela
            columns = nome das colunas. default = *
            where = condição
            e.g.: "SELECT * FROM PRODUTOS"
        """
        self.cursor.execute(f"SELECT {columns} FROM {table} WHERE {conditional}")
        for line in self.cursor.fetchall():
            print(line)      
    def data_update(self,table,values,conditional):
        """
        Atualizar dados.
            table = nome_tabela
            values = valores para atualização
            conditional = condição de atualização
            e.g.: "UPDATE produtos SET valor = 70.00 WHERE valor > 80.0"
        """
        self.cursor.execute(f"UPDATE {table} SET {values} WHERE {conditional}")
        self.connect.commit()
    def data_delete(self,table,conditional):
        """
        Remover dados.
            table = nome_tabela
            values = valores para atualização
            conditional = condição de atualização
            e.g.: "DELETE FROM produtos WHERE valor = 62.0"
        """
        self.cursor.execute(f"DELETE FROM {table} WHERE {conditional}")
        self.connect.commit()
    def tables(self):
        [print(f"table: {table[1]}, coluns: {table[-1].split('(')[1].split(',')}") for table in self.cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")]
