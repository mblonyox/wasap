from multiprocessing.connection import Client


class WasapClient():
    def __init__(self, hostname: str, port: int, key: str):
        self.address = (hostname, port)
        self.authkey = bytes(key, "utf-8")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def connect(self):
        self.client = Client(self.address, authkey=self.authkey)

    def send_message(self, chat, message):
        if (not self.client) or self.client.closed:
            self.connect()
        self.client.send((chat, message))

    def close(self):
        self.client.close()
