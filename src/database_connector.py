import mysql.connector
from mysql.connector import errorcode
from config import database_config


class DatabaseConnector:
    connection_count = 0
    disconnect_count = 0

    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**database_config.database_config)
            DatabaseConnector.connection_count += 1
            print(f"Connected to the database {DatabaseConnector.connection_count}")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: Access denied. Check your database credentials.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Error: Database does not exist.")
            else:
                print(f"Error: {err}")
            raise


    def disconnect(self):
        if self.connection == None:
            return
        if self.connection.is_connected():
            self.connection.close()
            DatabaseConnector.disconnect_count += 1
            print(f"Disconnected from the database {DatabaseConnector.connection_count}")

    def execute_query(self, query, data=None):
        cursor = self.connection.cursor(dictionary=True)
        try:
            if data:
                cursor.execute(query, data)
                self.connection.commit()
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.connection.rollback()
            raise
        finally:
            cursor.close()