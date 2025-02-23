from dotenv import load_dotenv

import os
import psycopg

class DatabaseConnection: 
    def __init__(self):
        load_dotenv()
        self.connection = None
        self.cursor = None
        self.database_name = os.getenv('DB_NAME')
        self.database_user = os.getenv('DB_USER')
        self.database_password = os.getenv('DB_PASSWORD')
    
    def connect(self):
        try:
            self.connection = psycopg.connect(
                dbname=self.database_name,
                user=self.database_user,
                password=self.database_password,
                host='localhost',
                port=5432,
                row_factory=psycopg.rows.dict_row
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Error to connect in database: {e}")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def execute(self, query):
        try:
            self.cursor.execute(query)
        except Exception as e:
            print(f"Error to execute query: {e}")
            self.connection.rollback()
            
    def commit(self):
        if self.connection:
            self.connection.commit()
            
    def fetch_all(self):
        return self.cursor.fetchall()