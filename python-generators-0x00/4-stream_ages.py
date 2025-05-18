import seed

def stream_user_ages():
    """Generator that yields user ages one by one."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield age
    cursor.close()
    connection.close()

def average_user_age():
    """Calculates and prints the average age using the generator."""
    total = 0
    count = 0
    for age in stream_user_ages():  # Only one loop used
        total += age
        count += 1
    avg = total / count if count else 0
    print(f"Average age of users: {avg}")

if __name__ == "__main__":
    average_user_age()