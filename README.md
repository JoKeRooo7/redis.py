## Working with Redis in python


* [Installation and launch of Redis](#installing-the-redis-server-and-running-it)
* [Configuration settings](#configuring-the-configuration)
* [Produser](#produser-manufacturer)
* [Consumer](#consumer)


## Installing the Redis server and running it

* macOS
    * installing `brew install redis`
    * launching the `redis-server`


## Configuring the configuration

I created a separate file with the initial Redis settings - `server_data.py `.
* **REDIS_HOST** - the address where REDIS is running
* **REDIS_PORT** - the port through which REDIS
is running * **QUEUE_NAME** - the name of the queue in REDIS
* **SUBSCRIBE** - subscription channel where messages will be sent


## Produser (manufacturer)

Represented by a file `produser.py `.

The encoding format in the file is `utf-8'.
```python 
# -*- coding: utf-8 -*-
```

The `main()` function creates a `redis_info` host object.

It also has an infinite loop for generating messages in the `json` format. The `generate_json_message()` function is used for `json`. It generates a dictionary with data. The function returns a formatted string in json format from the message dictionary.

I add the generated json file to the top of the queue using the `lpush` method to the `SUBSCRIBE` subscription channel.

Information is output to the terminal using the `logger` object.

Generation occurs once every 1 second `time.sleep(1)`


## Consumer

File `consumer.py `. To run it, you need command-line arguments, numbers, and if they meet on the server, it will swap them out. (This is done so that if money is sent to a bad account (account number), it can be deployed back)

The `find_accounts(bad_accounts)` function accepts comma-separated numbers of bad accounts.

It reads all transactions from the beginning to the end.
`reverse()` - expands messages so that there are messages previously sent at the beginning.
Messages are being read in the loop, and if there is a number from `bad_accounts`, it expands the numbers and outputs them to the terminal.
