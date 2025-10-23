from fastapi import FastAPI, Request
import psycopg2
import json

app = FastAPI()

DB_PARAMS = dict(
    dbname="smart_home",
    user="piuser",
    password="pisecret",
    host="db",    # Must match your service name in docker-compose
    port="5432"
)

def get_conn():
    return psycopg2.connect(**DB_PARAMS)

@app.post("/sensor")
async def sensor_data(request: Request):
    data = await request.json()
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO sensor_events (sensor, value, ts) VALUES (%s, %s, %s)",
                (data.get("sensor"), json.dumps(data.get("value")), data.get("ts"))
            )
            conn.commit()
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "up"}
