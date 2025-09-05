import csv

def load_third_party(connection, file_path_csv): 
    cursor = connection.cursor() 

    # Open and read the CSV file
    with open(file_path_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row if present

        for row in reader:
            # Unpack the values and insert into the database
            cursor.execute("""
                INSERT INTO sales (
                    event_id, event_date, event_code, event_name, end_date,
                    event_type, city, venue_id, price, ticket_count
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, row)

    connection.commit() 
    cursor.close() 
    print("CSV data loaded successfully.")
