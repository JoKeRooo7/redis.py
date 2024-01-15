# -*- coding: utf-8 -*-

import json
import redis
import random
import redis
import time

from server_data import *


def generate_number():
    return random.randint(10**9, 10**10 - 1)


def generate_json_message():
    from_account = generate_number()
    to_account = generate_number()
    amount = random.randint(-100000, 100000)

    message = {
        "metadata": {
            "from": from_account,
            "to": to_account
        },
        "amount": amount
    }

    return json.dumps(message)


def main():
    redis_info = redis.Redis(REDIS_HOST, REDIS_PORT)
    try:
        while True:
            message = generate_json_message()
            redis_info.lpush(SUBSCRIBE, message)
            #  redis_info.publish(SUBSCRIBE, message)
            logger.info("Sent message: " + message)
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Producer stopped")


if __name__ == "__main__":
    main()
