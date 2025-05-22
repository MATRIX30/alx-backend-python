#!/usr/bin/env python3
"""module for transaction management """

import sqlite3 
import functools


def with_db_connection(func):
    """
    decorator that automatically handles opening
    and closing database connections
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect("users.db")
            return func(conn, *args, **kwargs)
        except Exception as e:
            print(f"Error:{e}")
        finally:
            conn.close()

    return wrapper

def transactional(func):
    """
    a decorator transactional(func) that ensures 
    a function running a database operation is wrapped
    inside a transaction.If the function raises an error,
    rollback; otherwise commit the transaction.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print(f"Error{e}")
            raise
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=322, new_email='Crawford_Cartwright@hotmail.com')