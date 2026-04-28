from sql.query import Query

nq = Query('users').where('age > ?', [18]).count()
fq = Query('users').where('age > ?', [18]).first()

print(nq)
print(dict(fq))



