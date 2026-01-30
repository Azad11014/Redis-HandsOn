import json
from app.cache.client import redis_client


def get_cache(key : str):
    try:
        data = redis_client.get(key)
        if data:
            return json.loads(data)
        else:
            return None

    except Exception:
        return None
    
def set_cache(key : str, value, ttl=60):
    try:
        redis_client.setex(key, ttl, value=json.dumps(value))
    except Exception:
         return None
    
def delete_cache(key : str):
    redis_client.delete(key)