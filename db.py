from contextlib import contextmanager

import psycopg2

DB_CONFIG = {
    "dbname": "players",
    "user" :"postgres",
    "password": "9405",
    "host" :"localhost",
    "port": 5432
}

@contextmanager
def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()


def execute_query(query, fetchone=False, fetchall=False, params=None):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
        if fetchone:
            return cursor.fetchone()
        if fetchall:
            return cursor.fetchall()
        conn.commit()
