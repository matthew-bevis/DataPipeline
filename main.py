from load_third_party import load_third_party
from connection import get_db_connection

def create_sales_table_if_not_exists(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            event_id INT,
            event_date DATE,
            event_code INT,
            event_name VARCHAR(255),
            end_date DATE,
            event_type VARCHAR(50),
            city VARCHAR(100),
            venue_id INT,
            price DECIMAL(10,2),
            ticket_count INT
        );
    """)
    connection.commit()
    cursor.close()

def query_popular_tickets(connection):
    cursor = connection.cursor()
    sql_statement = """
        SELECT event_name, SUM(ticket_count) AS total_tickets
        FROM sales
        WHERE event_date BETWEEN '2020-08-01' AND '2020-08-31'
        GROUP BY event_name
        ORDER BY total_tickets DESC;
    """
    cursor.execute(sql_statement)
    records = cursor.fetchall()  # List of tuples: [(event_name, total_tickets), ...]
    cursor.close()
    return records


def display_popular_tickets(records):
    if not records:
        print("No popular tickets found for the past month.")
        return

    print("Here are the most popular tickets in the past month:")
    for row in records:
        print(f"- {row[0]}")

if __name__ == "__main__":
    conn = get_db_connection()
    create_sales_table_if_not_exists(conn)
    load_third_party(conn, "third_party_sales_1.csv")
    popular_tickets = query_popular_tickets(conn)
    display_popular_tickets(popular_tickets)
