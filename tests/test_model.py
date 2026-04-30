from sql.expression import Column

class User:
    __tablename__ = 'users'
    age = Column('age')
    name = Column('name')
    email = Column('email')
