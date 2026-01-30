# import redis

# redis_client = redis.Redis(
#     host="localhost",
#     port=6379,
#     decode_responses=True,
# )

import redis
import os

redis_client = redis.from_url(
    os.getenv("REDIS_URL"),
    decode_responses=True,
)

# Test
redis_client.set("tcp:test", "hello")
print(redis_client.get("tcp:test"))

