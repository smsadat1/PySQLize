import pytest

from core.connection import Connection
from core.executor import Executor

@pytest.fixture
def db():

    conn = Connection(':memory:')
    exec = Executor(conn)

    exec.execute('CREATE TABLE users (id INTEGER, name TEXT, age INTEGER)')

    exec.execute("INSERT INTO users VALUES(?, ?, ?)", [1, 'Siam', 23])
    exec.execute("INSERT INTO users VALUES(?, ?, ?)", [2, 'Shamim', 22])
    exec.execute("INSERT INTO users VALUES(?, ?, ?)", [3, 'Sifat', 27])
    exec.execute("INSERT INTO users VALUES(?, ?, ?)", [4, 'Syed', 31])
    exec.execute("INSERT INTO users VALUES(?, ?, ?)", [5, 'Saif', 40])
    exec.execute("INSERT INTO users VALUES(?, ?, ?)", [6, 'Rifat', 20])
    exec.execute("INSERT INTO users VALUES(?, ?, ?)", [7, 'Emon', 21])
    exec.execute("INSERT INTO users VALUES(?, ?, ?)", [8, 'Raihan', 29])
    exec.execute("INSERT INTO users VALUES(?, ?, ?)", [9, 'Mahfuj', 30])
    exec.execute("INSERT INTO users VALUES(?, ?, ?)", [10, 'Ishan', 39])

    return exec