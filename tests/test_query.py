from sql.query import Query

from tests.test_model import User


def test_where_filter(db):
    q = Query(db, User).where(User.age > 20)
    rows = q.all()
    assert len(rows) == 9
    assert rows[0]['name'] == 'Siam'
    
    expected_sql = "SELECT * FROM users WHERE (age > 20)"
    assert q.show_sql() == expected_sql


def test_where_chain_filter(db):
    q = Query(db, User).where(User.age > 20).where(User.email == 'sifat344@email.com')
    rows = q.all()
    assert len(rows) == 1
    assert rows[0]['name'] == 'Sifat'

    expected_sql = "SELECT * FROM users WHERE ((age > 20) AND (email = sifat344@email.com))"
    assert q.show_sql() == expected_sql


def test_count(db):
    q = Query(db, User).where(User.age < 27)
    assert q.count() == 4

    expected_sql = "SELECT * FROM users WHERE (age < 27)"
    assert q.show_sql() == expected_sql


def test_exists(db):
    q = Query(db, User).where(User.name == 'Syed')
    assert q.exists() == True

    expected_sql = "SELECT * FROM users WHERE (name = Syed)"
    assert q.show_sql() == expected_sql


def test_first(db):
    q = Query(db, User).where(User.age >= 27)
    row = q.first()
    assert row['name'] == 'Sifat'

    expected_sql = "SELECT * FROM users WHERE (age >= 27)"
    assert q.show_sql() == expected_sql


def test_get(db):
    q = Query(db, User).where(User.age == 22)
    rows = q.get()
    if rows:
        assert rows['name'] == 'Shamim'

    expected_sql = "SELECT * FROM users WHERE (age = 22)"
    assert q.show_sql() == expected_sql

