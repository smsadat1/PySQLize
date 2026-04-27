class Executor:

    def __init__(self, connection):
        self.connection = connection

    def execute(self, query: str, params = None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or [])
        self.connection.conn.commit()
        return cursor
    
    def fetchall(self, query: str, params = None):
        cursor = self.execute(query, params)
        return cursor.fetchall()

    def fetchone(self, query: str, params = None):
        cursor = self.execute(query, params)
        return cursor.fetchone()
