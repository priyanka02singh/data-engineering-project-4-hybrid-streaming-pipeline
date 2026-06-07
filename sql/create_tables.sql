CREATE TABLE IF NOT EXISTS crypto_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    price FLOAT,
    timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS crypto_alerts (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    alert_type VARCHAR(50),
    price_at_alert FLOAT,
    avg_price_10min FLOAT,
    timestamp TIMESTAMP
);
