import requests
import psycopg2
import os
from datetime import datetime

DB_HOST = os.getenv("DB_HOST", "localhost")

def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return [
        ("BTC", data["bitcoin"]["usd"], datetime.utcnow()),
        ("ETH", data["ethereum"]["usd"], datetime.utcnow())
    ]


def load_to_postgres(data):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,   
            database="crypto_db",
            user="airflow",
            password="airflow",
            port=5432          
        )

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id SERIAL PRIMARY KEY,
            symbol VARCHAR(10),
            price FLOAT,
            timestamp TIMESTAMP
        )
        """)

        insert_query = """
        INSERT INTO crypto_prices (symbol, price, timestamp)
        VALUES (%s, %s, %s)
        """

        cursor.executemany(insert_query, data)

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Data inserted successfully")

    except Exception as e:
        print(f"❌ DB Error: {e}")


if __name__ == "__main__":
    data = fetch_crypto_prices()
    load_to_postgres(data)
