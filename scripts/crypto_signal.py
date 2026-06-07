import psycopg2
from datetime import datetime


def detect_price_drop():
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="crypto_db",
            user="airflow",
            password="airflow",
            port=5432
        )

        cursor = conn.cursor()

        cursor.execute("""
            SELECT symbol, price, timestamp
            FROM crypto_prices
            WHERE timestamp >= NOW() - INTERVAL '15 minutes'
            ORDER BY symbol, timestamp ASC
        """)

        rows = cursor.fetchall()

        if not rows:
            print("⚠️ No data found for signal check")
            return

        data_by_symbol = {}

        for symbol, price, ts in rows:
            data_by_symbol.setdefault(symbol, []).append(price)

        for symbol, prices in data_by_symbol.items():
            if len(prices) < 2:
                continue
            
            latest_price = prices[-1]
            avg_price = sum(prices) / len(prices)

            if latest_price < 0.98 * avg_price:
                print(f"🚨 ALERT: {symbol} dropped >2%!")

                cursor.execute("""
                    INSERT INTO crypto_alerts 
                    (symbol, alert_type, price_at_alert, avg_price_10min, timestamp)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    symbol,
                    "PRICE_DROP",
                    latest_price,
                    avg_price,
                    datetime.utcnow()
                ))

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Signal check complete")

    except Exception as e:
        print(f"❌ Signal Error: {e}")


if __name__ == "__main__":
    detect_price_drop()
