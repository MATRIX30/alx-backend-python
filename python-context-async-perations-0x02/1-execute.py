#!/usr/bin/env python3
import sqlite3
"""
a reusable context manager that takes a query as input and executes it, 
managing both connection and the query execution
"""

class ExecuteQuery:
    """
    class based custom context manager ExecuteQuery that takes the query: ”SELECT * FROM users WHERE age > ?”
    and the parameter 25 and returns the result of the query
    """
    def __init__(self, db_name:str, query:str, age:int):
        self.database_name = db_name
        self.age = age
        self.query = query
        self.connection = None
    def __enter__(self):
        """
        context manager open method
        """
        try:
            self.connection = sqlite3.connect(database=self.database_name)
            cursor = self.connection.cursor()
            results = cursor.execute(self.query, (self.age,)).fetchall()
            return results
        except Exception as e:
            print(f"Error: {e}")

    
    def __exit__(self, exc_type, exc_value, traceback):
        """
        method to close the connection on exit
        the with context
        """
        self.connection.close()
        return True


if __name__ == "__main__":
    with ExecuteQuery("users.db","SELECT * FROM users WHERE age > ?", 25) as db:
       print(db)