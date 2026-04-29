from core.config import DB_PATH
from core.executor import Executor
from core.connection import Connection

from sql.compiler import compiler

class Query:

    def __init__(self, db, table):
        self.exec = db
        self.table = table

        self._limits = None
        self._order = None
        self._params = []
        self._where = None


    def __iter__(self):
        sql, params = self.compile()
        cursor = iter(self.exec.fetchall(sql, params))

        for row in cursor:
            yield row


    def count(self):
        sql = f'SELECT COUNT(*) FROM {self.table}'

        if self._where:
            sql += f' WHERE {self._where}'

        row = self.exec.fetchone(sql, self._params)
        return row[0]


    def exists(self):
        sql, params = self.compile()
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
    

    def where(self, expression, params = None):
        self._where = expression
        if params:
            self._params.extend(params)
        return self


    def compile(self):
        sql = f'SELECT * FROM {self.table}'

        if self._where:
            where_sql, params = self._where.compile()
            sql += f'WHERE {where_sql}'
            self._params += params

        if self._limits:
            sql += f' LIMIT {self._limits}'

        if self._order:
            sql += f' ORDER BY {self._order}'

        return sql, self._params


    def all(self):
        sql, params = self.compile()
        return self.exec.fetchall(sql, params)

