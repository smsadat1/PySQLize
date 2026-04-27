import sqlite3

class Connection:

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None 

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        return self.conn
    
    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def cursor(self):
        if not self.conn:
            self.connect()
        
        return self.conn.cursor()   # type: ignore
