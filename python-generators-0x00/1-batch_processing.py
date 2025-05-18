import seed

def stream_users_in_batches(batch_size):
    """Generator that yields users in batches of batch_size."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch
    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25 and prints them."""
    for batch in stream_users_in_batches(batch_size):  # 1st loop
        for user in batch:  # 2nd loop
            if user['age'] > 25:
                print(user)