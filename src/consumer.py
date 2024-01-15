import json
import redis
import argparse

from server_data import *


def swap_accounts(message):
    if message["amount"] > 0:
        from_account = message["metadata"]["from"]
        to_account = message["metadata"]["to"]
        message["metadata"]["from"] = to_account
        message["metadata"]["to"] = from_account


def find_accounts(bad_accounts):
    try:
        redis_info = redis.Redis(REDIS_HOST, REDIS_PORT)
        message_range = redis_info.lrange(SUBSCRIBE, 0, -1)
        message_range.reverse()
        if not message_range:
            print("Messages are over")
        for message in message_range:
            message = json.loads(message.decode("utf-8"))
            if (str(message["metadata"]["from"]) in bad_accounts or
               str(message["metadata"]["to"]) in bad_accounts):
                swap_accounts(message)
            logger.info(f"Received message: {json.dumps(message)}")
    except KeyboardInterrupt:
        logger.info("Producer stopped")


def main():
    parser = argparse.ArgumentParser(description='logs')
    parser.add_argument(
        "-e",
        "--bad-accounts",  # длинный аариант аргумента -e
        required=False, default="",
        help="The lists with bad accounts")
    args = parser.parse_args()
    bad_accounts = args.bad_accounts.split(',')
    find_accounts(bad_accounts)


if __name__ == "__main__":
    main()
