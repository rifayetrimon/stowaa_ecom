from fastapi import FastAPI, Depends, HTTPException
from redis import Redis
import uvicorn
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.db.session import get_db
from app.db.base import Base
from app.db.session import engine
from app.db.models import *
import json
import httpx
from app.core.redis import init_redis, close_redis

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "message": "Database connection is healthy."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")


# Redis lifecycle management
@app.on_event("startup")
async def startup_event():
    app.state.redis = init_redis()
    app.state.http_client = httpx.AsyncClient()



@app.on_event("shutdown")
async def shutdown_event():
    close_redis(app.state.redis)


@app.get("/redis")
async def redis_check():

    value = app.state.redis.get("redis")

    if value is None:
        response = await app.state.http_client.get("https://dummyapi.online/api/movies")

        value = response.json()
        data_str = json.dumps(value)
        app.state.redis.set("redis", data_str, ex=60)

    return json.loads(value)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
