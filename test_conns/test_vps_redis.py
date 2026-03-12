import redis

r = redis.Redis(
    # host="<VPS_SERVER_IP>",
    # port=VPS_REDIS_PORT,
    # password="<REDIS_PASSWORD",
    # ssl=True,
    # ssl_ca_certs="ca.crt",  # Path to downloaded certificate
    # decode_responses=True
)

print(r.ping())  # True
r.set("hello", "world")
print(r.get("hello"))  # world