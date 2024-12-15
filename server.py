"""
postgres Database containing
- player token: str
- field: str   --> Dict[Any, Any] (the tiles we got from setup()
-
"""
from tkinter import Tk

import psycopg2
from zero import ZeroServer

from bands import RegisteredPlayer
from db import execute_query, DB_CONFIG
from minesweeper import Minesweeper

app = ZeroServer(port=5559)
window = Tk()
window.title("Minesweeper")

FIELD = Minesweeper(window).setup()


def fetch_player_count():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM PLAYERS;"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    conn.close()
    return count


def add_player(token: str, field):
    query = """
    INSERT INTO players (token, field) VALUES (%s, %s);
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    # if field is None:
    #     cursor.execute("INSERT INTO players (token, field) VALUES (%s, %s);", (token, FIELD))
    # else:
    cursor.execute("INSERT INTO players (token, field) VALUES (%s, %s);", (token, field))
    conn.commit()
    conn.close()


def fetch_field(token: str):
    query = """
        SELECT field FROM players WHERE token = %s;
    """
    return execute_query(query, fetchone=True, params=(token,))


def generate_token(player_token) -> str:
    return f"miner-{player_token}"


@app.register_rpc
async def register_player() -> RegisteredPlayer:
    """
    first we will get the number of players in the db
    """
    players_count = fetch_player_count()
    if players_count < 2:
        if players_count == 0:
            token_for_player = 1
            field=FIELD
        else:
            field = fetch_field(token="miner-1")
            # fetch players1's field
            token_for_player = 2
        token = generate_token(token_for_player)
        add_player(field=field, token=token)
        return RegisteredPlayer(token, field, is_registered=True)
    return RegisteredPlayer(is_registered=False)


if __name__ == '__main__':
    connection = psycopg2.connect(
        dbname="players",
        user="postgres",
        password="9405",
        host="localhost",
        port=5432
    )
    cursor = connection.cursor()

    # dropping if already exists
    cursor.execute("DROP TABLE IF EXISTS players;")

    print("here i come")
    # creating table player
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            player_num SERIAL PRIMARY KEY,
            token TEXT UNIQUE NOT NULL,
            field TEXT NOT NULL
        );
    ''')
    print("here i go")

    connection.commit()
    connection.close()
    app.run(workers=1)
