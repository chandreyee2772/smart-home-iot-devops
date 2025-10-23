CREATE TABLE IF NOT EXISTS sensor_events (
    id SERIAL PRIMARY KEY,
    sensor VARCHAR(32),
    value TEXT,
    ts TIMESTAMP
);
