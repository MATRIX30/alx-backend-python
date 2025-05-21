#!/usr/bin/env python3
import sqlite3
import logging
import functools
#### decorator to lof SQL queries

## configuring the logging library
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M"
                    )

def log_queries(func) -> None:
    """
    decorator to log database queries executed
    by any function
    """
    @functools.wraps(func) # preventing wrapper from overriding original functions info
    def wrapper(*args, **kwargs):
        """
        decorator wrapper function
        """
        if args:
            query = args[0]
        elif kwargs:
            query = kwargs["query"]
        else:
            pass
        logging.info(query)
        func(*args, **kwargs)
    return wrapper
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    #cursor.execute(query)
    cursor.execute("SELECT *FROM users")
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
