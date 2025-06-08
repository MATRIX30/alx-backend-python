#!/usr/bin/env python3
"""
Using Decorators to retry database queries
"""
import time
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


def retry_on_failure(retries=3, delay=2):
    """
    a retry_on_failure(retries=3, delay=2) decorator that
    retries the function of a certain number of times if it
    raises an exception
    """

    def decoratorFactory(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try_count = 0
            while try_count < retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Attempt {try_count + 1} failed: {e}")
                    time.sleep(delay)
                finally:
                    try_count += 1

        return wrapper

    return decoratorFactory


@with_db_connection
@retry_on_failure(retries=15, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    return cursor.fetchall()


# attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
