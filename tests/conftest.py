import pytest

from core.connection import Connection
from core.executor import Executor

@pytest.fixture
def db():

    conn = Connection(':memory:')
    exec = Executor(conn)

    exec.execute(
        '''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            age INTEGER,
            email TEXT CHECK(email LIKE '%@%.%')
        )
        '''
    )

    exec.execute("INSERT INTO users VALUES(?, ?, ?, ?)", [1, 'Siam', 23, 'siam123@gmail.com'])
    exec.execute("INSERT INTO users VALUES(?, ?, ?, ?)", [2, 'Shamim', 22, 'shamim298@gmail.com'])
    exec.execute("INSERT INTO users VALUES(?, ?, ?, ?)", [3, 'Sifat', 27, 'sifat344@email.com'])
    exec.execute("INSERT INTO users VALUES(?, ?, ?, ?)", [4, 'Syed', 31, 'syed455@yahoo.com'])
    exec.execute("INSERT INTO users VALUES(?, ?, ?, ?)", [5, 'Saif', 40, 'saif909@proton.com'])
    exec.execute("INSERT INTO users VALUES(?, ?, ?, ?)", [6, 'Rifat', 20, 'rifat123@gmail.com'])
    exec.execute("INSERT INTO users VALUES(?, ?, ?, ?)", [7, 'Emon', 21, 'fde873bd@email.com'])
    exec.execute("INSERT INTO users VALUES(?, ?, ?, ?)", [8, 'Raihan', 29, 'euler@mailmail.com'])
    exec.execute("INSERT INTO users VALUES(?, ?, ?, ?)", [9, 'Mahfuj', 30, 'pasf3fd5@mailmail.com'])
    exec.execute("INSERT INTO users VALUES(?, ?, ?, ?)", [10, 'Ishan', 39, 'oirt35485343@gmail.com'])

    return exec