from multiprocessing.connection import Listener
from wasap.wasap import Wasap
import click
import string
import random


@click.command()
@click.option("--hostname", "-h", default="localhost", help="Hostname / Network Interface to use for binding")
@click.option("--port", "-h", default=9292, help="Port number to use for binding")
@click.option("--key", "-k", help="Set the secret key instead of generated")
def main(hostname: str = "localhost", port: int = 9292, key: str = None):
    if not key:
        key = rand_key()
        print(f"secret-key: {key}")
    run_service(hostname, port, bytes(key, "utf-8"))


def rand_key(n=16):
    chars = string.ascii_uppercase + string.digits
    return "".join(random.choices(chars, k=n))


def run_service(hostname: str, port: int, key: bytes):
    with Wasap() as wa:
      print("Whatsapp Web is ready...")
      with Listener((hostname, port), authkey=key) as listener:
        print(f"Wasap service running on {hostname}:{port}")
        while True:
          conn = listener.accept()
          print(f"Established connection from {listener.last_accepted}")
          try:
            while True:
              (chat, message) = conn.recv()
              print(f"sending message to {chat} with message: {message}")
              wa.select_chat(chat)
              wa.send_message(message)
          except:
            conn.close()
