from sql.query import Query

from tests.test_model import User


def test_expr_gt():
    expr_gt = User.age > 18
    sql, params = expr_gt.compile()

    assert sql == '(age > ?)'
    assert params == [18]


def test_expr_lt():
    expr_gt = User.age < 40
    sql, params = expr_gt.compile()

    assert sql == '(age < ?)'
    assert params == [40]


def test_expr_eq():
    expr_gt = User.age == 18
    sql, params = expr_gt.compile()

    assert sql == '(age = ?)'
    assert params == [18]


def test_expr_ge():
    expr_gt = User.age >= 35
    sql, params = expr_gt.compile()

    assert sql == '(age >= ?)'
    assert params == [35]


def test_expr_le():
    expr_gt = User.age <= 40
    sql, params = expr_gt.compile()

    assert sql == '(age <= ?)'
    assert params == [40]


def test_expr_ne():
    expr_gt = User.age != 40
    sql, params = expr_gt.compile()

    assert sql == '(age != ?)'
    assert params == [40]


def test_expr_or():
    expr_gt = (User.age > 20) | (User.name == 'Saif')
    sql, params = expr_gt.compile()

    assert sql == '((age > ?) OR (name = ?))'
    assert params == [20, "Saif"]


def test_expr_and():
    expr = (User.age > 22) & (User.name == 'Siam')
    sql, params = expr.compile()

    assert sql == '((age > ?) AND (name = ?))'
    assert params == [22, "Siam"]


def test_expr_not():
    expr = ~(User.age > 20)
    sql, params = expr.compile()

    assert sql == 'NOT (age > ?)'
    assert params == [20]

def test_expr_param_order():
    expr = (User.age > 20) & (User.name == 'Siam')
    sql, params = expr.compile()

    assert params == [20, 'Siam']


def test_between(db):
    q = Query(db, User).where(User.age.between(20, 30))
    assert q.count() == 7

def test_not_between_no_match(db):
    q = Query(db, User).where(User.age.between(999, 9999))
    assert q.count() == 0

def test_not_between_negation(db):
    q = Query(db, User).where(~User.age.between(20, 30))
    rows = q.all()

    assert all(not (20 <= r['age'] <= 30) for r in rows)


def test_in(db):
    q = Query(db, User).where(User.age.in_([18, 20, 22]))
    assert q.count() == 2 

def test_not_in_no_match(db):
    q = Query(db, User).where(User.age.in_([999, -1, 99999]))
    assert q.count() == 0

def test_not_in_negation(db):
    q = Query(db, User).where(~User.age.in_([18, 20, 22]))
    rows = q.all()

    assert all(r['age'] not in [18, 20, 22] for r in rows)

def test_in_empty(db):
    q = Query(db, User).where(User.age.in_([]))
    assert q.count() == 0


def test_like(db):
    q = Query(db, User).where(User.email.like('%@%.%'))
    rows = q.all()
    assert all('@' in r['email'] and r['email'].count('.') >= 1 for r in rows)

