from sql.query import Query

def test_where_filter(db):
    q = Query(db, 'users').where('age > ?', [20])
    rows = q.all()

    assert len(rows) == 5 
    assert rows[0]['name'] == 'Siam'


def test_count(db):
    q = Query(db, 'users').where('age > ?', [27])
    
    assert q.count() == 2


def test_first(db):
    q = Query(db, 'users').where('age > ?', [27])
    row = q.first()

    assert row['name'] == 'Syed'

def test_get(db):
    q = Query(db, 'users').where('age = ?', [22])
    rows = q.get()

    if rows:
        assert rows['name'] == 'Shamim'

