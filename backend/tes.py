import psycopg2
import os

conn = psycopg2.connect(
            dbname=os.getenv("POSTGRESS_DB"),
            user=os.getenv("POSTGRESS_USER"),
            password=os.getenv("POSTGRESS_PASSWORD"),
            host=os.getenv("POSTGRESS_HOST"),
            port=os.getenv("POSTGRESS_PORT")
        )
