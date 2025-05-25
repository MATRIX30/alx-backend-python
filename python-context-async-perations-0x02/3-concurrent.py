#!/usr/bin/env python3
import aiosqlite
import asyncio
"""
Run multiple database queries concurrently
using asyncio.gather.
"""

async def async_fetch_users():
    """
    fetches all user
    """
    async with aiosqlite.connect("users.db") as db:
        cursor =  await db.execute("SELECT * FROM users")
        result = await cursor.fetchall()
    return result

async def async_fetch_older_users():
    """
    fetches all users and users older than 40
    """
    async with aiosqlite.connect("users.db") as db:
        cursor =  await db.execute("SELECT * FROM users WHERE age > 40")
        result = await cursor.fetchall()
    return result

async def fetch_concurrently():
    result = await asyncio.gather(async_fetch_users(), async_fetch_older_users())
    print("all Task executed:", result)
    
asyncio.run(fetch_concurrently())