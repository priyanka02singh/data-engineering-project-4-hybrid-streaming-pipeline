import pandas as pd
import os
from sqlalchemy import create_engine, text

HOST = os.getenv("DB_HOST", "localhost")

# PostgreSQL connection
DB_USER = "airflow"
DB_PASSWORD = "airflow"
DB_HOST = HOST
DB_PORT = "5432"
DB_NAME = "crypto_db"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS crypto_signals (
        id SERIAL PRIMARY KEY, 
        symbol VARCHAR(10), 
        price FLOAT, 
        short_ma FLOAT, 
        long_ma FLOAT, 
        signal VARCHAR(10), 
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """))


# Read latest crypto prices
query = """
SELECT *
FROM crypto_prices
ORDER BY timestamp ASC
"""

# Load into pandas dataframe
df = pd.read_sql(query, engine)

signals = []

for symbol in df['symbol'].unique():

    coin_df = df[df['symbol'] == symbol].copy()

    # Moving averages
    coin_df['short_ma'] = coin_df['price'].rolling(window=3).mean()
    coin_df['long_ma'] = coin_df['price'].rolling(window=5).mean()

    latest = coin_df.iloc[-1]

    signal = 'HOLD'

    if latest['short_ma'] > latest['long_ma']:
        signal = 'BUY'

    elif latest['short_ma'] < latest['long_ma']:
        signal = 'SELL'

    signals.append({
        'symbol': symbol,
        'price': latest['price'],
        'short_ma': latest['short_ma'],
        'long_ma': latest['long_ma'],
        'signal': signal
    })

signals_df = pd.DataFrame(signals)

# Save to PostgreSQL
signals_df.to_sql(
    'crypto_signals',
    engine,
    if_exists='append',
    index=False
)

print("✅ Signals generated successfully")
