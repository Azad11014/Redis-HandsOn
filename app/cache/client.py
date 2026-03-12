# import redis

# redis_client = redis.Redis(
#     host="localhost",
#     port=6379,
#     decode_responses=True,
# )

import redis
import os

#this is for upstash
# redis_client = redis.from_url(
#     os.getenv("REDIS_URL"),
#     decode_responses=True,
# )

#This is VPS
CA_CERT_PATH = "ca.crt"
redis_client = redis.from_url(
    os.getenv("VPS_REDIS_URL"),
    ssl_ca_certs=CA_CERT_PATH,  # Add the certificate!
    decode_responses=True,
)

# Test
redis_client.set("tcp:test", "hello")
print(redis_client.get("tcp:test"))

