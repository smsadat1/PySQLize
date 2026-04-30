from types import UnionType
from typing import Any


class Expression:

    def __lt__(self, other):
        return BinaryExpression(self, '<', Value(other))
    
    def __gt__(self, other):
        return BinaryExpression(self, '>', Value(other))

    def __eq__(self, other):
        return BinaryExpression(self, '=', Value(other))
    
    def __ne__(self, other):
        return BinaryExpression(self, '!=', Value(other))

    def __le__(self, other):
        return BinaryExpression(self, '<=', Value(other))
    
    def __ge__(self, other):
        return BinaryExpression(self, '>=', Value(other))
    
    def __or__(self, other):
        return BinaryExpression(self, 'OR', other)
    
    def __and__(self, other):
        return BinaryExpression(self, 'AND', other)
    
    def __invert__(self):
        return UnaryExpression('NOT', self)
    
    def __bool__(self):
        raise TypeError("Expressions cannot be used in boolean context")
    
    def compile(self):
        raise NotImplementedError


class Column(Expression):
    def __init__(self, name):
        self.name = name

    def between(self, low, high):
        return Between(self, low, high)
    
    def in_(self, values):
        return In(self, values)

    def like(self, pattern):
        return Like(self, pattern)

    def compile(self):
        return self.name, []

class Value(Expression):
    def __init__(self, value):
        self.value = value

    def compile(self):
        return '?', [self.value] 


class UnaryExpression(Expression):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr 

    def compile(self):
        sql, params = self.expr.compile()
        return f'{self.op} {sql}', params    


class BinaryExpression(Expression):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def compile(self):
        l_sql, l_params = self.left.compile()
        r_sql, r_params = self.right.compile()

        # wrap only if child is also a BinaryExpression
        # if isinstance(self.left, BinaryExpression):
        #     l_sql = f"({l_sql})"

        # if isinstance(self.right, BinaryExpression):
        #     r_sql = f"({r_sql})"

        return f'({l_sql} {self.op} {r_sql})', l_params + r_params
    

class Between(Expression):
    def __init__(self, column, low, high):
        self.column = column
        self.low = low
        self.high = high

    def compile(self):
        c_sql, c_params = self.column.compile()
        return f"{c_sql} BETWEEN ? AND ?", c_params + [self.low, self.high]


class Like(Expression):
    def __init__(self, column, pattern):
        self.column = column
        self.pattern = pattern

    def compile(self):
        c_sql, c_params = self.column.compile()
        return f"{c_sql} LIKE ?", c_params + [self.pattern]
    

class In(Expression):
    def __init__(self, column, values):
        self.column = column
        self.values = values

    def compile(self):

        if not self.values:
            return "1=0", []

        c_sql, c_params = self.column.compile()
        placeholders = ', '.join(['?'] * len(self.values))
        sql = f"{c_sql} IN ({placeholders})"
        return sql, c_params + list(self.values)