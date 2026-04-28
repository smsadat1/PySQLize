from core.config import DB_PATH
from core.executor import Executor
from core.connection import Connection


from sql.compiler import compiler

class Query:

    def __init__(self, table):
        self.conn = Connection(DB_PATH)
        self.exec = Executor(self.conn)
        self.table = table

        self._where = None
        self._params = []
        self._limits = None


    def __iter__(self):
        sql, params = self.compile()
        cursor = iter(self.exec.fetchall(sql, params))

        for row in cursor:
            yield row


    def first(self):
        sql, params = self.compile()
        sql += ' LIMIT 1'
        return self.exec.fetchone(sql, params)


    def count(self):
        sql = f'SELECT COUNT(*) FROM {self.table}'

        if self._where:
            sql += f' WHERE {self._where}'

        row = self.exec.fetchone(sql, self._params)
        return row[0]


    def where(self, condition: str, params=None):
        self._where = condition
        if params:
            self._params.extend(params)
        return self


    def limit(self, n: int):
        self._limits = n
        return self


    def compile(self):
        sql = f'SELECT * FROM {self.table}'

        if self._where:
            sql += f' WHERE {self._where}'

        if self._limits:
            sql += f' LIMIT {self._limits}'

        return sql, self._params


    def all(self):
        sql, params = self.compile()
        return self.exec.execute(sql, params)

