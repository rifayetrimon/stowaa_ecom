# app/core/redis.py
import logging
from redis import Redis
from app.core.settings import settings

# Initialize a global variable to hold the Redis client
redis_client = None

def init_redis():
    """
    Initialize the Redis client and assign it to the app's state.
    """
    logging.info("Redis client initialized")

    return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,decode_responses=True)

def close_redis(redis_client):
    """
    Close the Redis connection.
    """
    if redis_client:
        redis_client.close()
        logging.info("Redis client closed")
        redis_client = None
