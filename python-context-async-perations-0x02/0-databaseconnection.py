#!/usr/bin/env python3
import sqlite3
"""
custom context manager DatabaseConnection using the __enter__ 
and the __exit__ methods
"""

class DatabaseConnection:
    """
    custom context manager class
    """
    def __init__(self, db_name:str):
        self.database_name = db_name
        self.connection = None
    def __enter__(self):
        """
        context manager open method
        """
        try:
            self.connection = sqlite3.connect(database=self.database_name)
            return self.connection
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
    with DatabaseConnection("users.db") as db:
        cursor = db.cursor()
        results = cursor.execute("select * from Users;").fetchone()
    print(results)