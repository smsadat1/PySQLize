from core.connection import Connection
from core.executor import Executor

def compiler(sql: str):

    conn = Connection('../test.db')
    exec = Executor(conn)

    rows = exec.fetchall(sql)

    return rows
