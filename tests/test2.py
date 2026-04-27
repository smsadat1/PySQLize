# test query builder

from sql.query import Query

q = Query('users').where('age > ?', [18]).limit(5)

for row in q:
    print(dict(row))    

