#!/usr/bin/env python3
"""
"""
import time
import sqlite3 
import functools


query_cache = {}


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


def cache_query(func):
    """
    decorator cache_query(func)
    that caches query results based on
    the SQL query string
    """
    def wrapper(conn, *args, **kwargs):
        if args:
            query = args[0]
        else:
            query = kwargs["query"]
        
        
        # standardizing string
        query = query.replace(" ", "").strip().lower()

        if query in query_cache:
            print("reading from cache memory")
            result = query_cache[query]
        else:
            result = func(conn, *args, **kwargs)
            query_cache[query] = result
        return result
    return wrapper
    
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")