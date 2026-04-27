# test connector and executor

from core.config import DB_PATH
from core.connection import Connection
from core.executor import Executor

conn = Connection(DB_PATH)
exec = Executor(conn)

exec.execute("DROP TABLE IF EXISTS users")

exec.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, age INTEGER)')

exec.execute('INSERT INTO users (id, name, age) VALUES (?, ?, ?)', (1, 'Siam', 23))
exec.execute('INSERT INTO users (id, name, age) VALUES (?, ?, ?)', (1, 'Saif', 13))
exec.execute('INSERT INTO users (id, name, age) VALUES (?, ?, ?)', (1, 'Rafi', 19))
exec.execute('INSERT INTO users (id, name, age) VALUES (?, ?, ?)', (1, 'Araf', 30))


rows = exec.fetchall('SELECT * FROM users')

for row in rows:
    print(dict(row))