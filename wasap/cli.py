from wasap.wasap import Wasap


def main():
    with Wasap() as wa:
        running = True
        while running:
            inputs = input("wasap:").split(" ")
            command = inputs[0]
            args = " ".join(inputs[1:])
            if not command:
                continue
            elif command == "chat" or command == "/c":
                if not args:
                    print("No contact name argument provided.")
                else:
                    try:
                        wa.select_chat(args)
                    except Exception as e:
                        print(f"Error selecting chat. {e}")
            elif command == "message" or command == "/m":
                if not args:
                    print("No message argument provided.")
                else:
                    try:
                        wa.send_message(args)
                    except Exception as e:
                        print(f"Error sending message. {e}")
            elif command == "quit" or command == "/q":
                running = False
                continue
            else:
                print("Unknown command.")
