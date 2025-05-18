import mysql.connector
import csv
import uuid

def connect_db():
    """Connect to MySQL server (not to a specific database)."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Set your MySQL root password if needed
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Create ALX_prodev database if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Set your MySQL root password if needed
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Create user_data table if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        );
    """)
    connection.commit()
    print("Table user_data created successfully")
    cursor.close()

def insert_data(connection, csv_file):
    """Insert data from CSV into user_data table if not already present."""
    cursor = connection.cursor()
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Check if user_id already exists
            cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (row['user_id'],))
            if cursor.fetchone():
                continue  # Skip if already exists
            cursor.execute(
                "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                (row['user_id'], row['name'], row['email'], row['age'])
            )
    connection.commit()
    cursor.close()
