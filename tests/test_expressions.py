from sql.expression import Column

class User:
    age = Column('age')
    name = Column('name')

def test_expr_gt():
    expr_gt = User.age > 18
    sql, params = expr_gt.compile()

    assert sql == 'age > ?'
    assert params == [18]


def test_expr_lt():
    expr_gt = User.age < 40
    sql, params = expr_gt.compile()

    assert sql == 'age < ?'
    assert params == [40]


def test_expr_eq():
    expr_gt = User.age == 18
    sql, params = expr_gt.compile()

    assert sql == 'age = ?'
    assert params == [18]


def test_expr_ge():
    expr_gt = User.age >= 35
    sql, params = expr_gt.compile()

    assert sql == 'age >= ?'
    assert params == [35]


def test_expr_le():
    expr_gt = User.age <= 40
    sql, params = expr_gt.compile()

    assert sql == 'age <= ?'
    assert params == [40]


def test_expr_ne():
    expr_gt = User.age != 40
    sql, params = expr_gt.compile()

    assert sql == 'age != ?'
    assert params == [40]


def test_expr_or():
    expr_gt = (User.age > 20) | (User.name == 'Saif')
    sql, params = expr_gt.compile()

    assert sql == '(age > ?) OR (name = ?)'
    assert params == [20, "Saif"]


def test_expr_and():
    expr = (User.age > 22) & (User.name == 'Siam')
    sql, params = expr.compile()

    assert sql == '(age > ?) AND (name = ?)'
    assert params == [22, "Siam"]


def test_expr_not():
    expr = ~(User.age > 20)
    sql, params = expr.compile()

    assert sql == 'NOT (age > ?)'
    assert params == [20]


