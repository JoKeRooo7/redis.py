import logging
REDIS_HOST = "localhost"
REDIS_PORT = 6379
QUEUE_NAME = "json_queue"
SUBSCRIBE = "transaction"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("transaction")
