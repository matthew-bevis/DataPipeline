import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME')
        )

        if connection.is_connected():
            print("Successfully connected to the MySQL database.")
        else:
            print("Connection failed.")
    except Exception as error:
        print("Error while connecting to database:", error)

    return connection

get_db_connection()
