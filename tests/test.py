from core.connection import Connection
from core.executor import Executor

conn = Connection('../test.db')
exec = Executor(conn)

exec.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)')
exec.execute('INSERT INTO users VALUES (?, ?)', (1, 'Siam'))

rows = exec.fetchall('SELECT * FROM users')

for row in rows:
    print(dict(row))