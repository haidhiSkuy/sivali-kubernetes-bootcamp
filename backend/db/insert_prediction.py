import psycopg2
import os

class PostgresDb:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("POSTGRESS_DB"),
            user=os.getenv("POSTGRESS_USER"),
            password=os.getenv("POSTGRESS_PASSWORD"),
            host=os.getenv("POSTGRESS_HOST"),
            port=os.getenv("POSTGRESS_PORT")
        )
        self.cur = self.conn.cursor()

    def insert(self, patient_name : str, alzheimer_status : str):
        query = f"INSERT INTO patients (patient_name, alzheimer_status) VALUES (%s, %s)"
        values = (patient_name, alzheimer_status)
        self.cur.execute(query, values)
        self.conn.commit()