from core.config import DB_PATH
from core.executor import Executor
from core.connection import Connection

from sql.compiler import compiler

class Query:

    def __init__(self, db, table):
        self.exec = db
        
        if isinstance(table, str):
            self.table = table
        else:
            self.table = table.__tablename__

        self._limits = None
        self._order = None
        self._where = None


    def __iter__(self):
        sql, params = self.compile()
        cursor = iter(self.exec.fetchall(sql, params))

        for row in cursor:
            yield row


    def count(self):
        sql, params = self.compile()
        sql = sql.replace('SELECT *', 'SELECT COUNT(*)')

        row = self.exec.fetchone(sql, params)
        return row[0] if row else 0


    def exists(self):
        sql = f'SELECT 1 FROM {self.table}'
        params = []

        if self._where is not None:
            where_sql, where_params = self._where.compile()
            sql += f' WHERE {where_sql}'
            params += where_params

        sql += ' LIMIT 1'
        row = self.exec.fetchone(sql, params)
        return row is not None


    def first(self):
        sql, params = self.compile()
        sql += ' LIMIT 1'
        return self.exec.fetchone(sql, params)


    def get(self):
        sql, params = self.compile()
        sql += " LIMIT 2"
        rows = self.exec.fetchall(sql, params)

        if len(rows) == 0:
            return None
        if len(rows) > 1:
            raise Exception('Multiple rows returned')

        return rows[0]


    def limit(self, n: int):
        self._limits = n
        return self


    def order_by(self, clause: str):
        self._order = clause
        return self
    

    def where(self, expr):
        if self._where is not None:
            self._where = self._where & expr
        else:
            self._where = expr
        return self


    def compile(self):
        sql = f'SELECT * FROM {self.table}'
        params = []

        if self._where is not None:
            where_sql, where_params = self._where.compile()
            sql += f' WHERE {where_sql}'
            params += where_params

        if self._order:
            sql += f' ORDER BY {self._order}'

        if self._limits:
            sql += f' LIMIT {self._limits}'

        return sql, params


    def all(self):
        sql, params = self.compile()
        return self.exec.fetchall(sql, params)


    def show_sql(self):
        sql, params = self.compile()

        for param in params:
            if isinstance(param, str):
                escaped = param.replace("'", "''")
                value = f'{escaped}'
            else:
                value = str(param)

            sql = sql.replace('?', value, 1)

        return sql
